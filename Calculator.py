x=int(input("Enter the no. of entries"))
num=[]
for i in range(x):
  n=float(input("Enter the number"))
  num.append(n)
o=input("Add/Sub/Multi/Div")
if o.lower()=="add":
  result=sum(num)
elif o.lower()=="sub":
  result=num[0]
  for j in num[1:]:
    result-=j
elif o.lower()=='multi':
  result=1
  for j in num:
    result*=j
elif o.lower()=='div':
  result=num[0]
  for j in num[1:]:
    result/=j
print("The answer is", result)
  
