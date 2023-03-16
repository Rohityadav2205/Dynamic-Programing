def findmin(s1, s2):
    if s1 < s2:
        return s1
    else:
        return s2


# print(findmin(7,59))

e1 = 3
e2 = 5
x1 = 3
x2 = 2
s1 = [7, 9, 3, 4, 8, 4]
s2 = [8, 5, 6, 4, 5, 7]
t1 = [2, 3, 1, 3, 4]
t2 = [2, 1, 2, 2, 1]
r1 = [e1, e1 + s1[0]]
r2 = [e2, e2 + s2[0]]
print(r1, r2)
n = 2
nextr1 = findmin(r1[-1] + s1[n - 1], r2[-1] + t2[n - 2] + s1[n - 1])
nextr2 = findmin(r2[-1] + s2[n - 1], r1[-1] + t1[n - 2] + s2[n - 1])
r1.append(nextr1)
r2.append(nextr2)
print(r1, r2)
n = 3
nextr1 = findmin(r1[-1] + s1[n - 1], r2[-1] + t2[n - 2] + s1[n - 1])
nextr2 = findmin(r2[-1] + s2[n - 1], r1[-1] + t1[n - 2] + s2[n - 1])
r1.append(nextr1)
r2.append(nextr2)
print(r1, r2)
n = 4
nextr1 = findmin(r1[-1] + s1[n - 1], r2[-1] + t2[n - 2] + s1[n - 1])
nextr2 = findmin(r2[-1] + s2[n - 1], r1[-1] + t1[n - 2] + s2[n - 1])
r1.append(nextr1)
r2.append(nextr2)
print(r1, r2)
