from email import message
from multiprocessing import context
from pydoc import text
from re import U
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.ext import MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["step"] = "waiting_first_number"
    await update.message.reply_text("Enter the first number: ")

async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    step = context.user_data.get("step")
    if step == "waiting_first_number":
        try:
            context.user_data["first_number"] = int(update.message.text)
        except ValueError:
            await update.message.reply_text("Pleas enter a number !")
            return

        context.user_data["step"] = "waiting_operation"
        keyboard = [
            [InlineKeyboardButton("➕", callback_data="Sum"), InlineKeyboardButton("➖", callback_data="Subtraction")],
            [InlineKeyboardButton("✖️", callback_data="Cross"), InlineKeyboardButton("➗", callback_data="Division")]
        ]
        markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Choose an operation:", reply_markup=markup)

    elif step == "waiting_second_number":
        try:
            context.user_data["second_number"] = int(update.message.text)
        except ValueError:
            await update.message.reply_text("Please Enter a number !")
            return

        num1 = context.user_data["first_number"]
        num2 = context.user_data["second_number"]
        op = context.user_data["operation"]
        if op == "Sum":
            resault = num1 + num2
        elif op == "Subtraction":
            resault = num1 - num2
        elif op == "Cross":
            resault = num1 * num2
        elif op == "Division":
            resault = num1 / num2
        
        await update.message.reply_text(f"The answer is {resault}")

async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data["operation"] = query.data
    context.user_data["step"] = "waiting_second_number"
    await query.message.reply_text("Enter the second number: ")

app = Application.builder().token("").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
app.add_handler(CallbackQueryHandler(on_button))
app.run_polling()
