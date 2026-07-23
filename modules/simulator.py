import time
from modules.utils import get_valid_float
def show_introduction():
    print("=" * 60)
    print("                 ECHO - LIFE DECISION SIMULATOR")
    print("=" * 60)
    print()

    print("Connecting to your future...")
    time.sleep(1.5)
    print()

    print("Connection established.")
    time.sleep(1)
    print("-" * 60)
    print()

    print("I'm Echo.")
    time.sleep(1)
    print()

    print("I'm not here to predict your future.")
    time.sleep(1)
    print()

    print("I'm here to show you")
    print("the future you're building.")
    print()

    print("Let's begin.")
    print()

    print("-" * 60)
    print()





def get_name():
    print("What's your name?")
    name = input("> ")
    return name


def get_goal():
    print("What's your biggest goal?")
    goal = input("> ")
    return goal


def get_habit():
    print("What ONE daily habit will help you achieve it?")
    habit = input("> ")
    return habit

def get_daily_hours():
    print("How many hours every day?")
    hours = get_valid_float("> ")
    return hours

def generate_future_echo(name, goal, habit, hours):
    hours_30_days = hours * 30 
    hours_1_year = hours * 365
    hours_5_years = hours * 365 * 5
    print("=" * 60)
    print("                 FUTURE ECHO ACTIVATED")
    print("=" * 60)
    print()
     
    print("Hello,", name + ".")
    print()
    print("Analyzing your future...")
    time.sleep(2)
    print()
    print("I've analyzed your daily choices...")
    print()

    print("Your goal          : " , goal)
    print("Your daily habit   : " , habit)
    print("Daily Commitment   : " , hours ,  "hours/a day")
    print()
    print("-" * 60)
    print()
    print("If you stay consistent...")
    print()

    print("30 Days   →", hours_30_days, "hours invested")
    print()

    print("1 Year    →", hours_1_year, "hours invested")
    print()

    print("5 Years   →", hours_5_years, "hours invested")
    
    print()
    print("-" * 60)
    print()

    print("Remember...")
    print()

    print("Your future isn't built in one day.")
    print()

    print("It's built by repeating today's habit")
    print("again...")
    print("and again...")
    print("and again.")
    print()

    print("                         — Echo")

    print("=" * 60)

def start_simulation():
    show_introduction()
    name = get_name()
    goal = get_goal()
    habit = get_habit()
    hours = get_daily_hours()
    generate_future_echo(name, goal, habit, hours)
 