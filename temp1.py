import asyncio

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)  # Simulate an I/O operation
    print("Done fetching")
    return {'data': 123}

async def main():
    print("Before fetching")
    result = await fetch_data()
    print("Result:", result)
    print("After fetching")

asyncio.run(main())
print("this should execute the first")
