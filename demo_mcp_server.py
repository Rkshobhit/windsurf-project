# demo_mcp_server.py
import asyncio
from mcp.server.fastmcp import FastMCP

# create MCP server
server = FastMCP("demo-mcp")

# Example tool
@server.tool()
def say_hello(name: str) -> str:
    """Returns a friendly greeting."""
    return f"Hello, {name}! This is your MCP server speaking."

# Run the server
if __name__ == "__main__":
    asyncio.run(server.run())
