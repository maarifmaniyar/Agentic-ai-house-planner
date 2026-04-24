from crewai import Agent

# Use Ollama model name directly
llm = "ollama/llama3"

requirement_agent = Agent(
    role="Requirement Analyzer",
    goal="Understand user requirements for house planning",
    backstory="Expert in analyzing housing needs",
    llm=llm,
    verbose=True
)

architect_agent = Agent(
    role="Architect",
    goal="Design house layout",
    backstory="Professional architect",
    llm=llm,
    verbose=True
)

interior_agent = Agent(
    role="Interior Designer",
    goal="Suggest interior design",
    backstory="Creative designer",
    llm=llm,
    verbose=True
)

cost_agent = Agent(
    role="Cost Estimator",
    goal="Estimate cost",
    backstory="Construction cost expert",
    llm=llm,
    verbose=True
)

report_agent = Agent(
    role="Report Generator",
    goal="Create final report",
    backstory="Professional report writer",
    llm=llm,
    verbose=True
)