# mcp_instance.py
from mcp.server.fastmcp import FastMCP
import os

PORT = int(os.getenv("PORT", 1729))

# Create a single shared instance of FastMCP
mcp = FastMCP("RJCGG",host="0.0.0.0", port=PORT, debug=True)
