from SlApp import *
import time
#rolling updates every minute.
while True:
    print('----------------------------------')
    print('Last Update: ', time.ctime()) #last update
    print('')
    SegersjoMotTumba()   #local bus stop to train station
    print('')
    TumbaMotMarsta()  #trains leaving towards sthlm C
    print('')
    print("Information: ")
    Deviations()       #deviations and traffic information
    print('----------------------------------')
    time.sleep(60)
