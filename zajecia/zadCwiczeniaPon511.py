import statistics

statistics.mean([1, 2, 3]) #srednia z 3 liczb - odwolanie po kropce, po imporcie

from statistics import mean #wtedy mogę bez kropki. Po import możemy po przecinku dać po mean, itd
#mean()

#jak mamy funkcję (bez kropki) to możemy alt+enter i pokaże skąd możemy ją importować, np funkcja median



import datetime

now = datetime.datetime.now()
now2 = datetime.datetime.now()

print(now, now2)

#ręczne tworzenie datatime
datetime_object = datetime.datetime(2020, 12, 14, 13, 45, 33)
print(datetime_object)

#możemy na datatime objekcie robić różne operacje, np.
#znaczniki po procentach w dokumentacji
print(datetime_object.strftime("%m-%d-%Y, %A"))