Transaction Tracker CLI
A lightweight, Python-based Command Line Interface (CLI) for managing and auditing personal financial transactions. Built with Python dataclasses for speed and reliability.

Description
The Transaction Tracker CLI helps you log daily expenses and income without leaving your terminal. It stores data locally and provides quick summaries of your spending habits by category. This project was designed to demonstrate clean Python architecture and efficient data handling.

Features
Easy Logging: Quickly add transactions with category and description.

Smart Defaults: Automatically handles timestamps if a date isn't provided.

Categorization: Group your spending (e.g., Food, Rent, Utilities).

Lightweight: Zero heavy database dependencies; uses local storage.

Data Integrity: Uses Python Type Hinting to ensure data accuracy.

Installation & Setup
Prerequisites
Python 3.8 or higher

git (optional, for cloning)

Steps
Clone the repository:

Bash
git clone https://github.com/[USER_NAME]/[REPO_NAME].git
cd [REPO_NAME]
Create a Virtual Environment (Recommended):

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
(Note: Since this uses standard libraries, this step might be empty, or you can add pip install -r requirements.txt if you add extra tools later.)

Sample CLI Usage
Once the script is set up, you can interact with it directly from your terminal.

Adding a Transaction
To log a new expense, run the add command:

Bash
python tracker.py add --amount 15.50 --category "Food" --description "Lunch at Cafe"
Viewing Transactions
To see a formatted list of all your logs:

Bash
python tracker.py list
Screenshot
(Tip: Replace the link above with a real screenshot from your terminal! You can upload the image to your GitHub repo and link it like this: ![](./docs/screenshot.png))

Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

License
Distributed under the MIT License. See LICENSE for more information.
