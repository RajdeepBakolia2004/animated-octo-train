from time import *
print('''This program will record how fast your typing speed is.
If you are ready press enter, after that wait until your screen prints go and the start writing.
After you are finished press enter to see how much time you took''')
input('Press enter when you are ready')
sleep(0.5)
print('ready',end=' ')
sleep(1)
print('steady',end=' ')
sleep(1)
print('go')
start=time()
word=input()
stop=time()
diff=stop-start
sec=diff%60
temp=diff//60
minute=temp%60
hour=temp//60
if hour>0:
    print('you took',hour,'hour(s)',minute,'minute(s)',sec,'seconds','to write-','\n',word)
elif minute>0:
    print('you took',minute,'minute(s)',sec,'seconds','to write-','\n',word)
else:
    print('you took',sec,'seconds','to write-','\n',word)
