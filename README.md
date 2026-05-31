# 🧮 Calculator Bot

A Telegram bot that performs basic arithmetic operations through an interactive step-by-step interface.

## Features

- Addition, Subtraction, Multiplication, Division
- Interactive inline keyboard for selecting operations
- Input validation with helpful error messages
- Per-user state management — each user has their own independent session

## How It Works

```
1. User sends /start
2. Bot asks for the first number
3. User sends a number
4. Bot shows operation buttons (➕ ➖ ✖️ ➗)
5. User taps an operation
6. Bot asks for the second number
7. User sends a number
8. Bot returns the result
```

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/Zuktus/calculator-bot
cd calculator-bot
```

**2. Install dependencies**
```bash
pip install python-telegram-bot
```

**3. Get a bot token**

Talk to [@BotFather](https://t.me/BotFather) on Telegram:
```
/newbot
```
Copy the token it gives you.

**4. Set the token as an environment variable**

Linux / macOS:
```bash
export BOT_TOKEN="your_token_here"
```

Windows:
```bash
set BOT_TOKEN=your_token_here
```

**5. Run the bot**
```bash
python bot.py
```

## Project Structure

```
calculator-bot/
├── bot.py        # Main bot logic
└── README.md
```

## What I Learned Building This

- How to manage multi-step conversations using `context.user_data`
  to store and retrieve user input across different messages
- How to handle inline keyboard callbacks and react
  differently based on `query.data`
- The difference between `MessageHandler` and `CallbackQueryHandler`
  and when to use each one
- How to validate user input with `try/except` and use
  `return` to stop execution when input is invalid
- How to use `update.message` and `query.message`
  and why they are different

## Tech Stack

- Python 3.10+
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
