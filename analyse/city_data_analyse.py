# -*- coding:utf-8 -*-

'''
@author: roger
@date:2018-7-19
'''

import re
import pandas as pd
import matplotlib.pyplot as plt


class DataMining(object):
    def __init__(self, operator_type, client=True):
        self.__operator_type = operator_type
        self.__client = client
        self.__file = None
        self.__excute()

    def __excute(self):
        self.__file = open(r'../dataSet/file.txt', 'r', encoding='utf-8')
        if self.__operator_type == 'domain':
            self.domain()
        elif self.__operator_type == 'operator':
            self.operator()
        elif self.__operator_type == 'mozilla_inner':
            self.mozilla_inner()
        elif self.__operator_type == 'mozilla':
            self.mozilla()
        else:
            self.address()
        self.__file.close()  # 关闭文件 #

    def domain(self):
        domain = re.compile('www\.[-\w]+\.[a-z]{2,4}')  # 域名检测,只检测含有www开头的域名 #
        temp_list = []
        for f in self.__file.readlines():
            word = f.strip()
            domain_list = domain.findall(word)
            if len(domain_list) != 0:
                temp_list.extend(domain_list)
            else:
                continue

        domain_list = pd.DataFrame({'domain': temp_list, 'count': [1 for index in range(len(temp_list))]})
        domain_cnt = domain_list.groupby(['domain'])['count'].count().reset_index()

        if self.__client is True:
            print(domain_cnt)

        domain_cnt = domain_cnt.sort_values(by=['count'], ascending=False).reset_index().drop(['index'], axis=1)
        print_cnt = 8
        x = list(domain_cnt['domain'])[:print_cnt]
        y = list(domain_cnt['count'])[:print_cnt]
        plt.pie(y,
                labels=x,
                startangle=90,
                shadow=True,
                autopct='%1.1f%%',
                )
        plt.title('Domain Statistic')
        plt.show()

    def operator(self):
        operator = re.compile('Windows NT|Mac OS|Linux|GoogleMaps')  # 操作系统类型 #
        temp_list = []
        for f in self.__file.readlines():
            word = f.strip()
            operator_list = operator.findall(word)
            if len(operator_list) != 0:
                temp_list.extend(operator_list)
            else:
                continue

        operator_list = pd.DataFrame({'operator': temp_list, 'count': [1 for index in range(len(temp_list))]})
        operator_cnt = operator_list.groupby(['operator'])['count'].count().reset_index()

        if self.__client is True:
            print(operator_cnt)

        '''饼图'''
        x = list(operator_cnt['operator'])
        y = list(operator_cnt['count'])
        plt.pie(y,
                labels=x,
                startangle=90,
                shadow=True,
                autopct='%1.1f%%',
                )
        plt.title('Operator System Statistic')
        plt.show()

    def mozilla_inner(self):
        mozilla_inner = re.compile('Presto|Gecko|Trident|AppleWebKit')  # 浏览器内核 #
        temp_list = []
        for f in self.__file.readlines():
            word = f.strip()
            mozilla_inner_list = mozilla_inner.findall(word)
            # 打印浏览器内核 #
            if len(mozilla_inner_list) == 2:
                mozilla_inner_list.pop()
            if len(mozilla_inner_list) != 0:
                temp_list.extend(mozilla_inner_list)
            else:
                continue

        mozilla_inner_list = pd.DataFrame({'mozilla_inner': temp_list, 'count': [1 for index in range(len(temp_list))]})
        mozilla_inner_cnt = mozilla_inner_list.groupby(['mozilla_inner'])['count'].count().reset_index()

        if self.__client is True:
            print(mozilla_inner_cnt)

        '''饼图'''
        x = list(mozilla_inner_cnt['mozilla_inner'])
        y = list(mozilla_inner_cnt['count'])
        plt.pie(y,
                labels=x,
                startangle=90,
                shadow=True,
                autopct='%1.1f%%',
                )
        plt.title('Mozilla Kernel Statistic')
        plt.show()

    def mozilla(self):
        mozilla = re.compile('Chrome|Safari|Firefox|Mobile')  # 浏览器名称 #
        temp_list = []
        for f in self.__file.readlines():
            word = f.strip()
            mozilla_list = mozilla.findall(word)
            if len(mozilla_list) == 2:
                mozilla_list[0] = ' '.join(mozilla_list)
                mozilla_list.pop()
            temp_list.extend(mozilla_list)

        mozilla_list = pd.DataFrame({'mozilla': temp_list, 'count': [1 for index in range(len(temp_list))]})
        mozilla_cnt = mozilla_list.groupby(['mozilla'])['count'].count().reset_index()

        if self.__client is True:
            print(mozilla_cnt)

        x = list(mozilla_cnt['mozilla'])
        y = list(mozilla_cnt['count'])
        plt.pie(y,
                labels=x,
                startangle=90,
                shadow=True,
                autopct='%1.1f%%',
                )
        plt.title('Mozilla Static')
        plt.show()

    def address(self):
        address = re.compile('\"tz\": \"[\w]+[\/\\\]{1,2}[\w]+\"')  # 匹配城市地点 #
        temp_list = []
        for f in self.__file.readlines():
            word = f.strip()
            address_list = address.findall(word)
            # 打印地址信息 #
            if len(address_list) == 0:
                continue
            else:
                temp_list.append(address_list[0].split('"')[3].replace('\\/', ' '))

        address_list = pd.DataFrame({'address': temp_list, 'count': [1 for index in range(len(temp_list))]})
        address_cnt = address_list.groupby(['address'])['count'].count().reset_index()
        address_cnt = address_cnt.sort_values(by=['count'], ascending=False).reset_index().drop(['index'], axis=1)

        if self.__client is True:
            print(address_cnt)

        print_cnt = 6
        x = list(address_cnt['address'])[:print_cnt]
        y = list(address_cnt['count'])[:print_cnt]
        plt.pie(y,
                labels=x,
                startangle=90,
                shadow=True,
                autopct='%1.1f%%',
                )
        plt.title('Address Statistic')
        plt.show()


'''主函数入口'''
if __name__ == '__main__':
    DataMining('domain', client=True)  # domain  operator mozilla_inner mozilla address #
    DataMining('operator', client=True)
    DataMining('mozilla_inner', client=True)
    DataMining('mozilla', client=True)
    DataMining('address', client=True)

