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

  

low=0
high=10000
epsilon=0.00001
T=(high+low)/2.0
for i in range (1,n+1) :
  if i%2==0 :
    a=2**i+1
  else:
    a=3**i+1
  mult=a**(n-i)
  bul += mult
while abs(guess*a-T) >=epsilon :
  if guess*a<T :
    low=guess
  else:
    high=guess
  guess=(high+low)/2.0
print(T)

low=0
high=10000
T=(hight+low)/2.0
guess=0
while abs(T-guess)> low and abs(T-guess)<high :
  if guess*bul>B :
    T=guess
  else:
    T=(high+low)/2.0  
    

