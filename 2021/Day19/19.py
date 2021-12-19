import sys
sys.path.insert(0,'..')
from aoc import *
import numpy as np
import datetime
from collections import Counter
import math

DAY = datetime.date.today().day
test_exp_a = 79
test_exp_b = 3621


def compare(scannerA, scannerB):
    difsA = []
    posA = []
    difsB = []
    posB = []
    for i in range(len(scannerA)):
        for j in range(i+1, len(scannerA)):
            x1, y1, z1 = scannerA[i]
            x2, y2, z2 = scannerA[j]
            difsA.append((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2))
            posA.append([[x1, y1, z1], [x2, y2, z2]])
    for i in range(len(scannerB)):
        for j in range(i+1, len(scannerB)):
            x1, y1, z1 = scannerB[i]
            x2, y2, z2 = scannerB[j]
            difsB.append((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2))
            posB.append([[x1, y1, z1], [x2, y2, z2]])
    inBoth = 0
    for i in difsA:
        if i in difsB:
            inBoth += 1
    if inBoth < 66:
        return False, scannerA, scannerB, 0, 0, 0
    
    scannerB, dx, dy, dz = synchronize(scannerA, scannerB, difsA, difsB, posA, posB)
    return True, scannerA, scannerB, dx, dy, dz

def calculateDifs(A, B):
    d = []
    for i in range(3):
        line = []
        for j in range(3):
            line.append(A[i][j] - B[i][j])
        d.append(line)
    Adifs = []
    Bdifs = []
    for i in range(3):
        for j in range(i+1, 3):
            lA = []
            lB = []
            for k in range(3):
                lA.append(A[i][k]-A[j][k])
                lB.append(B[i][k]-B[j][k])
            Adifs.append(lA)
            Bdifs.append(lB)
    return d, Adifs, Bdifs



def synchronize(scannerA, scannerB, difsA, difsB, posA, posB):
    for i in difsA:
        if i in difsB:
            A1, A2 = posA[difsA.index(i)]
            B1, B2 = posB[difsB.index(i)]
            for p in posA:
                if A1 == p[0] and A2 != p[1]:
                    A3 = p[1]
                    d = difsA[posA.index(p)]
                    if d in difsB:
                        b0, b1 = posB[difsB.index(d)]
                        break

    if (B1 == b0):
        B3 = b1
    if (B1 == b1):
        B3 = b0
    if (B2 == b0):
        B2 = B1
        B1 = b0
        B3 = b1
    if (B2 == b1):
        B2 = B1
        B1 = b1
        B3 = b0

    A = [A1, A2, A3]
    B = [B1, B2, B3]
    d, Adifs, Bdifs = calculateDifs(A, B)
 

    if abs(Adifs[0][0]) != abs(Bdifs[0][0]):
        if abs(Adifs[0][0]) == abs(Bdifs[0][1]):
            scannerB = switch_axes(scannerB, "x", "y")
            for i in range(3):
                c = B[i][1]
                B[i][1] = B[i][0]
                B[i][0] = c
            d, Adifs, Bdifs = calculateDifs(A, B)
        else:
            scannerB = switch_axes(scannerB, "x", "z")
            for i in range(3):
                c = B[i][2]
                B[i][2] = B[i][0]
                B[i][0] = c
            d, Adifs, Bdifs = calculateDifs(A, B)
    if abs(Adifs[0][1]) != abs(Bdifs[0][1]):
        scannerB = switch_axes(scannerB, "y", "z")
        for i in range(3):
            c = B[i][2]
            B[i][2] = B[i][1]
            B[i][1] = c
        d, Adifs, Bdifs = calculateDifs(A, B)

    for i in range(3):
        if Adifs[0][i] == -Bdifs[0][i]:
            scannerB = flip(scannerB, i)
            for j in range(3):
                B[j][i] = -B[j][i]
            d, Adifs, Bdifs = calculateDifs(A, B)
    
    scannerB = move(scannerB, d[0][0], d[0][1], d[0][2])
    for j in range(3):
        for i in range(3):
            B[j][i] += d[0][i]
    return scannerB, d[0][0], d[0][1], d[0][2]



def switch_axes(scanner, ax1, ax2):
    new_scanner = []
    for i in scanner:
        x = i[0]
        y = i[1]
        z = i[2]
        if ax1 == "x" and ax2 == "y":
            x = i[1]
            y = i[0]
        if ax1 == "x" and ax2 == "z":
            x = i[2]
            z = i[0]
        if ax1 == "y" and ax2 == "z":
            y = i[2]
            z = i[1]
        new_scanner.append([x, y, z])
    return new_scanner


def flip(scanner, ax):
    new_scanner = []
    for i in scanner:
        x = i[0]
        y = i[1]
        z = i[2]
        if ax == 0:
            x = -x
        if ax == 1:
            y = -y
        if ax == 2:
            z = -z
        new_scanner.append([x, y, z])
    return new_scanner


def move(scanner, dx, dy, dz):
    new_scanner = []
    for i in scanner:
        x = i[0] + dx
        y = i[1] + dy
        z = i[2] + dz
        new_scanner.append([x, y, z])
    return new_scanner


def main_a(filename):
    data = load_block(filename)
    scanners = []
    for scanner in data:
        scanner = scanner.split("\n")
        points = []
        for i in range(1,len(scanner)):
            x, y, z = scanner[i].split(",")
            x = int(x)
            y = int(y)
            z = int(z)
            points.append([x, y, z])
        scanners.append(points)

    synced = [0]
    synchronized = [scanners[0]]
    while len(synchronized) < len(scanners):
        for i in range(len(synchronized)):
            for j in range(len(scanners)):
                if j not in synced:
                    b, sync, nosync, dx, dy, dz = compare(synchronized[i], scanners[j])
                    if b:
                        synchronized.append(nosync)
                        synced.append(j)
    
    beacons = []
    for s in synchronized:
        for point in s:
            if point not in beacons:
                beacons.append(point)

    beacons.sort()
    return len(beacons)


def main_b(filename):
    data = load_block(filename)
    scanners = []
    for scanner in data:
        scanner = scanner.split("\n")
        points = []
        for i in range(1,len(scanner)):
            x, y, z = scanner[i].split(",")
            x = int(x)
            y = int(y)
            z = int(z)
            points.append([x, y, z])
        scanners.append(points)

    synced = [0]
    synchronized = [scanners[0]]
    scan_pos = []
    while len(synchronized) < len(scanners):
        for i in range(len(synchronized)):
            for j in range(len(scanners)):
                if j not in synced:
                    b, sync, nosync, dx, dy, dz = compare(synchronized[i], scanners[j])
                    if b:
                        scan_pos.append([dx, dy, dz])
                        synchronized.append(nosync)
                        synced.append(j)
    

    maxManhattan = 0
    for i in range(len(scan_pos)):
        for j in range(i+1,len(scan_pos)):
            dis = abs(scan_pos[i][0]-scan_pos[j][0]) + abs(scan_pos[i][1]-scan_pos[j][1]) + abs(scan_pos[i][2]-scan_pos[j][2])
            if dis > maxManhattan:
                maxManhattan = dis

    return maxManhattan
    

#test_and_submit(main_a, DAY, test_exp_a, "a")
#test_and_submit(main_b, DAY, test_exp_b, "b")

print(main_a("19_test.txt"))
print(main_a("19.txt"))
print(main_b("19_test.txt"))
print(main_b("19.txt"))
