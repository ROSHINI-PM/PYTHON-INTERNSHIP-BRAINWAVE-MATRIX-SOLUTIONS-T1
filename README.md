# PYTHON-INTERNSHIP-BRAINWAVE-MATRIX-SOLUTIONS-T1
This is a Python-based ATM simulation program that allows users to perform basic banking operations such as checking balance, depositing money, withdrawing money, and printing transaction receipts.

Features
Card Insertion and Authentication
Simulates inserting a card and entering a PIN to authenticate the user.

Check Balance
Allows the user to view their current account balance.

Deposit Money
Enables the user to deposit money into their account.

Withdraw Money
Allows the user to withdraw funds, with validation for sufficient balance.

Print Receipt
Displays a summary of recent transactions and current balance.

Exit
Lets the user safely exit the ATM interface.

How to Use
Clone or download the project to your local machine.

Open the Python file (atm.py or similar) in your preferred Python environment.

Run the script using:

nginx
Copy
Edit
python atm.py
Follow the on-screen prompts to perform ATM operations.

Code Structure
ATM Class
Handles all core functionalities, including:

User authentication

Balance checking

Deposits and withdrawals

Printing transaction receipts

Main Function or Tkinter GUI
Responsible for:

User interface

Input fields and buttons

Screen navigation

Default Users
Three users are predefined in the system for demonstration:

Username: alice, PIN: 1234, Balance: 5000

Username: bob, PIN: 5678, Balance: 3000

Username: charlie, PIN: 0000, Balance: 10000

You can modify or add more users in the self.users dictionary in the code.

Contributing
If you'd like to suggest improvements or fix issues, feel free to fork the repository and submit a pull request. Contributions are welcome.

Requirements
Python 3.x

Tkinter (included with standard Python installations)
