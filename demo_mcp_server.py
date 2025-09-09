# demo_mcp_server.py
from mcp.server import Server
import os

# Create a simple MCP server
server = Server("DemoMCP")

@server.command("list_files")
def list_files(path: str = "."):
    """List files in a directory"""
    return os.listdir(path)

@server.command("read_file")
def read_file(filename: str):
    """Read a file’s content"""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    print("🚀 MCP Demo Server running...")
    server.run()
