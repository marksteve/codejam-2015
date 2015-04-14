T = raw_input()
for t in range(int(T)):
    _, S = raw_input().split(' ')
    total = 0
    req = 0
    for k, s in enumerate(S):
        s = int(s)
        r = k - total if s > 0 else 0
        if r > req:
            req = r
        total += s
    print "Case #{}: {}".format(t + 1, req)

