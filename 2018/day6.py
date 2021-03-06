input = """118, 274
102, 101
216, 203
208, 251
309, 68
330, 93
91, 179
298, 278
201, 99
280, 272
141, 312
324, 290
41, 65
305, 311
198, 68
231, 237
164, 224
103, 189
216, 207
164, 290
151, 91
166, 250
129, 149
47, 231
249, 100
262, 175
299, 237
62, 288
228, 219
224, 76
310, 173
80, 46
312, 65
183, 158
272, 249
57, 141
331, 191
163, 359
271, 210
142, 137
349, 123
55, 268
160, 82
180, 70
231, 243
133, 353
246, 315
164, 206
229, 97
268, 94"""

import string
import re

def nearest(coordinates, dic):
    xpoint,ypoint = coordinates
    nearestDistance = 10000
    result = 0
    for entry in dic:
        x,y = dic[entry]
        distance = abs(x - xpoint) + abs(y - ypoint) 
        if distance < nearestDistance:
            nearestDistance = distance
            result = entry
        elif distance == nearestDistance:
            result = 0
    return result

def nearEnough(coordinates, dic):
    xpoint,ypoint = coordinates
    maxDistance = 10000
    distanceSum = 0
    for entry in dic:
        x,y = dic[entry]
        distanceSum += abs(x - xpoint) + abs(y - ypoint)
        if distanceSum >= maxDistance:
            return False
        
    return True
    

def doOne():
    splitInput = input.split('\n')
    dic ={}
    count = 1
    for coordinates in splitInput:
        dic[count] = [int(x) for x in re.findall('[0-9]+', coordinates)]
        count += 1

    width, height = 350, 370
    matrix = [[0 for x in range(width)] for y in range(height)]

    resultdic = {}

    for x in range(width):
        for y in range(height):
            near = nearest([x,y], dic)
            matrix[y][x] = near
            if near not in resultdic:
                resultdic[near] = 0
            
            if x == width - 1 or y == height - 1 or x == 0 or y == 0:
                resultdic[near] = -1

            if resultdic[near] != -1:
                resultdic[near] += 1   
    
    
    return resultdic

def doTwo():
    splitInput = input.split('\n')
    dic ={}
    count = 1
    for coordinates in splitInput:
        dic[count] = [int(x) for x in re.findall('[0-9]+', coordinates)]
        count += 1

    width, height = 500, 500
    matrix = [[0 for x in range(width)] for y in range(height)]

    result = 0

    for x in range(width):
        for y in range(height):
            nearenough = nearEnough([x,y], dic)
            if nearenough:
              result += 1

    return result  

print(max(doOne().values()))

print(doTwo())