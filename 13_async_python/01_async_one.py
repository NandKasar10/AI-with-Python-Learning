import asyncio

async def brew_chai() : # this function is knwon as coroutine
    print("Brewing Chai .. !!")
    await asyncio.sleep(2)
    print("Chai is ready ..!!!")

asyncio.run(brew_chai())