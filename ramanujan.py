count=0
def number():
    num=input('Enter a natural number=')
    if num.isdigit():
        num=int(num)
        return num
    else:
        print('enter a natural number.')
        num=number()
        return num


num=number()
lis=[]
for i in range(1,num+1):
    lis=lis+[i**3]

main=[]
for i in lis:
    for j in lis:
        comb=[i,j]
        comb.sort()
        if comb not in main:
            main=main+[comb]


n=len(main)
number=[]
for i in range(n):
    a=main[i]
    for j in range(i,n):
        b=main[j]
        count+=1
        if sum(a)==sum(b) and a!=b:
            number=number+[sum(a)]
            print('='*30,'\n')
            print(sum(a),'is a ramanujan\'s number and it can be broken into:')
            print(a[0],'+',a[1])
            print(b[0],'+',b[1])
            print('='*30,'\n')
            
number.sort()
print(len(number))
print(number)
            

    



