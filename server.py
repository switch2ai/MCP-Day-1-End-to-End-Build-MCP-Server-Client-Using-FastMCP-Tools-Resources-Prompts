from fastmcp import FastMCP

mcp = FastMCP()


@mcp.tool()
def add(a : int, b : int) -> int:
    """This tool will add two numbers"""
    return a + b

@mcp.tool()
def substract(a : int, b : int) -> int:
    """This tool will substract two numbers"""
    return a - b

@mcp.resource("drive://my-resource")
def file_info() -> str:
    return "This is resource"

@mcp.prompt()
def summarize_prompt() -> str: 
    return "Summarize given document...."


mcp.run(
    transport="http",
    host="127.0.0.1",
    port=8000

)