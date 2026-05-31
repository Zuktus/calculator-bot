import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#222")

        self.expression = ""

        self.display = tk.Entry(
            root,
            font=("Arial", 24),
            bd=0,
            bg="#333",
            fg="white",
            justify="right",
            insertbackground="white",
        )
        self.display.pack(fill="both", padx=10, pady=20, ipady=15)

        buttons = [
            ["C", "<-", "(", ")"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["+/-", "0", ".", "+"],
            ["="],
        ]

        btn_frame = tk.Frame(root, bg="#222")
        btn_frame.pack(expand=True, fill="both", padx=10, pady=5)

        for r, row in enumerate(buttons):
            btn_frame.rowconfigure(r, weight=1)
            for c, label in enumerate(row):
                btn_frame.columnconfigure(c, weight=1)
                if label in ("/", "*", "-", "+", "="):
                    bg = "#ff9500"
                elif label in ("C", "<-"):
                    bg = "#a5a5a5"
                else:
                    bg = "#555"
                btn = tk.Button(
                    btn_frame,
                    text=label,
                    font=("Arial", 18, "bold"),
                    bg=bg,
                    fg="white",
                    bd=0,
                    activebackground="#777",
                    command=lambda x=label: self.on_click(x),
                )
                if label == "=":
                    btn.grid(row=r, column=0, columnspan=4, sticky="nsew", padx=3, pady=3)
                else:
                    btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

        self._bind_keys()
        self.root.focus_set()

    def _bind_keys(self):
        for ch in "0123456789+-*/().":
            self.root.bind(ch, lambda e, c=ch: self.on_click(c))
        self.root.bind("<Return>", lambda e: self.on_click("="))
        self.root.bind("<KP_Enter>", lambda e: self.on_click("="))
        self.root.bind("=", lambda e: self.on_click("="))
        self.root.bind("<Escape>", lambda e: self.on_click("C"))
        self.root.bind("<Delete>", lambda e: self.on_click("C"))
        self.root.bind("<BackSpace>", lambda e: self.on_click("<-"))

    def on_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "<-":
            if self.expression == "Error":
                self.expression = ""
            else:
                self.expression = self.expression[:-1]
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.expression = result
            except Exception:
                self.expression = "Error"
        elif char == "+/-":
            if self.expression.startswith("-"):
                self.expression = self.expression[1:]
            elif self.expression:
                self.expression = "-" + self.expression
        else:
            if self.expression == "Error":
                self.expression = ""
            self.expression += char

        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
