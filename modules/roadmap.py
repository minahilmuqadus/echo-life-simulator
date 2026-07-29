def get_ai_ml_roadmap():
    return [

        {
            "topic": "Python Basics",
            "reason": "Builds the foundation for everything else.",
            "estimated_time": "2-3 Days",
            "difficulty": "Easy",
            "echo_message": "Every expert starts here. Never underestimate how far strong fundamentals can take you."
        },

        {
            "topic": "Variables & Data Types",
            "reason": "Required to store and manipulate information.",
            "estimated_time": "2 Days",
            "difficulty": "Easy",
            "echo_message": "This is where you learn that every intelligent system begins by understanding data."
        },

        {
            "topic": "Conditionals",
            "reason": "Teaches decision making in programs.",
            "estimated_time": "2 Days",
            "difficulty": "Easy",
            "echo_message": "This was the first time I stopped writing instructions and started teaching computers how to make decisions."
        },

        {
            "topic": "Loops",
            "reason": "Allows automation through repetition.",
            "estimated_time": "3 Days",
            "difficulty": "Medium",
            "echo_message": "The day you understood loops, you stopped solving one problem at a time and started solving thousands."
        },

        {
            "topic": "Functions",
            "reason": "Essential for writing clean and reusable code.",
            "estimated_time": "3-4 Days",
            "difficulty": "Medium",
            "echo_message": "This was the moment your code stopped growing randomly and started becoming organized."
        }

    ]
def get_next_topic(completed_topics):

    roadmap = get_ai_ml_roadmap()

    for topic in roadmap:

        if topic["topic"] not in completed_topics:
            return topic

    return {
        "topic": "Congratulations!",
        "reason": "You've completed the entire roadmap.",
        "estimated_time": "-",
        "difficulty": "-",
        "echo_message": "Your learning journey never truly ends. Keep building."
    }