n, B = list(map(int, input().strip().split()))
mult=0
bul=0
for i in range (1,n+1) :
  if i%2==0 :
    a=2**i+1
  else:
    a=3**i+1
  mult=a**(n-i)
  bul += mult
low=0
high=10000
T1=(high+low)/2
while abs(T1)>low and abs(T1)<high:
  if T1*bul<B :
    low=T1
    T1=(high+low)/2.0

  else:
    high=T1
    T1=(high+low)/2
    print(T1)
    
      

    
  

    