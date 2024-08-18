from crewai import Agent, Task, Crew, Process
import os

os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_MODEL_NAME"] = "llama3-70b-8192"
os.environ["OPENAI_API_KEY"] = "" #Please register at https://console.groq.com to get the API keys (https://console.groq.com/keys)

email = "nigerian prince sending some gold"
is_verbose = True

classifier = Agent(
    role = "email classifier",
    goal = "accuratly classify emails based on their importance. Give every email one of these ratintgs: important, casual or spam.",
    backstory = "You are an AI assistant whose only job is to classify emails accurately and honesty. Do not be afraid to give emails bad rating if they are not important. Your jon is to help the user manage their inbox.",
    verbose = True,
    allow_delegation = False
)

responder = Agent(
    role = "email classifier, write concise and simple response.",
    goal = "Based on the email .",
    backstory = "You are an AI assistant whose only job is to classify emails accurately and honesty. Do not be afraid to give emails bad rating if they are not important. Your jon is to help the user manage their inbox.",
    verbose = True,
    allow_delegation = False
)

classify_email = Task(
    description = f"clasify the email '{email}'",
    agent = classifier,
    expected_output = "One of these 3 options: 'important', 'casual' or 'spam'."
)

respond_email = Task(
    description = f"respond to email '{email}'",
    agent = responder,
    expected_output = "a very concise response to the email bnased on importance provided by the 'classifier' agent."
)

crew = Crew(
    agents = [classifier, responder],
    tasks = [classify_email, respond_email],
    verbose =  True,
    process = Process.sequential
)

output = crew.kickoff()
print(output)