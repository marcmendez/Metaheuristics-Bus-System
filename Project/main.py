import numpy as np

print "1 - GRASP+FI"
print "2 - GRASP+BI"

heuristic = int(raw_input("Enter a number (1 or 2): "))
while heuristic not in (1, 2):
    print "Choose either 1 or 2"
    heuristic = int(raw_input("Enter a number (1 or 2): "))

import data

print "Choose an data set to run(ordered from shorter-easier to longer-harder)"
print "1 "
print "2 "
print "3 "
instance = int(raw_input("Enter a number (1, 2 or 3): "))
while instance not in (1, 2, 3):
    print "Choose either 1, 2 or 3"
    instance = int(raw_input("Enter a number (1, 2 or 3): "))
data.data = getattr(data, "data_%d" % instance)



print "Choose an aplha between 0-1 multiple of 0.1"

alpha = float(raw_input("Enter a number: "))
while alpha not in np.arange(0.0, 1.1, 0.1):
    print "Choose an aplha between 0-1 multiple of 0.1"
    alpha = float(raw_input("Enter a number: "))

import GRASP

time = []
solutions = []
t, sol = GRASP.grasp(alpha, heuristic)
time.append(t)
solutions.append(sol)

print "Total time", t
print "\n"
print "Best Solution cost", sol
