
import multiprocessing
import os

def sender(connection):
    message = "Hello from Child Process!"

    print("Sender Process ID:", os.getpid())
    print("Sending Message:", message)

    connection.send(message)
    connection.close()


if __name__ == "__main__":

    # Create one-way pipe
    parent_conn, child_conn = multiprocessing.Pipe(duplex=False)

    process = multiprocessing.Process(
        target=sender,
        args=(child_conn,)
    )

    process.start()

    child_conn.close()

    # Receive message
    received_message = parent_conn.recv()

    print("\nReceiver Process ID:", os.getpid())
    print("Received Message:", received_message)

    parent_conn.close()

    process.join()

    print("\nPipe Communication Completed")
