# %% CLASSES AND INHERITANCE

class Book:
    """_summary_
    """
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages


book1 = Book("LOTR", "Tolkein", 500)
book2 = Book("G G Marquez", "Cien Anos de Soledad", 200)


print(book1.author)
print(book2.pages)


class HorrorBook(Book):
    """_summary_
    """
    pass

fantasy_book_1 = HorrorBook("Frankenstein", "Mary Shelley", 200)

print(fantasy_book_1.author)

# %% Asyncio / Asynchronous coding
import asyncio

async def main():
    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(1)
    print("B")
    return_value = await task
    print(f"Return value is {return_value}")

async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10

asyncio.run(main())


# %% multiprocessing
import multiprocessing
import time

def do_somthing():
    print("Sleeping one second.")
    time.sleep(1)
    print("Finished sleeping.")

if __name__ == '__main__':
    start = time.time()


    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_somthing)
        p.start()
        processes.append(p)
    
    for process in processes:
        process.join()

    finish = time.time()

    print(f"Finished in {round(finish-start, 2)} seconds.")

# %% Multithreading
import threading
import time

def do_somthing():
    print("Sleeping one second.")
    time.sleep(1)
    print("Finished sleeping.")

if __name__ == '__main__':
    start = time.time()

    threads = []

    for _ in range(10):
        t = threading.Thread(target=do_somthing)
        t.start()
        threads.append(t)
    
    for process in threads:
        process.join()

    finish = time.time()

    print(f"Finished in {round(finish-start, 2)} seconds.")
