import argparse
import os

from dotenv import load_dotenv
from gentopia import chat
from gentopia.assembler.agent_assembler import AgentAssembler
from gentopia.output import enable_log


def main():
    enable_log(log_level='info')
    load_dotenv("/mnt/c/Users/default.LAPTOP-7062P5CO/Desktop/nlp2/CS678_hw2/nlp hw/GentPool/.env")  # Retrieve the OpenAI API key from the environment
    api_key = os.getenv('OPENAI_API_KEY')

    # Print the API key to verify
    # print(f"Loaded API Key: {api_key}")

    if not api_key:
        raise ValueError("API key not found. Make sure it is set correctly in the .env file.")

    parser = argparse.ArgumentParser(description='Assemble an agent with given name.')
    parser.add_argument('name', type=str, help='Name of the agent to assemble.')
    parser.add_argument('--print_agent', action='store_true', help='Print the agent if specified.')

    args = parser.parse_args()
    agent_name = args.name
    print_agent = args.print_agent

    # Check if agent_name is under directory ./gentpool/pool/
    print(f"Checking for agent at: ./gentpool/pool/{agent_name}")  # Debugging statement
    if not os.path.exists(f'./gentpool/pool/{agent_name}'):
        raise ValueError(f'Agent {agent_name} does not exist. Check ./gentpool/pool/ for available agents.')

    agent_config_path = f'./gentpool/pool/{agent_name}/agent.yaml'

    assembler = AgentAssembler(file=agent_config_path)

    # # assembler.manager = LocalLLMManager()
    # print(f">>> Assembling agent {agent_name}...")
    agent = assembler.get_agent()

    if agent.name != agent_name:
        raise ValueError(f"Agent name mismatch. Expected {agent_name}, got {agent.name}.")

    chat(agent, verbose=print_agent)


if __name__ == '__main__':
    main()
