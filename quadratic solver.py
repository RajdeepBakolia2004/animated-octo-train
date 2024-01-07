import math
while True:
    a=input('enter an quadratic equation of the form ax**2+bx+c=')
    if 'x**2' not in a or 'x' not in a or '+'not in a:
        print('enter again')
        continue
    c=a.split('+')
    x='0'
    if 'x**2' in c[0]:
        for i in range(len(c[0])):
            if c[0][i].isdigit():
                x+=c[0][i]
            if c[0][i]=='x':
                break
    if 'x**2' in c[1]:
        for i in range(len(c[1])):
            if c[1][i].isdigit():
                x+=c[1][i]
            if c[1][i]=='x':
                break
    if 'x**2' in c[2]:
         for i in range(len(c[2])):
            if c[2][i].isdigit():
                x+=c[2][i]
                if c[2][i]=='x':
                    break
    x=int(x)
    if 'x**2' in a and 'x' in a and '+'in a and x!=0 :
        print('your equation is=',a)
        break
    else:
        print('enter again')
x=y=z='0'
c=a.split('+')
print(c)
if 'x**2' in c[0]:
    for i in range(len(c[0])):
        if c[0][i].isdigit():
            x+=c[0][i]
        if c[0][i]=='x':
            break
if 'x**2' in c[1]:
    for i in range(len(c[1])):
        if c[1][i].isdigit():
            x+=c[1][i]
        if c[1][i]=='x':
            break
if 'x**2' in c[2]:
    for i in range(len(c[2])):
        if c[2][i].isdigit():
            x+=c[2][i]
        if c[2][i]=='x':
            break
if 'x' in c[0] and '**2' not in c[0]:
    for i in range(len(c[0])):
        if c[0][i].isdigit():
            y+=c[0][i]
        if c[0][i]=='x':
            break
if 'x' in c[1] and '**2' not in c[1]:
    for i in range(len(c[1])):
        if c[1][i].isdigit():
            y+=c[1][i]
        if c[1][i]=='x':
            break
if 'x' in c[2] and '**2' not in c[2]:
    for i in range(len(c[2])):
        if c[2][i].isdigit():
            y+=c[2][i]
        if c[2][i]=='x':
            break        
if 'x**2' not in c[0] and 'x' not in c[0]:
    for i in range(len(c[0])):
        if c[0][i].isdigit():
            z+=c[0][i]
if 'x**2' not in c[1] and 'x' not in c[1]:
    for i in range(len(c[1])):
        if c[1][i].isdigit():
            z+=c[1][i]
if 'x**2' not in c[2] and 'x' not in c[2]:
    for i in range(len(c[2])):
        if c[2][i].isdigit():
            z+=c[2][i]
x=a=float(x)
y=b=float(y)
z=c=float(z)
print(x,y,z)
if x==0:
    x=1
    d=(y)**2-4*x*z
    if d==0:
        print('it have equal real roots')
        r=-y/(2*a)
        print('root is',r)
    if d>0:
        print('it have distinct real roots')
        r1=(-b+math.sqrt(d))/(2*a)
        r2=(-b-math.sqrt(d))/(2*a)
        print('roots are',r1,r2)
    if d<0:
        print('it have two imaginary roots')
        r1=complex(-b/2*a,math.sqrt(-d)/(2*a))
        r2=complex(-b/2*a,-math.sqrt(-d)/(2*a))
        print('roots are',r1,r2)
else:
    d=(y)**2-4*x*z
    if d==0:
        print('it have equal real roots')
        r=-b/(2*a)
        print('root is',r)
    if d>0:
        print('it have distinct real roots')
        r1=(-b+math.sqrt(d))/(2*a)
        r2=(-b-math.sqrt(d))/(2*a)
        print('roots are',r1,r2)
    if d<0:
        print('it have two imaginary roots')
        r1=complex(-b/2*a,math.sqrt(-d)/(2*a))
        r2=complex(-b/2*a,-math.sqrt(-d)/(2*a))
        print('roots are',r1,r2)
