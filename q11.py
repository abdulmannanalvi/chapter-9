import os

with open("old.txt") as f:
    os.rename("old.txt","new.txt")