import math
def f(x):
  return (x-3)*x**3*(x-6)**4
a=int(input())
b=int(input())
fb=[1,1,2,3,5,8,13,21,34,55]
k=2;
i=0
l=(b-a)
n=int(input())
print("The code sinnept finds the new region of the function using fibonacci search method")
for k in range(2,n+1):  
  lk=(fb[n-k+1]/fb[n+1])*l
  x1=a+lk
  x2=b-lk
  if (x1>x2 and f(x2)>f(x1)):
    a=x2
  elif (x1>x2 and f(x1)>f(x2)):
    b=x1
  elif (x2>x1 and f(x1)>f(x2)):
    a=x1
  elif (x2>x1 and f(x2)>f(x1)):
    b=x2 
  i=i+1
  print("|It::",i,"|  a:: ", (round(a,3)),"| b::",(round(b,3))," | x1:: ", x1," | x2:: ", x2," | f(x1):: ", f(x1)," | f(x2):: ", f(x2)," | new region is ::[ ",(round(a,2))," ,", (round(b,2)),"]  |  n==k ::",bool(n==k))
print("new region is [ ",(round(a,2))," ,", (round(b,2)),"]")
