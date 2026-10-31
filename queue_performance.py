
import multiprocessing
import time

def receiver(queue):

    data = queue.get()

    checksum = sum(data)

    queue.put(checksum)


if __name__ == "__main__":

    DATA_SIZE = 5 * 1024 * 1024  # 5 MB

    data = b"A" * DATA_SIZE

    queue = multiprocessing.Queue()

    process = multiprocessing.Process(
        target=receiver,
        args=(queue,)
    )

    start = time.perf_counter()

    process.start()

    queue.put(data)

    result = queue.get()

    process.join()

    end = time.perf_counter()

    print("MESSAGE QUEUE PERFORMANCE")
    print("--------------------------")
    print("Data Size: 5 MB")
    print("Checksum:", result)
    print("Time Taken:", round(end - start, 5), "seconds")

    queue.close()
    queue.join_thread()
