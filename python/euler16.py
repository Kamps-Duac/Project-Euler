def solveit():
    n = 2**1000
    summer = 0
    for i in range(len(str(n))):
        summer = summer + int(str(n)[i])
    print summer

solveit()