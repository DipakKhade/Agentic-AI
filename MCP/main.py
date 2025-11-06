from fastmcp import FastMCP

mcp = FastMCP("server_name")

@mcp.tool
def get_my_name() -> str:
    return f"Dipak Khade"

if __name__ == "__main__":
    mcp.run()