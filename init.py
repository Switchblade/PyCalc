import math
import os
import sys
import random
import time
import mathc

# Definitions

num_a = 0
num_b = 0

launchtime = random.randrange(1,5)
def barrier(length):
    bcount = 0
    while bcount < length:
        print("=", end="")
        bcount += 1

# Boot

barrier(33)
print("\n         PYCALC V0.1")
barrier(33)
print("\n")
time.sleep(int(random.randrange(0, 2)))
print("Clearing Storage Registers.")
time.sleep(int(random.randrange(0, 2)))
print("Building Registry.")
time.sleep(int(random.randrange(0, 2)))
print("Flushing DNS.")
time.sleep(int(random.randrange(0, 2)))
print("Priming Hydrogen Fuel Cell.")
time.sleep(int(random.randrange(0, 2)))
print("Filling Liquid Hydrogen Tanks.")
time.sleep(int(random.randrange(0, 3)))
print("Preparing large robot army.")
time.sleep(int(random.randrange(0, 2)))
print("Training large robot army.")
time.sleep(int(random.randrange(0, 2)))
print("Destroying all evidence of robot army.")
time.sleep(int(random.randrange(0, 2)))
print("Quickly destroying all evidence of destroying the evidence.")
time.sleep(launchtime)
print("\nStartup Complete. Took " + str(launchtime) + " Seconds.")
time.sleep(3)
# Loop
end = 0
while end < 1:
    print("Welcome to PyCalc. Type HELP to see the help screen.")
    input1 = input("Command:")

    if str(input1) == "HELP":
        mathc.helpc()
    elif str(input1) == "ADD":
        num_a = eval(input("FIRST NUMBER:"))
        num_b = eval(input("SECOND NUMBER:"))
        mathc.add(num_a, num_b)
    elif str(input1) == "SUB":
        num_a = eval(input("FIRST NUMBER:"))
        num_b = eval(input("SECOND NUMBER:"))
        mathc.sub(num_a, num_b)
    elif str(input1) == "MULT":
        num_a = eval(input("FIRST NUMBER:"))
        num_b = eval(input("SECOND NUMBER:"))
        mathc.mult(num_a, num_b)
    elif str(input1) == "DIV":
        num_a = eval(input("FIRST NUMBER:"))
        num_b = eval(input("SECOND NUMBER:"))
        mathc.div(num_a, num_b)
    elif str(input1) == "ADD":
        num_a = eval(input("FIRST NUMBER:"))
        num_b = eval(input("SECOND NUMBER:"))
        mathc.add(num_a, num_b)
    elif str(input1) == "END":
        break
