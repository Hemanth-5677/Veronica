#! /usr/bin/env python3

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.adk.agents import Agent 
from .prompts import root_agent_prompt
from .sub_agents.calendar_mangement_agent.agent import calendar_management_agent
from .sub_agents.data_elicitation_agent.agent import data_elicitation_agent
from .sub_agents.generalized_rag_agent.agent import generalized_rag_agent
import os

# Load environment variables
load_dotenv()

# Agent setup
MODEL = os.getenv("MODEL_TEXT")
 
root_agent = Agent(
    model=MODEL,
    name="advertisment_generation_agent",
    description="A senior hospital receptionist agent that greets patients, engages in warm conversations with user in their prefferd languages, and routes queries to the correct specialized sub-agent.",
    instruction=root_agent_prompt(),
    sub_agents=[generalized_rag_agent , calendar_management_agent , data_elicitation_agent],
    output_key="final_output"
)
# http://localhost:8000/apps/veronica_agent/users/forusone/sessions/session_10 
