#coding=utf-8

import matplotlib.pyplot as plt
from numpy import array
import pandas as pd
import numpy as np
import datetime
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

dataset_one = pd.read_csv(r'dataset_one.csv', encoding='utf-8')
dataset_two = pd.read_csv(r'dataset_two.csv', encoding='utf-8')

# print(dataset_one)
# print(dataset_two)

'''Question_one'''
# dataset_one['time'] = [int(index.split(' ')[0].split('/')[2]) for index in dataset_one['time']]
# time_bar = pd.pivot_table(dataset_one, index='time', values='sequence', aggfunc='count').reset_index()
# print(time_bar)
# X = list(time_bar['time'])
# Y = list(time_bar['sequence'])
# plt.bar(X, Y, color='blue')
# plt.xlabel('Time')
# plt.ylabel('Records')
# plt.title('Time-Records')
# plt.show()
#
# # plt.hist(list(dataset_one['time']), bins=5, color='blue')
# # plt.show()

'''Question_two'''
# send = dataset_one[dataset_one['sender'] == '本机'].shape[0]
# receive = dataset_one[dataset_one['sender'] != '本机'].shape[0]
# X = ['send', 'receive']
# Y = [send, receive]
#
# cols = ['orange', 'purple']
# plt.pie(Y,
#         labels=X,
#         colors=cols,
#         startangle=90,
#         shadow=True,
#         explode=(0, 0.1),
#         autopct='%1.1f%%',
#         )
#
# plt.title('The way of communicate')
# plt.show()


'''Question_three'''
# # print(dataset_one)
# records = pd.DataFrame(list(dataset_one['sender']) + list(dataset_one['receiver']), columns=['phone_number'])
# way = records['phone_number'].value_counts().reset_index()
# way = way[way['index'] != '本机']
# way = way.iloc[:10, :]
# print(way)
# X = list(way['index'])
# Y = list(way['phone_number'])
# plt.pie(Y,
#         labels=X,
#         startangle=90,
#         shadow=True,
#         autopct='%1.1f%%',
#         )
# plt.title('Top ten user')
# plt.show()

'''Question_four'''
# # print(dataset_one)
# send = dataset_one[dataset_one['sender'] == '本机']
# print(send[send['cost'] == 0.1])
# print(send[send['cost'] != 0.1])
# receive = dataset_one[dataset_one['sender'] != '本机']
# print(receive[receive['cost'] == 0.1])
# print(receive[receive['cost'] != 0.1])

'''Question_five'''
# # print(dataset_one)
# records = pd.DataFrame(list(dataset_one['sender']) + list(dataset_one['receiver']), columns=['phone_number'])
# way = records['phone_number'].value_counts().reset_index()
# way = way[way['index'] != '本机']
# way.loc[way['phone_number'] > 1, 'phone_number'] = 1
# print(way)
# X = list(way['index'])
# Y = list(way['phone_number'])
# plt.pie(Y,
#         labels=X,
#         startangle=90,
#         shadow=True,
#         autopct='%1.1f%%',
#         )
# plt.title('All user')
# plt.show()


'''Question_six'''
# print(dataset_two)
'''民族与人数关系'''
# x = range(len(list(dataset_two['nation'])))
# y = list(dataset_two['num'])
# N = len(x)
# colors = np.random.rand(N)
# area = [index**2 * 0.0000000007 for index in list(dataset_two['num'])]   #   * 0.0000000007  #
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.ylim(0, 2.5*1e7)
# plt.xlim(-10, N)
# # plt.xlabel(u"时间", fontproperties='SimHei')  # 中文标注 #
# plt.xticks(x, list(dataset_two['nation']), rotation=60, fontproperties='SimHei')   # , rotation='vertical' #
# plt.show()
'''民族与城市关系'''
# city = list(dataset_two['distribute'])
# city = [index.count('.')+1 for index in city]
# print(city)
# x = range(len(list(dataset_two['nation'])))
# y = city
# N = len(x)
# colors = np.random.rand(N)
# area = [index**2 * 50 for index in city]   #   * 0.0000000007  #
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.ylim(0, 25)
# plt.xlim(-5, N)
# # plt.xlabel(u"时间", fontproperties='SimHei')  # 中文标注 #
# plt.xticks(x, list(dataset_two['nation']), rotation=60, fontproperties='SimHei')   # , rotation='vertical' #    # 文字倾斜角度   xticks(x, x_label)更改横坐标标记 #
# plt.show()

'''Question_seven'''
# # print(dataset_two)
# city_dict = {}
# city = list(dataset_two['distribute'])
# for index in city:
#     if (index.count('.') == 0) and (index not in city_dict.keys()):
#         city_dict[index] = 1
#     elif (index.count('.') == 0) and (index in city_dict.keys()):
#         city_dict[index] += 1
#     else:
#         string = index.split('.')
#         for str in string:
#             if str not in city_dict.keys():
#                 city_dict[str] = 1
#             else:
#                 city_dict[str] += 1
#
# print(city_dict.keys())
# print(city_dict.values())
# x = range(len(list(city_dict.keys())))
# y = list(city_dict.values())
# N = len(x)
# colors = np.random.rand(N)
# area = [index**2 * 30 for index in list(city_dict.values())]
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.ylim(0, 30)
# plt.xticks(x, list(city_dict.keys()), rotation=60, fontproperties='SimHei')   # , rotation='vertical' #
# plt.show()


'''Question_eight'''
# print(dataset_two)
nation = list(dataset_two['nation'])
city = list(dataset_two['distribute'])
print(nation)
print(city)

'''打印节点数据'''
for index in nation:
    print("{name: \"%s\"}," % index)
print(len(nation))

city_set = []
for index in city:
    if index.count('.') == 0:
        city_set.append(index)
    else:
        for str in index.split('.'):
            city_set.append(str)

city_set = list(set(city_set))
print(len(city_set))
for index in city_set:
    print("{name: \"%s\"}," % index)
print(city_set)

for index in range(len(nation)):
    if city[index].count('.') == 0:
        print("{source: %d" % index + ", target: %d}," % (city_set.index(city[index])+55))
    else:
        for str in city[index].split('.'):
            print("{source: %d" % index + ", target: %d}," % (city_set.index(str) + 55))

print('记得换city')

