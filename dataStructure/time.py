import time

i = 0
start = time.time()
while time.time() - start < 1:
    i = i + 1

print("I counted to {} in one second ".format(i))