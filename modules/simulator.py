import time
from modules.utils import get_valid_float
from modules.storage import profile_exists, save_profile, load_profile , delete_profile
from modules.roadmap import get_ai_ml_roadmap
from modules.roadmap import get_ai_ml_roadmap, get_next_topic


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
     
    print(f"Hello, {name}.")
    print()
    print("Analyzing your future...")
    time.sleep(2)
    print()
    print("I've analyzed your daily choices...")
    time.sleep(1.5)
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
    time.sleep(2)
    
    print()
    print("-" * 60)
    print()

    future_message = f"""
    Remember...

    Your future isn't built in one day.

    It's built by repeating today's habit
    again...
    and again...
    and again.

                         — Echo
    """

    print(future_message)

    print("-" * 60)
    print()

    future_message = f"""
============================================================
                   A MESSAGE FROM YOUR FUTURE
============================================================

Hey, {name}.

Thank you.

Thank you for choosing your future,
even when nobody was watching.

Thank you for spending time every day
on {habit.lower()},
when it would've been easier to quit.

Thank you for carrying uncertainty,
self-doubt, and pressure...

...so I wouldn't have to.

Today, I'm living the life
you kept believing in.

Remember this...

You are no longer
the person standing at Level 0.

You've already become someone
who takes action.

Protect that version of yourself.

Keep moving.

I'll be waiting for you.

                          — Future You
============================================================
"""

    time.sleep(2)
    show_future_message(future_message)

def show_future_message(future_message):

    print("=" * 60)
    print("Receiving transmission from the future...")
    time.sleep(2)

    print("Decrypting message...")
    time.sleep(2)

    print("Connection established.")
    time.sleep(1)

    print(future_message)

def create_profile():
    name = get_name()
    goal = get_goal()
    habit = get_habit()
    hours = get_daily_hours()

    profile = {
        "name": name,
        "goal": goal,
        "habit": habit,
        "hours": hours,
        "completed_topics": []
    }

    save_profile(profile)

    return profile

def update_goal(profile):

    print()
    print(f"{profile['name']}...")
    print()
    print("Sometimes our destination changes.")
    print("That's not failure.")
    print()
    print("Let's update your future.")
    print()

    new_goal = input("What's your new goal?\n> ")

    profile["goal"] = new_goal

    save_profile(profile)

    print()
    print("Future updated.")
    print("I'll remember this path from now on.")
    print()

def reset_profile(profile):

    print()
    print(f"{profile['name']}...")
    print()

    print("This will erase everything")
    print("I've remembered about you.")
    print()

    answer = input("Are you sure? (Y/N): ").strip().lower()

    if answer == "y":

        delete_profile()

        print()
        print("Your past has been forgotten.")
        print("Let's begin again.")
        print()

    else:

        print()
        print("Nothing was changed.")
        print()

def show_main_menu(profile):

    print("\n" + "=" * 60)
    print("                        E C H O")
    print("=" * 60)

    print()
    print(f"Welcome back, {profile['name']}.")
    print()

    print("🎯 Goal")
    print(profile["goal"])
    print()

    print("📍 Daily Habit")
    print(f"{profile['habit']} ({profile['hours']} hrs/day)")
    print()

    completed_topics = profile["completed_topics"]
    next_topic = get_next_topic(completed_topics)

    print("📚 Today's Focus")
    print(next_topic["topic"])
    print()

    print("⏱ Estimated Time")
    print(next_topic["estimated_time"])
    print()

    print("-" * 60)

    print("1. Start Today's Session")
    print("2. Learning Path")
    print("3. Change Goal")
    print("4. Begin Again")
    print("0. Exit")

    print("-" * 60)

    return input("\nChoose an option: ")

def handle_menu_choice(choice, profile):

    if choice == "1":

        generate_future_echo(
            profile["name"],
            profile["goal"],
            profile["habit"],
            profile["hours"]
        )

    elif choice == "2":

        roadmap = get_ai_ml_roadmap()

        print("\n========== YOUR AI/ML ROADMAP ==========\n")

        for index, topic in enumerate(roadmap, start=1):
            print(f"{index}. {topic['topic']}")

        completed_topics = profile["completed_topics"]

        next_topic = get_next_topic(completed_topics)

        print("\n" + "=" * 60)
        print("                  FUTURE ANALYSIS")
        print("=" * 60)
        print()

        print(f"{profile['name']}...")
        print()

        print("I've been looking at the path you're building.")
        print()

        print("The next step I recommend is:")
        print()

        print(f"➡ {next_topic['topic']}")
        print()

        print("Why?")
        print(next_topic["reason"])
        print()

        print(next_topic["echo_message"])
        print()

        print("                         — Future You")
        print()
        ask_topic_completion(profile, next_topic)
    elif choice == "3":

        update_goal(profile)

    elif choice == "4":

        reset_profile(profile)

    elif choice == "0":

        print("\nGoodbye. See you soon!\n")
        return

    else:

        print("\n❌ Invalid choice.\n")


def ask_topic_completion(profile, next_topic):

    print()

    answer = input("Did you complete this topic? (Y/N): ").strip().lower()

    if answer == "y":

     profile["completed_topics"].append(next_topic["topic"])

     save_profile(profile)

     print("\nExcellent.")
     print("I've updated your journey.\n")

    elif answer == "n":
        print("\nThat's okay. I'll be here when you're ready.\n")

    else:
        print("\nI couldn't understand your answer.\n")

def start_simulation():
    #show_introduction()

    if profile_exists():
        profile = load_profile()

        print(f"\nWelcome back, {profile['name']}!\n")

    else:
        
       show_introduction()

       print("\nI don't think we've met before.")
       print("Let's introduce ourselves.\n")

       profile = create_profile()

    choice = show_main_menu(profile)

    handle_menu_choice(choice, profile)