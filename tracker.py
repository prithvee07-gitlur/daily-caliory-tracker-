# Name: Priithvee Singh Yadav
# Date: 18/10/2025
# Project Title: Daily Calorie Tracker CLI

import datetime

def welcome():
    print("-"*50)
    print("       Welcome to the Daily Calorie Tracker!      ")
    print("-"*50)
    print("\n>This tool helps you to log your meals and track your daily calorie intake.")
    print(">You can enter your meals, see the total, and compare it with your daily limit.\n\n")

welcome()

meal_l=[]
cal_l=[]

num=int(input("How many meals would you like to log?\n "))
print()

for i in range(num):

    m_name=input(f"Enter the name for meal #{i + 1}: ")
    cal=float(input(f"Enter the calories for {m_name}: "))

    meal_l.append(m_name)
    cal_l.append(cal)

total=sum(cal_l)
avg=total/num 

limit=float(input("\nWhat is your daily calorie limit?\n"))

print("\n\n----- Your Calorie Report -----")
print("-"*35)
print("Meal Name\t\tCalories")
print("-"*35)

for i in range(num):
    print(f"{meal_l[i].ljust(20)}\t {cal_l[i]}")
    print()
print("-"*35)

print(f"Total Calories:\t\t{total:.2f}")

print(f"Average Calories/Meal:\t{avg:.2f}")

print(f"Your Daily Limit:\t{limit:.2f}")

print("-"*35)
l_stat=""

sub=total-limit
if total>limit:
    print(f"\n⚠️  Warning! You are {sub:.2f} calories OVER your daily limit. ⚠️")
    l_stat = f"Over limit by {sub:.2f} calories."

else:
    print(f"\n✅  Success! You are within your daily limit. ✅\nYou have {-sub:.2f} calories left.")
    l_stat = f"Under limit by {-sub:.2f} calories."
    
s=input("\nWould you like to save this session to a log file? (yes/no): ").lower()
if s in ['yes', 'y']:
    with open("calorie.txt", "a") as f: 
        f.write("--- Calorie Session Log ---\n")
        f.write(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-"*30 + "\n")

        for i in range(num):
            f.write(f"{meal_l[i]} {cal_l[i]}\n")
        f.write("-"*30 + "\n")
        f.write(f"Total Calories: {total:.2f}\n")
        f.write(f"Average Calories: {avg:.2f}\n")
        f.write(f"Daily Limit: {limit:.2f}\n")
        f.write(f"Status: {l_stat}\n")
        f.write("-"*30 + "\n\n")
    print("Session saved successfully to calorie.txt")
else:
    print("Log not saved. Have a great day!")