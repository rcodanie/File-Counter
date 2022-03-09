from ast import While
from asyncore import loop
from unittest.util import _count_diff_hashable


name = input("Please enter the full filename: ")
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

def mostCommon():
    mCount = None
    mWord = []
    for word, count in counts.items():
        if mCount is None or count >= mCount:
            mWord.append(word)
            mCount = count
    print(mWord, mCount)

def leastCommon():
    lWord = []
    for word, count in counts.items():
        if count == 1:
            lWord.append(word)
    print(lWord, 1)

def printMenu():
    print("What would you like to know about the file?" + 
    "\n A) All words and their count" +
    "\n B) The most common word(s)" +
    "\n C) The least common word(s)" +
    "\n D) Nothing. Quit the program")

while True:
    printMenu()
    mode = input("Please select an option: ")
    if mode == "A":
            print(word, counts)  

    elif mode == "B":
        mostCommon()

    elif mode == "C":
        leastCommon()

    elif mode == "D":
        break

    else :
        print("Invald selection please try again")  