import os
import time

input_path = "/input/nanogpt-dataset/shakespeare_char/train.bin"

for i in range(10):
    exists = os.path.exists(input_path)
    print("Found: ", exists)
    time.sleep(1)
