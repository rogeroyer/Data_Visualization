# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r'data2.xls', encoding='utf-8', header=None, names=['date', 'sales'])

data1 = data[(data.sales >= 0) & (data.sales < 500)].reset_index().drop(['index'], axis=1)
data2 = data[(data.sales >= 500) & (data.sales < 1000)].reset_index().drop(['index'], axis=1)
data3 = data[(data.sales >= 1000) & (data.sales < 1500)].reset_index().drop(['index'], axis=1)
data4 = data[(data.sales >= 1500) & (data.sales < 2000)].reset_index().drop(['index'], axis=1)
data5 = data[(data.sales >= 2000) & (data.sales < 2500)].reset_index().drop(['index'], axis=1)
data6 = data[(data.sales >= 2300) & (data.sales < 3000)].reset_index().drop(['index'], axis=1)
data7 = data[(data.sales >= 3000) & (data.sales < 3500)].reset_index().drop(['index'], axis=1)
data8 = data[(data.sales >= 3500) & (data.sales < 4000)].reset_index().drop(['index'], axis=1)


def draw_bar():
    global data1, data2, data3, data4, data5, data6, data7, data8
    # data_frame = pd.DataFrame([index for index in range(1, 9, 1)])
    data_frame = pd.DataFrame(['[0, 500)', '[500, 1000)', '[1000, 1500)', '[1500, 2000)', '[2000, 2500)', '[2500, 3000)', '[3000, 3500)', '[3500, 4000)'])

    temp = []
    for index in [data1, data2, data3, data4, data5, data6, data7, data8]:
        temp.append(list(index.sales))

    temp = pd.Series(temp)
    data_frame['list'] = temp
    data_frame.columns = ['index', 'list']
    data_frame['mean'] = data_frame['list'].map(lambda x: np.mean(x))
    data_frame['median'] = data_frame['list'].map(lambda x: np.median(x))
    data_frame['count'] = data_frame['list'].map(lambda x: len(x))
    total_num = sum(data_frame['count'])       # 总记录数 #
    data_frame['frequency'] = data_frame['count'].map(lambda x: x / total_num)

    '''累计频率'''
    acc_fre = list(data_frame['frequency'])
    for index in range(1, 8, 1):
        acc_fre[index] = acc_fre[index] + acc_fre[index - 1]

    data_frame['acc_fre'] = np.array(acc_fre)
    data_frame.index = data_frame['index']
    data_frame = data_frame.drop(['list', 'index'], axis=1)
    print(data_frame)

    bar_width = 0.2    # 柱宽度 #
    # exit(0)
    '''mean median count frequency acc_fre'''
    x = np.arange(8)
    plt.bar(x, data_frame['mean'], bar_width, color='yellow', label='mean')
    plt.bar(x + bar_width, data_frame['median'], bar_width, color='orange', label='median')
    plt.xticks(x + bar_width / 2, data_frame.index)
    plt.legend()
    plt.tight_layout()
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Mean and Median')
    plt.show()

    plt.bar(x, data_frame['count'], bar_width, color='black', label='count')
    plt.bar(x + bar_width * 1, data_frame['frequency'], bar_width, color='blue', label='frequency')
    plt.bar(x + bar_width * 2, data_frame['acc_fre'], bar_width, color='red', label='acc_fre')
    plt.xticks(x + bar_width * 1, data_frame.index)
    plt.legend()
    plt.tight_layout()
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Count and Frequency and Acc_fre')
    plt.show()


if __name__ == '__main__':
    draw_bar()
