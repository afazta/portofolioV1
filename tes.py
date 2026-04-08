import sys
import time


data = ["helo","dunia","apaya"]

for word in data:
    for lenalp in range(len(word) + 1):
        print(f"\r{word[:lenalp]}",end="",flush=True)
        time.sleep(1)
    print("")
    for lenalp in range(len(word), -1, -1):
        print(f"\r{word[:lenalp]}",end="",flush=True)
        time.sleep(1)
    print("\r", end="")
