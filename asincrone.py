import asyncio
import json


async def task2(names,prices):
   with  open("task2.json","r") as file:
       data = json.load(file)
       for i in range(len(names)):
           dict = {"name":names[i],"price":prices[i]}
           data["course"].append(dict)
   with open("task2.json","w") as file:
       json.dump(data,file,indent=4)
   print(data)




async def task1():

    with open("task1.json","r") as file:
        data= json.load(file)
        names =[]
        prices = []
        for i in data["course"]:
            names.append(i["name"])
            prices.append(i["price"])
        print(names,prices,"to task2")
        return asyncio.gather(task2(names,prices))




async def main():
    await asyncio.gather(task1())

if __name__ == "__main__":
    asyncio.run(main())
