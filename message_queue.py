
import multiprocessing
import os

def producer(queue):

    print("Producer Process ID:", os.getpid())

    messages = [
        "Hello",
        "Welcome to IPC",
        "Message Queue Practical",
        "Communication Completed"
    ]

    for message in messages:
        print("Sending:", message)
        queue.put(message)

    # Signal that no more messages are coming
    queue.put(None)


def consumer(queue):

    print("Consumer Process ID:", os.getpid())

    while True:
        message = queue.get()

        if message is None:
            break

        print("Received:", message)


if __name__ == "__main__":

    queue = multiprocessing.Queue()

    producer_process = multiprocessing.Process(
        target=producer,
        args=(queue,)
    )

    consumer_process = multiprocessing.Process(
        target=consumer,
        args=(queue,)
    )

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    queue.close()
    queue.join_thread()

    print("\nMessage Queue Communication Completed")
