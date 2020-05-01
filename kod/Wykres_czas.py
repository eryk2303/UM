import matplotlib.pyplot as plt
import pandas as pd


def basic(name):
    time_all = []
    basic_file = open(name, "r")
    count = 0
    while count < 19:
        count += 1
        file_time = str(basic_file.readline())
        file_time = file_time.replace(":", ".")
        file_time = file_time[3:].split('.')
        time_float = []
        for item in file_time:
            time_float.append(float(item))
        time = time_float[0]*60 + time_float[1] + time_float[2]*10**(-6)
        time_all.append(round(time, 2))
    return time_all


bank_basic = basic("bank_time_basic.txt")
agaricus_basic = basic("grzyby_time_basic.txt")
student_basic = basic('student_time_basic.txt')

x_list = []
y = 0.05
while y < 1:
    x_list.append(y)  
    y += 0.05 


fig, ax = plt.subplots(nrows=3)
fig.suptitle("Drzewo orginalne")
ax[0].plot(x_list, bank_basic)
ax[1].plot(x_list, agaricus_basic)
ax[2].plot(x_list, student_basic)
ax[0].set_ylabel("Czas [s]")
ax[1].set_ylabel("Czas [s]")
ax[2].set_xlabel("Ilość  danych")
ax[2].set_ylabel("Czas [s]")
ax[0].set_title('Zbiór "bank"')
ax[1].set_title('Zbiór "agaricus-lepiota"')
ax[2].set_title('Zbiór "student-mat"')
plt.show()

def inc_basic(basic):
    basic_inc = []
    for tmp in basic:
        basic_inc.append(round(tmp + basic[-1], 2))
    return basic_inc

def incremental(name):
    time_all = []
    basic_file = open(name, "r")
    count = 0
    while count < 19:
        count += 1
        file_time = str(basic_file.readline())
        file_time = file_time.replace(":", ".")
        file_time = file_time[3:].split('.')
        time_float = []
        for item in file_time:
            time_float.append(float(item))
        time = time_float[0]*60 + time_float[1] + time_float[2]*10**(-6)
        time_all.append(round(time, 2))
    return time_all


bank_incremental = incremental('bank_time_incremental_0.950000.txt')
agaricus_incremental = incremental('grzyby_time_incremental_0.950000.txt')
student_incremental = incremental('student_time_incremental_0.950000.txt')
bank_basic_inc = inc_basic(bank_basic)
agaricus_basic_inc = inc_basic(agaricus_basic)
student_basic_inc = inc_basic(student_basic)
print(bank_basic_inc)

i = 0.05
all_x = []
while i < 1:
    
    x = "%s, %s" % (str(round(i,2)), str(round((1-i),2)))
    i += 0.05
    all_x.append(x)

fig, ax = plt.subplots(nrows=3)
fig.suptitle("Uczenie przyrostowe, ilość danych użytych do trenowania - 0.95 całego zbioru treningowego")
ax[0].plot(all_x, bank_incremental, label = 'algorymt uczenia przyrostowego')
ax[0].plot(all_x, bank_basic_inc, label = 'orginalny algorytm')
ax[1].plot(all_x, agaricus_incremental)
ax[1].plot(all_x, agaricus_basic_inc)
ax[2].plot(all_x, student_incremental)
ax[2].plot(all_x, student_basic_inc)
ax[0].set_ylabel("Czas [s]")
ax[1].set_ylabel("Czas [s]")
ax[2].set_xlabel("Ilość danych odpowiednio, do budowy podstawowego drzewa, użyte do uczenia przyrostowego")
ax[2].set_ylabel("Czas [s]")
ax[0].set_title('Zbiór "bank"')
ax[1].set_title('Zbiór "agaricus-lepiota"')
ax[2].set_title('Zbiór "student-mat"')
fig.legend()
plt.show()

