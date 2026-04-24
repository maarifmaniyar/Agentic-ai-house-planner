from crewai import Task
from agents import (
    requirement_agent,
    architect_agent,
    interior_agent,
    cost_agent,
    report_agent
)

def create_tasks(user_input):

    requirement_task = Task(
        description=f"Analyze the following user input and extract structured housing requirements:\n{user_input}",
        expected_output="Structured list of requirements like rooms, size, budget, and style.",
        agent=requirement_agent
    )

    architect_task = Task(
        description="Create a detailed house layout based on the analyzed requirements.",
        expected_output="A detailed description of room placement and layout.",
        agent=architect_agent
    )

    interior_task = Task(
        description="Provide interior design suggestions for the planned house.",
        expected_output="Interior design ideas including furniture, colors, and style.",
        agent=interior_agent
    )

    cost_task = Task(
        description="Estimate the construction cost based on layout and requirements.",
        expected_output="Estimated cost range with explanation.",
        agent=cost_agent
    )

    report_task = Task(
    description="""
Combine all previous outputs into a professional house planning report.

Format the output clearly like this:

🏠 HOUSE PLAN SUMMARY

📏 Plot Size:
🛏 Rooms:
💰 Budget:
🎨 Style:

🏗 Layout Plan:
(Explain room arrangement clearly)

🎨 Interior Design Suggestions:
(Colors, furniture, style)

💰 Estimated Cost:
(Give range and explanation)

📌 Additional Suggestions:
(Any improvements or ideas)
""",
    expected_output="A clean, structured, and well-formatted house plan report.",
    agent=report_agent
)

    return [
        requirement_task,
        architect_task,
        interior_task,
        cost_task,
        report_task
    ]