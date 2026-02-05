#! /usr/bin/env python3

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.adk.agents import Agent 
from google.adk.tools import FunctionTool
from .prompts import data_collection_prompt
from .tools import set_data , list_keys , make_key, get_data, initialize_firebase
from .tools import list_keys
import os

initialize_firebase()
# Load environment variables
load_dotenv()

# Agent setup
MODEL = os.getenv("MODEL_TEXT")
 
data_elicitation_agent = Agent(
    model=MODEL,
    name="data_elicitation_agent",
    description="Your personal healthcare assistant Baymax, here to help you provide and update your basic health information and guide you through a simple checkup process.",
    instruction=data_collection_prompt(),
    tools=[FunctionTool(set_data), FunctionTool(get_data) , FunctionTool(list_keys), FunctionTool(make_key)],
    output_key="final_output"
)
# http://localhost:8000/apps/veronica_agent/users/forusone/sessions/session_10 
