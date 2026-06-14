from fastmcp import Client 
import asyncio

async def main():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        result = await client.call_tool(
            "add",
            {"a" : 3, "b" : 7}
        )

        result2 = await client.call_tool(
            "substract",
            {"a" : 8, "b" : 7}
        )

        resource = await client.read_resource("drive://my-resource")
        prompt = await client.get_prompt("summarize_prompt")

        print(result)
        print(result2)
        print(resource)
        print(prompt)

asyncio.run(main())

