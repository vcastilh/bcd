import asyncio
from dotenv import load_dotenv
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_anthropic import ChatAnthropic
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"))

stdio_server_params = StdioServerParameters(
    command="python",
    args = ["/Users/vicious/Desktop/bcd/servers/math_server.py"],
)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream = write) as session:
            await session.initialize()
            print("Session initialized")
            tools = await session.list_tools()
            print(tools)
          

if __name__ == "__main__":
    asyncio.run(main())
