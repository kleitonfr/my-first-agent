# 1 - pip install -qU langchain "langchain[anthropic]";
# 2 - pip install python-dotenv;
# 3 - we store sensitive information in a .env file, which is not committed to github

import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# 4 - Initialize the Model (the "brain") 
# this is the LLM that will:
# - Understand the question
# - Decide which tool to use
# - Generate the final answer
from langchain.chat_models import init_chat_model


# "claude-sonnet-4-6"
model = init_chat_model("claude-sonnet-4-6")


# 5 - Define the tools (the "Hands")
# Tools allow the agent to do things instead of just responding.
# Each tool must have: a clear name, a description, and type hints.
from langchain_core.tools import tool
import math

# this is a decorator that registers the function as a tool, so agent can discover it
@tool
def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    the agent will use this when it detects an addition problem
    """

    return a + b

@tool
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    the agent will use this when it detects a multiplication problem
    """

    return a * b

@tool
def divide(a: float, b: float) -> str:
    """
    Divide the first number by the second number. includes error handling for division by zero.
    the agent will use this when it detects a division problem
    """

    if b == 0:
        return "Error: Division by zero is not allowed."
    return str(a / b)  #convert to string to avoid float representation issues


@tool
def square_root(a: float) -> str:
    """
    Calculate the square root of a number. includes error handling for negative numbers.
    the agent will use this when it detects a square root problem
    """

    if a < 0:
        return "Error: Square root of negative number is not defined."
    return str(math.sqrt(a))  #convert to string to avoid float representation issues

# 6 - Combining all tools into a list
tools = [add, multiply, divide, square_root]

# 7 - just cause i wanna see what the agent has access to i will print available tools
print("Available tools:")
for tool in tools:
    print(f" - {tool.name}: {tool.description}")

print()

# 8 - Create the agent (the "loop")
from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools=tools
)

# 9 running the agent

def run_agent(question: str):
    """
    This function takes a question as input, runs the agent, and returns the answer.
    """

    print(f"\n User: {question}")
    print("-" * 60)

     

    print("🔎 Clean Agent Execution Trace")
    print("-" * 60)
    
    step = 1
    
    for msg in result["messages"]:
        
        # original message from the user
        if msg.type == "human":
            print(f"Step {step}: User asked:")
            print(f" {msg.content}")
            step += 1
            
        # ia message from the agent, agent decides to use a tool
        elif msg.type == "ai" and getattr(msg, "tool_calls", None):
            for tool_call in msg.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]
                
                print(f"{step}. Agent decision:")
                print(f" i need to use the toll: {tool_name}")
                print(f" with the following arguments: {tool_args}")
                step += 1
                
        # Tool response from the agent, after using a tool, retuned by the tool
        elif msg.type == "tool":
            print(f"{step}. Tool response:")
            print(f" {msg.content}")
            step += 1
            
        
        # final answer from the agent
        elif msg.type == "ai" and msg.content:
            print(f"{step}. Final answer:")
            print(f" {msg.content}")
            step += 1
            
    print("=" * 60)
    
    
    # -------------------------------------
    # TEST CASES
    # -------------------------------------
    
if __name__ == "__main__":
    run_agent("Quanto é 15 vezes 8?")