from datetime import datetime


def save_history(activity, recommendation):
    with open("history.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write(f"\n[{timestamp}] {activity}\n")
        file.write(recommendation)
        file.write("\n" + "-" * 50 + "\n")