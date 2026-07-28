def get_ai_ml_roadmap():
    return [

        {
         "topic": "Python Basics",
        "reason": "Builds the foundation for everything else.",
        "echo_message": "Every expert starts here. Never underestimate how far strong fundamentals can take you."
        },

        {
         "topic": "Variables & Data Types",
         "reason": "Required to store and manipulate information.",
        "echo_message": "This is where you learn that every intelligent system begins by understanding data."
        },

        {
         "topic": "Conditionals",
         "reason": "Teaches decision making in programs.",
         "echo_message": "This was the first time I stopped writing instructions and started teaching computers how to make decisions."
        },
        {
         "topic": "Loops",
         "reason": "Allows automation through repetition.",
         "echo_message": "The day you understood loops, you stopped solving one problem at a time and started solving thousands."
        },
        {
        "topic": "Functions",
        "reason": "Essential for writing clean and reusable code.",
        "echo_message": "This was the moment your code stopped growing randomly and started becoming organized."
        },

    ]

def get_next_topic(completed_topics):
    roadmap = get_ai_ml_roadmap()

    for topic in roadmap:

        if topic["topic"] not in completed_topics:

            return topic

    return None