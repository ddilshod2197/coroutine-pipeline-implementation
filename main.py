import asyncio

class Pipeline:
    def __init__(self):
        self.tasks = []

    async def send(self, data):
        task = asyncio.create_task(self.process(data))
        self.tasks.append(task)

    async def process(self, data):
        # Birinchi bosqich: ma'lumotni qayta ishlash
        data = await self.stage1(data)
        # Ikkinchi bosqich: ma'lumotni qayta ishlash
        data = await self.stage2(data)
        # Uchinchi bosqich: ma'lumotni qayta ishlash
        data = await self.stage3(data)
        return data

    async def stage1(self, data):
        # Birinchi bosqich: ma'lumotni qayta ishlash
        await asyncio.sleep(1)  # 1 soniya kutish
        return data.upper()

    async def stage2(self, data):
        # Ikkinchi bosqich: ma'lumotni qayta ishlash
        await asyncio.sleep(2)  # 2 soniya kutish
        return data + " - Stage 2"

    async def stage3(self, data):
        # Uchinchi bosqich: ma'lumotni qayta ishlash
        await asyncio.sleep(3)  # 3 soniya kutish
        return data + " - Stage 3"

async def main():
    pipeline = Pipeline()
    await pipeline.send("Hello, World!")
    await pipeline.send("Coroutine pipeline")

    for task in pipeline.tasks:
        await task

asyncio.run(main())
```

Kodda, `Pipeline` klassi yaratilgan bo'lib, u `send` metodini qo'llab, ma'lumotni pipeline orqali o'tkazish uchun ishlatiladi. `process` metodida, ma'lumotni qayta ishlash uchun uchta bosqich mavjud bo'lib, ular `stage1`, `stage2` va `stage3` metodlarida ifodalangan. Har bir bosqichda, ma'lumotni qayta ishlash uchun `asyncio.sleep` metodidan foydalaniladi. `main` funktsiyada, pipeline orqali ma'lumotni o'tkazish uchun `send` metodidan foydalaniladi.
