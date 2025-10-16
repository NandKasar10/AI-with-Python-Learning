import asyncio
import time

async def brew (chai) :
    print(f"Brewing {chai} ...!!")
    await asyncio.sleep(3) # non-blocking code
    # time.sleep(3) #blocking code
    print(f"{chai} is ready ..!!!")

async def main() :
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Green Chai"),
        brew("Ginger Chai"),
    )

asyncio.run(main())

