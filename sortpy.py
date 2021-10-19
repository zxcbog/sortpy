c = list(str(input()))
def sort(c):
    running = True
    pr = False
    g = [1]
    e = 0
    i = 0
    while running and pr == False:
        if ord(c[i+1]) < ord(c[i]):
            c[i], c[i+1] = c[i + 1], c[i]
        i += 1
        if i == len(c) - 1:
            for j in range(len(c) - 1):
                if c[j] > c[j + 1]:
                    i = 0
                    pr = False
                    break
                else:
                    pr = True
    for j in range(len(c) - 1):
        if (c[j] == c[j + 1]):
            g[e] += 1
        else:
            g += [1]
            e += 1
    return c, g, e
c1, g, e = sort(c)
print(sort(c)[0])
i = 0
for es in range(e + 1):
    i += g[es]
    print((c[i - 1]),':', g[es])
