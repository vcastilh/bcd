import asyncio
from dotenv import load_dotenv
import os

from mcp import ClientSession, StdioServerParameters
from langchain_anthropic import ChatAnthropic
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"))
stdio_server_params = StdioServerParameters(
    command="python",
    args = ["/Users/vicious/Desktop/bcd/servers/mathserver.py"],
)



async def main():
    print("Hello from bcd!")

if __name__ == "__main__":
    asyncio.run(main())
