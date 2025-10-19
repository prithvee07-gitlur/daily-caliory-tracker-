# daily-caliory-tracker #

🥗 Daily Calorie Tracker CLI (Command Line Interface)
This is a simple Python command-line application designed to help users log their daily meals, calculate their total calorie intake, and compare it against a set daily limit.

🌟 Features
Interactive Meal Logging: Prompts the user to enter the name and calorie count for each meal.

Calculation: Automatically sums up the total calories consumed and average calories per meal.

Daily Limit Comparison: Checks if the total calories are over or under a user-defined daily limit.

Detailed Report: Displays a summary report including meal details, total calories, average calories per meal, and status relative to the limit.

Session Logging: Optionally saves the entire session to a persistent log file calorie.txt with a timestamp.

📝 Code Structure (Tracker.py)
The script is straightforward and executes sequentially:

1.Imports: Imports the datetime module for timestamping the log file.
2.welcome() function: Prints a friendly introduction to the user.
3.Input Collection: Gathers the number of meals, then loops to collect meal names and calorie values, storing them in meal_l and cal_l lists.
4.Calculations: Computes the total and avg calories, and asks for the limit.
5.Report Generation: Prints the formatted "Calorie Report," including the over/under status with clear warnings/success messages.
6.Log File Handling: Asks the user to save the session. If confirmed, it appends the current session's data to the calorie.txt file.
📜 Log File (calorie.txt)
The calorie.txt file is used to maintain a historical record of all saved sessions. Each session is appended with a timestamp and includes all critical information:

Timestamp

List of meals and their calories

Total Calories

Average Calories

Daily Limit

Final Status (Over or Under limit)
