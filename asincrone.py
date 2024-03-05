import asyncio
import json
from datetime import datetime


async def task2(names,prices):
   with  open("task2.json","w") as file:
        json.dumps(names)
        json.dumps(prices)




async def task1():

    with open("task1.json","r") as file:
        data= json.load(file)
        names =[]
        prices = []
        for i in data["courses"]:
            names.append(i["name"])
            prices.append(i["price"])

        await asyncio.run(task2(names,prices))




async def main():
    await asyncio.gather(task1())

if __name__ == "__main__":
    print(datetime.now().time())
    asyncio.run(main())
    print(datetime.now().time())
