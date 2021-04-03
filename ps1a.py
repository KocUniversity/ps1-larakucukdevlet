n, B = list(map(int, input().strip().split()))
T=0
prev = 0
curr = 0
k = 0.0

for i in range(1,n+1) :
  if i %2 == 0:
    a = (2**i)+1
  else:
    a =(3**i)+1
  
  prev = a ** (n-i)
  curr += prev
k = float(B/curr)
for i in range(0,10001):
  if i > k:
    T = i
    break
print(T)
