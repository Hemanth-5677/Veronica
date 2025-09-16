#! /usr/bin/env python3

import uuid
from google import genai
from dotenv import load_dotenv

from google.generativeai.types import content_types
from google.generativeai.types.content_types import Part

from google.genai import types
from google.adk.agents import Agent 
from google.adk.orchestration import Runner
from google.adk.orchestration.session import InMemorySessionService
from google.adk.orchestration.session.session import Session
# from .prompts import get_orchestration_prompt
import os

# Load environment variables
load_dotenv()

# Creating inmemory services and internal states 
session_service = InMemorySessionService()
initial_state = {
    "username": "Brandon",
    "user_preferences": {
        "favorite_color": "Blue",
        "favorite_food": "Pizza",
        "favorite_movie": "The Matrix",
        "favorite_tv_show": "Game of Thrones"
    }
}

# Create a new session
session_id = str(uuid.uuid4())
session = session_service.create_session(
    app_name="BrandonBot",
    user_id="brandon_hancock",
    session_id=session_id,
    state=initial_state
)

# Create a runner with our agent and session service
runner = Runner(
    # root_agent=qa_agent,
    session_service=session_service
)

# Create a message to send to the agent
message = content_types.Content(
    role="user",
    parts=[Part.from_text("What is Brandon's favorite TV show?")]
)

# Run the agent with our message
response = runner.run(
    user_id="brandon_hancock",
    session_id=session_id,
    content=message
)


# Agent setup
MODEL = os.getenv("MODEL_TEXT")
 
root_agent = Agent(
    model=MODEL,
    name="advertisment_generation_agent",
    description="AI agent for generating and modifying images and html content for Advertisments ,Banners and Hodings for Nippon India Mutual Funds. Your role is to orchestrate the agents based on the user requirements and to create the required advertisments.",
    instruction="greeting agent greet user",
    # sub_agents=[image_generation_agent , html_content_agent , file_processing_agent],
    output_key="final_output"
)

# Process the response to get the final text
final_response = None
for event in response.events:
    if event.type == "content" and event.content.role == "agent":
        final_response = event.content.parts[0].text

# Print the agent's response
print("Session ID:", session_id)
print("\nAgent Response:")
print(final_response)

# Print the session state for exploration
print("\nSession State Exploration:")
print(session.state)