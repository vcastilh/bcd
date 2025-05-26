# weather_server.pyfrom typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return "It's cold right now"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")