import random as rnd
import string
#import httpx as hp

def generate_username(length: int) -> str:
    arr = []
    letters = string.ascii_letters
    for i in range(length):
        random_username = rnd.choice(letters)
        arr.append(random_username)

    for g in arr:
        print(g, end="")


print(generate_username(5))