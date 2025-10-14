import asyncio

async def brew (chai) :
    print(f"Brewing {chai} chai ...!!")
    await asyncio.sleep(2)
    print(f"{chai} is ready ..!!!")

async def main() :
    await asyncio.gather()