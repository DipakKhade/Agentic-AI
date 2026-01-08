from fastmcp import FastMCP
import os
from typing import List

mcp = FastMCP("assistance")

@mcp.tool()
async def query_db(query):
    pass


if __name__ == "__main__":
    try:
        print('starting MCP Server...')
        mcp.run()
    except KeyboardInterrupt:
        print("Exiting")
