
import multiprocessing
import time

def receiver(connection):

    data = connection.recv_bytes()

    checksum = sum(data)

    connection.send(checksum)

    connection.close()


if __name__ == "__main__":

    DATA_SIZE = 5 * 1024 * 1024  # 5 MB

    data = b"A" * DATA_SIZE

    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(
        target=receiver,
        args=(child_conn,)
    )

    start = time.perf_counter()

    process.start()
    child_conn.close()

    parent_conn.send_bytes(data)

    result = parent_conn.recv()

    process.join()

    end = time.perf_counter()

    print("PIPE PERFORMANCE ANALYSIS")
    print("--------------------------")
    print("Data Size: 5 MB")
    print("Checksum:", result)
    print("Time Taken:", round(end - start, 5), "seconds")

    parent_conn.close()
