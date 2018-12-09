input = """Step Y must be finished before step A can begin.
Step O must be finished before step C can begin.
Step P must be finished before step A can begin.
Step D must be finished before step N can begin.
Step T must be finished before step G can begin.
Step L must be finished before step M can begin.
Step X must be finished before step V can begin.
Step C must be finished before step R can begin.
Step G must be finished before step E can begin.
Step H must be finished before step N can begin.
Step Q must be finished before step B can begin.
Step S must be finished before step R can begin.
Step M must be finished before step F can begin.
Step N must be finished before step Z can begin.
Step E must be finished before step I can begin.
Step A must be finished before step R can begin.
Step Z must be finished before step F can begin.
Step K must be finished before step V can begin.
Step I must be finished before step J can begin.
Step R must be finished before step W can begin.
Step B must be finished before step J can begin.
Step W must be finished before step V can begin.
Step V must be finished before step F can begin.
Step U must be finished before step F can begin.
Step F must be finished before step J can begin.
Step X must be finished before step C can begin.
Step T must be finished before step Q can begin.
Step B must be finished before step F can begin.
Step Y must be finished before step L can begin.
Step P must be finished before step E can begin.
Step A must be finished before step J can begin.
Step S must be finished before step I can begin.
Step S must be finished before step A can begin.
Step K must be finished before step R can begin.
Step D must be finished before step C can begin.
Step R must be finished before step U can begin.
Step K must be finished before step U can begin.
Step D must be finished before step K can begin.
Step S must be finished before step M can begin.
Step D must be finished before step E can begin.
Step A must be finished before step K can begin.
Step G must be finished before step I can begin.
Step O must be finished before step M can begin.
Step U must be finished before step J can begin.
Step T must be finished before step S can begin.
Step C must be finished before step M can begin.
Step S must be finished before step J can begin.
Step N must be finished before step V can begin.
Step P must be finished before step N can begin.
Step D must be finished before step M can begin.
Step A must be finished before step B can begin.
Step Z must be finished before step R can begin.
Step T must be finished before step N can begin.
Step K must be finished before step J can begin.
Step N must be finished before step A can begin.
Step M must be finished before step R can begin.
Step E must be finished before step A can begin.
Step Y must be finished before step O can begin.
Step O must be finished before step B can begin.
Step O must be finished before step A can begin.
Step I must be finished before step V can begin.
Step M must be finished before step Z can begin.
Step D must be finished before step U can begin.
Step O must be finished before step S can begin.
Step Z must be finished before step W can begin.
Step M must be finished before step A can begin.
Step N must be finished before step E can begin.
Step M must be finished before step U can begin.
Step R must be finished before step J can begin.
Step W must be finished before step F can begin.
Step I must be finished before step U can begin.
Step E must be finished before step U can begin.
Step Y must be finished before step R can begin.
Step Z must be finished before step K can begin.
Step C must be finished before step F can begin.
Step B must be finished before step V can begin.
Step G must be finished before step B can begin.
Step O must be finished before step G can begin.
Step E must be finished before step Z can begin.
Step A must be finished before step V can begin.
Step Y must be finished before step Q can begin.
Step P must be finished before step D can begin.
Step X must be finished before step G can begin.
Step I must be finished before step W can begin.
Step M must be finished before step V can begin.
Step T must be finished before step M can begin.
Step G must be finished before step J can begin.
Step T must be finished before step I can begin.
Step H must be finished before step B can begin.
Step C must be finished before step E can begin.
Step Q must be finished before step V can begin.
Step H must be finished before step U can begin.
Step X must be finished before step K can begin.
Step D must be finished before step T can begin.
Step X must be finished before step W can begin.
Step P must be finished before step Z can begin.
Step C must be finished before step U can begin.
Step Y must be finished before step Z can begin.
Step L must be finished before step F can begin.
Step C must be finished before step J can begin.
Step T must be finished before step W can begin."""

result = []

import re
import string
def prepareData():
    splitInput = input.split('\n')

    dic = {}
    for condition in splitInput:
        match = re.search('\s([A-Z])\smust be finished before step ([A-Z])', condition)
        letters = match.groups()

        if letters[0] not in dic:
            dic[letters[0]] = []
        if letters[1] not in dic:
            dic[letters[1]] = []
        dic[letters[1]].append(letters[0])

    return dic

def work(inWork, result):
    for entry in inWork.copy():
        inWork[entry] -= 1
        if inWork[entry] == 0:
            result.append(entry)
            inWork.pop(entry)

    return inWork

def doOne():

    dic = prepareData()
    ready = []
    result = []

    while (len(dic) > 0):
        for key in dic.copy():
            isReady = True
            conditions = dic[key]

            for condition in conditions:
                if condition not in result:
                    isReady = False
                    break
            
            if isReady:
                ready.append(key)
                dic.pop(key)

        ready.sort()
        ready.reverse()
        result.append(ready.pop())


    return result

def doTwo():
    dic = prepareData()

    matching = {}
    count = 61
    for x in string.ascii_uppercase:
        matching[x] = count
        count += 1

    result = []
    ready = []
    inWork = {}
    time = 0

    while (True):
        time += 1
        for key in dic.copy():
            isReady = True
            conditions = dic[key]

            for condition in conditions:
                if condition not in result:
                    isReady = False
                    break
            
            if isReady:
                ready.append(key)
                dic.pop(key)

        ready.sort()
        ready.reverse()
        while len(inWork) < 5 and len(ready) > 0:
                letter = ready.pop()
                inWork[letter] = matching[letter]
            
        inWork = work(inWork, result)

        if len(inWork) == 0 and len(dic) == 0:
            return time



result = doTwo()
print(result)