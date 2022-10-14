import time
print("What shall I remind you about?")
text=str(input())
print("In how many minutes would you like me to remind you ?")
time.localtime=float(input())
time.localtime=time.localtime*60
time.sleep(time.localtime)
print(text)
