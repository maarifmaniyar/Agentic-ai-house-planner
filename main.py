from dotenv import load_dotenv
import os

load_dotenv()

print("API KEY LOADED:", os.getenv("OPENAI_API_KEY"))

from crewai import Crew
from tasks import create_tasks

def run_house_planner():
    print("🏠 AI House Planner Started...\n")

    user_input = input("Enter your house requirements:\n")

    tasks = create_tasks(user_input)

    crew = Crew(
        agents=[task.agent for task in tasks],
        tasks=tasks,
        verbose=False 
    )

    result = crew.kickoff()

    print("\n\n🏠 FINAL HOUSE PLAN:\n")
    print(result)


if __name__ == "__main__":
    run_house_planner()