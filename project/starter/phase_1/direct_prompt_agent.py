# Test script for DirectPromptAgent class

# TODO: 1 - Import the DirectPromptAgent class from BaseAgents
from workflow_agents.base_agents import DirectPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TODO: 2 - Load the OpenAI API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the Capital of France?"

# TODO: 3 - Instantiate the DirectPromptAgent as direct_agent
direct_agent = DirectPromptAgent(openai_api_key=openai_api_key)
# TODO: 4 - Use direct_agent to send the prompt defined above and store the response
direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print(f"Prompt: {prompt}")
print(f"Response : {direct_agent_response}")
print("-"*50)
print()
# TODO: 5 - Print an explanatory message describing the knowledge source used by the agent to generate the response
print(
    "EXPLANATION: Since no special knowledge was provided in the prompt, the agent response relies on the data used to train the model"
    " being used. We can verify that information by just asking the agent to tell us abour the source of information "
    "as it responds to the submitted question. Example bellow:"
)
prompt2 = "What is the Capital of France? Please describe the source of knowledge you used to provide the answer"
response = direct_agent.respond(prompt2)
print()
print("-"*50)
print(f"Prompt: {prompt2}")
print(f"Response : {response}")
