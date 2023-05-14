"""  # =================================================================================================================
Section 2 - 2: async
------------------------------------------------------------------------------------------------------------------------
[ async ]---------------------------------------------------------------------------------------------------------------
코드가 동기적으로 동작한다 => 코드가 반드시 작성된 순서대로 실행되는 것이 아니다.
------------------------------------------------------------------------------------------------------------------------
"""  # =================================================================================================================
# import ===============================================================================================================
import time
import asyncio
# ======================================================================================================================


async def delivery(name, mealtime):
    print(f"Successfully delivered to {name}")
    await asyncio.sleep(mealtime)  # asyncio.sleep : 주어진 시간 동안 block
    print(f"{name} have eaten, spending {mealtime} sec.")
    print(f"Complete to pick up plates from {name}")
    return mealtime


async def main():
    result = await asyncio.gather(  # asyncio.gather : 동시에 태스크 실행
        delivery("A", 5),
        delivery("B", 3),
        delivery("C", 4),
    )

    print(result)

    task1 = asyncio.create_task(delivery("D", 1))
    task2 = asyncio.create_task(delivery("E", 2))
    await task2
    await task1
    # 동기 처리 -----------------
    # await delivery("A", 5)
    # await delivery("B", 3)
    # await delivery("C", 4)
    # -------------------------


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())  # asyncio.run : coroutine을 실행하고 반환
    end = time.time()
    print(end - start)
