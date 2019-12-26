sumsq = []
sqsum = []

for i in range(1, 101):
    i *= i
    sumsq.append(i)
    sumsumsq = sum(sumsq)

for j in range(1, 101):
    sqsum.append(j)
    sumsqsum = sum(sqsum)
    sumsqsum *= sumsqsum

print(sumsqsum - sumsumsq)
