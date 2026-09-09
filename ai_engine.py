import ollama
from timing_engine import analyze_timing


def get_recommendation(activity, available_time, goal, current_time):

    best_time, duration = analyze_timing(
        available_time,
        goal
    )

    prompt = f"""
Activity: {activity}
Availability: {available_time}
Goal: {goal}
Suggested time: {best_time}
Suggested duration: {duration}

Return ONLY these 4 lines:

🎯 Best time: ...
⏰ Duration: ...
💡 Why: ...
✅ Action: ...

Keep each line short.
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.2,
            "num_predict": 80
        }
    )

    return response["message"]["content"].strip()