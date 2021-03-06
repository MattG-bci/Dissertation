import random
import torch
import math
import time
from datetime import timedelta
from tqdm import tqdm

@torch.jit.script
def foo():
    x = torch.ones((1024*12, 1024*12), dtype=torch.float32)
    y = torch.ones((1024*12, 1024*12), dtype=torch.float32)
    z = x + y
    return z

if __name__ == "__main__":
    start = time.time()
    z0 = None
    for _ in tqdm(range(20000)):
        zz = foo()
        if z0 is None:
            z0 = zz
        else:
            z0 += zz

    delta = time.time() - start
    elapsed = str(timedelta(seconds=delta))
    print("Elpased time: {}".format(elapsed))