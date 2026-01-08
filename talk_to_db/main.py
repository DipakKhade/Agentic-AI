
from fastmcp import FastMCP
import mysql.connector
from typing import Any, List, Tuple, Optional
import os

mcp = FastMCP("assistance")

DB_CONFIG = {
    "user": os.getenv("DB_USER", "testuser"),
    "password": os.getenv("DB_PASSWORD", "testpass"),
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "database": os.getenv("DB_NAME", "testdb"),
}


@mcp.tool()
async def query_db(query: str, params: Optional[Tuple[Any, ...]] = None) -> List[dict]:
    """
    Execute a SQL query on MySQL database.

    Args:
        query: SQL query string (use %s placeholders)
        params: tuple of parameters

    Returns:
        List of rows as dictionaries (for SELECT queries)
        Empty list for INSERT/UPDATE/DELETE
    """
    cnx = None
    cursor = None

    try:
        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor(dictionary=True)

        cursor.execute(query, params or ())

        # If it's a SELECT query, fetch results
        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            return rows
        else:
            # For INSERT/UPDATE/DELETE
            cnx.commit()
            return []

    except mysql.connector.Error as err:
        return [{"error": str(err)}]

    finally:
        if cursor:
            cursor.close()
        if cnx and cnx.is_connected():
            cnx.close()


if __name__ == "__main__":
    try:
        print("🚀 Starting MCP Server...")
        mcp.run()
    except KeyboardInterrupt:
        print("🛑 MCP Server stopped.")
("Exiting")
