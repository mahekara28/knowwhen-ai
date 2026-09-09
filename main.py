from datetime import datetime
from ai_engine import get_recommendation
from history import save_history


print("🤖 KnowWhen-AI is ready!")
print("Type 'exit' anytime to quit.\n")


while True:

    activity = input("What do you want to do? ")

    if activity.lower() == "exit":
        print("\n👋 Thanks for using KnowWhen-AI!")
        break

    available_time = input("When are you usually available? ")
    goal = input("What is your goal? ")

    current_time = datetime.now().strftime(
        "%A, %d %B %Y, %I:%M %p"
    )

    recommendation = get_recommendation(
        activity,
        available_time,
        goal,
        current_time
    )

    print("\n" + recommendation)

    save_history(activity, recommendation)

    print("\n✅ Recommendation saved!\n")