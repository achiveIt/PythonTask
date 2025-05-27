import os

def findFile(path, fileName):
    files = os.listdir(path)
    for file in files:
        if file == fileName:
            return True
    return False

path = input("provide path: ")
fileName = input("File name: ")

if findFile(path, fileName):
    print("File is present")
else:
    print("File is not present")