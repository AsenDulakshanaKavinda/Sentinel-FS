
from mcp.server import FastMCP

# initialize FastMCP server
mcp = FastMCP("sentinel_fs")

@mcp.tool()
def add(a: int, b: int) -> int:
    """ add two numbers together """
    return a + b


@mcp.tool()
def search_code():
    pass


@mcp.tool()
def index_dir():
    pass


@mcp.tool()
def file_context():
    pass


if __name__ == "__main__":
    mcp.run(transport="stdio")


