#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import numpy as np

# Duration of the simulation
tmax = 1

# Name of each species
names = ["A", "B", "C"]

# Initial concentrations of each species
c = np.array([100, 50, 0])

# Number of reactions
n = 2

# Reactants of each reaction
r = [
    np.array([1, 1, 0]),
    np.array([0, 0, 1])
]

# Products of each reaction
p = [
    np.array([0, 0, 1]),
    np.array([1, 1, 0])
]

# Speed of each reaction
k = np.array([
    2,
    1
])

def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


assert(len(r) == n and len(p) == n and len(k) == n)

print("{},\t{}".format("t", ",\t".join(names)))

t = 0
while t < tmax:
    h = np.ones(n)
    for i in range(0, n):
        for a, b in zip(r[i], c):
            h[i] *= choose(b, a)

    sumhk = sum(h*k)

    if sumhk == 0:
        break

    t += -np.log(np.random.random())/sumhk

    j = np.random.random() * sumhk
    for i in range(0, n+1):
        if j <= 0:
            break
        else:
            j -= h[i]*k[i]
    i = i-1

    c = c - r[i] + p[i]
    print("{},\t{}".format(t, ",\t".join([str(a) for a in c])))
