#!/usr/bin/python3
def uppercase(str):
    if ord(str) in range(65, 90):
        print(f"{str}")
        return True
    else:
        return False
