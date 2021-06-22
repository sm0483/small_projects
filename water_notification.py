from plyer import notification
import time
import datetime

def nota(ti,messa):
    notification.notify(title=ti,message=messa,timeout=10)
  


def tm():
    now=datetime.datetime.now()
    tm.time=f"{now.hour}:{now.minute}"
    return tm.time
  
def function():
    tm()
    mark=1
    working_time=input("Enter time [hour:minutes]: ")
    drinking_cycle=float(input("Enter Gap For Drinking Water(hours): "))
    gap=drinking_cycle*3600
    while tm.time!=working_time:
        mark=mark+1
        time.sleep(gap)
        if mark%2==0:
            nota("Water","Drink Water")
        elif mark%2!=0:
            nota("Stop","Get Up And Warm Up")

        
            
            
            
try:
    function()
except KeyboardInterrupt:
    print("[+] script stoped execution")
