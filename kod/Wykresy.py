import matplotlib.pyplot as plt
import pandas as pd
all_data = []
count = 0
basic = open("test_basic.txt", "r")
while count < 19:
    count += 1
    data = basic.readline()
    data = data.replace('[', '')
    data = data.replace(']', '')
    data = data.split(',')
    for e in range(len(data)): data[e]=float(data[e])
    all_data.append(data)  

x_list = []
y = 0.05
while y < 1:
    x_list.append(y)  
    y += 0.05 

plot_data_11 = []
plot_data_12 = []
plot_data_13 = []
#plt.plot(x_list, all_data[:][0])
#plt.show()
tmp = 0
while tmp < 19:
        plot_data_11.append(all_data[tmp][0])
        plot_data_12.append(all_data[tmp][1])
        plot_data_13.append(all_data[tmp][2])
        tmp += 1
fig, ax = plt.subplots(nrows=3)
fig.suptitle("Drzewo orginalne")
plot_data_11 = [round(x, 1) for x in plot_data_11]
ax[0].plot(x_list, plot_data_11)
plot_data_12 = [round(x, 1) for x in plot_data_12]
ax[1].plot(x_list, plot_data_12)

ax[2].plot(x_list, plot_data_13)
ax[0].set_ylabel("Dopasowanie")
ax[1].set_ylabel("Dopasowanie")
ax[2].set_xlabel("Ilość  danych")
ax[2].set_ylabel("Dopasowanie")
ax[0].set_title('Zbiór "bank"')
ax[1].set_title('Zbiór "agaricus-lepiota"')
ax[2].set_title('Zbiór "student-mat"')
plt.show()
i = 0.05
all_x = []
while i < 1:
    
    x = "%s, %s" % (str(round(i,2)), str(round((1-i),2)))
    i += 0.05
    all_x.append(x)


count = 0
tmp = 0
all_data = []
plot_data_all_1 = []
plot_data_all_2 = []
plot_data_all_3 = []
i = 0.15
while i < 1:
    name = "test_incremental_%f.txt" % (i)
    inc = open(name, "r")
    mean_data = []
    count = 0
    all_data = []
    while count < 19:
        count += 1
        data = inc.readline()
        data = data.replace('[', '')
        data = data.replace(']', '')
        data = data.split(',')
        for e in range(len(data)): data[e]=float(data[e])
        all_data.append(data)
    tmp = 0
    plot_data_1 = []
    plot_data_2 = []
    plot_data_3 = []
    while tmp < 19:
        plot_data_1.append(all_data[tmp][0])
        plot_data_2.append(all_data[tmp][1])
        plot_data_3.append(all_data[tmp][2])
        tmp += 1
    plot_data_all_1.append(plot_data_1)
    plot_data_all_2.append(plot_data_2)
    plot_data_all_3.append(plot_data_3)
    i += 0.05

tmp = 0
sd_1 = []
sd_2 = []
sd_3 = []
r = 0
p_1 =[]
p_2 =[]
p_3 =[]
while r < 19:
    while tmp < 17:
        sd_1.append(plot_data_all_1[tmp][r])
        sd_2.append(plot_data_all_2[tmp][r])
        sd_3.append(plot_data_all_3[tmp][r])
        tmp += 1
    p_1.append(sum(sd_1) / len(sd_1))
    p_2.append(sum(sd_2) / len(sd_2))
    p_3.append(sum(sd_3) / len(sd_3))
    r += 1

fig, ax = plt.subplots()
ax.plot(all_x, plot_data_all_1[12], label='ilość danych 0.75 zbioru treningowego - max dopasowanie')
ax.plot(all_x, p_1, label='średnia')
ax.plot(all_x, plot_data_all_1[0], label='ilość danych 0.15 zbioru treningowego - min dopasowanie')
ax.set_ylabel("Dopasowanie")
ax.set_xlabel("Ilość danych odpowiednio, do budowy podstawowego drzewa, użyte do uczenia przyrostowego")
ax.set_title('Uczenie przyrostowe, zbiór "Bank"')
ax.legend()
plt.show()
count = 0
fig, ax = plt.subplots()
for w in plot_data_all_3:
    
    ax.plot(all_x, w, label='%d' % count)
    count += 1
ax.legend()
plt.show()

fig, ax = plt.subplots()
plot_data_all_2[16] = [round(x, 1) for x in plot_data_all_2[16]]
ax.plot(all_x, plot_data_all_2[16], label='ilość danych 0.95 zbioru treningowego - max dopasowanie')
p_2 = [round(x, 1) for x in p_2]
ax.plot(all_x, p_2, label='średnia')
plot_data_all_2[0] = [round(x, 1) for x in plot_data_all_2[0]]
ax.plot(all_x, plot_data_all_2[0], label='ilość danych 0.15 zbioru treningowego - min dopasowanie')
ax.set_ylabel("Dopasowanie")
ax.set_xlabel("Ilość danych odpowiednio, do budowy podstawowego drzewa, użyte do uczenia przyrostowego")
ax.set_title('Uczenie przyrostowe, zbiór "agaricus-lepiota"')
ax.legend()
plt.show()
fig, ax = plt.subplots()

ax.plot(all_x, plot_data_all_3[14], label='ilość danych 0.85 zbioru treningowego - max dopasowanie')
ax.plot(all_x, p_3, label='średnia')
ax.plot(all_x, plot_data_all_3[1], label='ilość danych 0.20 zbioru treningowego - min dopasowanie')
ax.set_ylabel("Dopasowanie")
ax.set_xlabel("Ilość danych odpowiednio, do budowy podstawowego drzewa, użyte do uczenia przyrostowego")
ax.set_title('Uczenie przyrostowe, zbiór "student-mat"')
ax.legend()
plt.show()
mean_1 = []

fig, ax = plt.subplots()
for pd_1 in plot_data_all_1:
    mean_1.append(sum(pd_1) / len(pd_1))

ax.plot(x_list[2:], mean_1, label = 'średnia, uczenie przyrostowe')
ax.plot(x_list[2:], plot_data_11[2:], label = 'Drzewo orginalne' )
ax.set_xlabel("ilość danych")
ax.set_ylabel("Dopasowanie")
ax.set_title('Porównanie uczenia przyrostowego i trzewa podstawowego, zbiór "Bank"')
ax.legend()
plt.show()

mean_2 = []

fig, ax = plt.subplots()
for pd_2 in plot_data_all_2:
    mean_2.append(sum(pd_2) / len(pd_2))
mean_2 = [round(x, 1) for x in mean_2]
ax.plot(x_list[2:], mean_2, label = 'średnia, uczenie przyrostowe')
ax.plot(x_list[2:], plot_data_12[2:], label = 'Drzewo orginalne' )
ax.set_xlabel("ilość danych")
ax.set_ylabel("Dopasowanie")
ax.set_title('Porównanie uczenia przyrostowego i trzewa podstawowego, zbiór "agaricus-lepiota"')
ax.legend()
plt.show()

mean_3 = []

fig, ax = plt.subplots()
for pd_3 in plot_data_all_3:
    mean_3.append(sum(pd_3) / len(pd_3))
ax.plot(x_list[2:], mean_3, label = 'średnia, uczenie przyrostowe')
ax.plot(x_list[2:], plot_data_13[2:], label = 'Drzewo orginalne' )
ax.set_xlabel("ilość danych")
ax.set_ylabel("Dopasowanie")
ax.set_title('Porównanie uczenia przyrostowego i trzewa podstawowego, zbiór "student-mat"')
ax.legend()
plt.show()