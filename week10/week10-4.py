a = [9, 8, 7, 1, 2, 3, 6, 5, 4, 0]
N = len(a)
print(a)
for i in range(N-1):
  if a[i] > a[i+1]:
    a[i], a[i+1] = a[i+1], a[i]
print(a)