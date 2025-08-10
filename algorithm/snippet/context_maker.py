import logging
from contextlib import contextmanager
import time

@contextmanager
def timer(tag: str):
    start = time.perf_counter()
    yield
    # logging.info("{tag}: {time.perf_counter() - start:.4f}s")
    print(f'{tag} took {time.perf_counter() - start:.4f} seconds')

with timer("heavy job"):
    sum(i * i for i in range(10_000_000))

