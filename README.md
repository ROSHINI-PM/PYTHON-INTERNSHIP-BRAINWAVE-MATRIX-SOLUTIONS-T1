# PYTHON-INTERNSHIP-BRAINWAVE-MATRIX-SOLUTIONS-T1

This is a Python-based ATM simulation program that allows users to perform basic banking operations such as checking balance, depositing money, withdrawing money, and printing transaction receipts.

✨ Features
✅ Card Insertion and Authentication
Simulates inserting a card and entering a PIN to verify user identity.

✅ Check Balance
View the current account balance.

✅ Deposit Money
Add funds to your account.

✅ Withdraw Money
Withdraw funds from your account (with balance check).

✅ Print Receipt
Displays a summary of your latest transactions and balance.

✅ Exit
Safely exit the ATM interface.

▶️ How to Use
Clone or Download this project to your local machine.

Open the file in any Python environment (e.g., VS Code, PyCharm, or terminal).

Run the script using:

nginx
Copy
Edit
python atm.py
Follow the on-screen instructions to interact with the ATM interface.

🧠 Code Structure
🔹 ATM Class
Manages:

Authentication (username & PIN)

Balance operations (check, deposit, withdraw)

Transaction tracking

Responsible for handling user data and actions.

🔹 main() Function or Tkinter Mainloop
Handles:

GUI display

Button interactions

Screens for login, deposit, withdrawal, and more

👥 Default Users
Three users are predefined in the system for demonstration:

Username: alice, PIN: 1234, Balance: 5000

Username: bob, PIN: 5678, Balance: 3000

Username: charlie, PIN: 0000, Balance: 10000

You can modify or add more users in the self.users dictionary in the code.



You can modify or extend this list in the code (self.users dictionary).

🤝 Contributing
Found an issue or want to improve the project?
Feel free to fork this repository, create a new branch, and submit a pull request. Contributions are welcome! 👨‍💻👩‍💻

🛠 Requirements
Python 3.x

No external libraries required (uses built-in tkinter)

