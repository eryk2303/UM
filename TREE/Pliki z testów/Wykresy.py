import matplotlib.pyplot as plt
import pandas as pd

count = 0
basic = open("test_basic.txt", "r")
while count < 19:
    count += 1
    data = basic.readline()
    data = data.replace('[', '')
    data = data.replace(']', '')
    data = data.split(',')
    for e in range(len(data)): data[e]=float(data[e])

i = 0
all_x = []
while i is not 95:
    i += 5
    x = "0.%d, 0.%d" % (i, 100-i)
    all_x.append(x)

count = 0
tmp = 0
all_data = []

i = 0.15
while i < 1:
    name = "test_incremental_%f.txt" % (i)
    inc = open(name, "r")
    i += 0.05
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
    plt.plot(all_x, plot_data_1)
    plt.show()