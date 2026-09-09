def analyze_timing(available_time, goal):

    available = available_time.lower()
    goal = goal.lower()

    if "morning" in available:
        best_time = "Morning"
    elif "afternoon" in available:
        best_time = "Afternoon"
    elif "evening" in available:
        best_time = "Evening"
    elif "night" in available:
        best_time = "Night"
    else:
        best_time = "Your available time window"

    if any(word in goal for word in ["learn", "study", "practice", "build"]):
        duration = "60–90 minutes"
    elif any(word in goal for word in ["quick", "review", "revise"]):
        duration = "30–45 minutes"
    else:
        duration = "45–60 minutes"

    return best_time, duration