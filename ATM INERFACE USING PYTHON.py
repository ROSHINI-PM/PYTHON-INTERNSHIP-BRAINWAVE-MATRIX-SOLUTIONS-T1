#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("Brainwave Matrix ATM")
        self.root.geometry("400x520")
        self.root.config(bg="#2c3e50")

        # Dummy user data as dictionary {username: (pin, balance)}
        self.users = {
            "alice": ("1234", 5000),
            "bob": ("5678", 3000),
            "charlie": ("0000", 10000)
        }

        self.current_user = None
        self.balance = 0

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Welcome to ATM",
                 font=("Helvetica", 16, "bold"), fg="white", bg="#2c3e50").pack(pady=20)

        tk.Label(self.root, text="Username:", font=("Helvetica", 14), fg="white", bg="#2c3e50").pack(pady=5)
        self.username_entry = tk.Entry(self.root, font=("Helvetica", 14), justify="center")
        self.username_entry.pack(pady=5)
        self.username_entry.focus()

        tk.Label(self.root, text="Enter PIN:", font=("Helvetica", 14), fg="white", bg="#2c3e50").pack(pady=5)
        self.pin_entry = tk.Entry(self.root, show="*", font=("Helvetica", 14), justify="center")
        self.pin_entry.pack(pady=5)

        tk.Button(self.root, text="Login", font=("Helvetica", 14, "bold"),
                  bg="#27ae60", fg="white", width=10, command=self.check_login).pack(pady=20)

    def check_login(self):
        username = self.username_entry.get().strip().lower()
        entered_pin = self.pin_entry.get()

        if username in self.users:
            correct_pin, balance = self.users[username]
            if entered_pin == correct_pin:
                self.current_user = username
                self.balance = balance
                self.create_main_menu()
            else:
                messagebox.showerror("Invalid PIN", "Incorrect PIN entered. Try again.")
                self.pin_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid Username", "Username not found. Try again.")
            self.username_entry.delete(0, tk.END)
            self.pin_entry.delete(0, tk.END)

    def create_main_menu(self):
        self.clear_screen()

        tk.Label(self.root, text=f"Welcome, {self.current_user.capitalize()}!", font=("Helvetica", 18, "bold"),
                 fg="white", bg="#2c3e50").pack(pady=20)

        btn_config = {"font": ("Helvetica", 14), "width": 15, "bg": "#2980b9", "fg": "white", "bd": 0, "relief": "ridge"}

        tk.Button(self.root, text="Check Balance", command=self.check_balance, **btn_config).pack(pady=10)
        tk.Button(self.root, text="Deposit", command=self.deposit_screen, **btn_config).pack(pady=10)
        tk.Button(self.root, text="Withdraw", command=self.withdraw_screen, **btn_config).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.logout, **btn_config).pack(pady=10)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ₹{self.balance}")

    def deposit_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Deposit Amount", font=("Helvetica", 18, "bold"),
                 fg="white", bg="#2c3e50").pack(pady=30)

        self.amount_entry = tk.Entry(self.root, font=("Helvetica", 14), justify="center")
        self.amount_entry.pack(pady=10)
        self.amount_entry.focus()

        tk.Button(self.root, text="Deposit", font=("Helvetica", 14, "bold"),
                  bg="#27ae60", fg="white", width=10, command=self.deposit_amount).pack(pady=20)

        tk.Button(self.root, text="Back", font=("Helvetica", 12),
                  bg="#c0392b", fg="white", width=8, command=self.create_main_menu).pack()

    def deposit_amount(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError
            self.balance += amount
            # Update the user's balance in the dictionary
            self.users[self.current_user] = (self.users[self.current_user][0], self.balance)
            messagebox.showinfo("Deposit Successful", f"₹{amount} deposited successfully!")
            self.create_main_menu()
        except ValueError:
            messagebox.showerror("Invalid Amount", "Please enter a valid positive number.")
            self.amount_entry.delete(0, tk.END)

    def withdraw_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Withdraw Amount", font=("Helvetica", 18, "bold"),
                 fg="white", bg="#2c3e50").pack(pady=30)

        self.amount_entry = tk.Entry(self.root, font=("Helvetica", 14), justify="center")
        self.amount_entry.pack(pady=10)
        self.amount_entry.focus()

        tk.Button(self.root, text="Withdraw", font=("Helvetica", 14, "bold"),
                  bg="#e67e22", fg="white", width=10, command=self.withdraw_amount).pack(pady=20)

        tk.Button(self.root, text="Back", font=("Helvetica", 12),
                  bg="#c0392b", fg="white", width=8, command=self.create_main_menu).pack()

    def withdraw_amount(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError
            if amount > self.balance:
                messagebox.showerror("Insufficient Balance", "You do not have enough balance.")
            else:
                self.balance -= amount
                # Update the user's balance in the dictionary
                self.users[self.current_user] = (self.users[self.current_user][0], self.balance)
                messagebox.showinfo("Withdrawal Successful", f"₹{amount} withdrawn successfully!")
                self.create_main_menu()
        except ValueError:
            messagebox.showerror("Invalid Amount", "Please enter a valid positive number.")
            self.amount_entry.delete(0, tk.END)

    def logout(self):
        self.current_user = None
        self.balance = 0
        self.create_login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    atm_app = ATM(root)
    root.mainloop()


# In[ ]:




