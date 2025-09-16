#! /usr/bin/env python3

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.adk.agents import Agent 
# from .prompts import get_orchestration_prompt
import os

# Load environment variables
load_dotenv()

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
# http://localhost:8000/apps/veronica_agent/users/forusone/sessions/session_10 
