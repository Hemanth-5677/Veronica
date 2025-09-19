#! /usr/bin/env python3

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.adk.agents import Agent 
# from .prompts import root_agent_prompt
import os

# Load environment variables
load_dotenv()

# Agent setup
MODEL = os.getenv("MODEL_TEXT")
 
generalized_rag_agent = Agent(
    model=MODEL,
    name="generalized_rag_agent",
    description="A senior hospital receptionist agent that greets patients, engages in warm conversations, and routes queries to the correct specialized sub-agent.",
    instruction="do a normal greeting",
    # sub_agents=[image_generation_agent , html_content_agent , file_processing_agent],
    output_key="final_output"
)
# http://localhost:8000/apps/veronica_agent/users/forusone/sessions/session_10 
