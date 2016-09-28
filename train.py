#!/ user/bin/env python
# -*- coding: cp936 -*-

'''Train tickets query via command-line.

Usage:
    train [-gdtkz] <from> <to> <date>
    
Options:
    -h,--help   help menu
    -g          gaotie
    -d          dongche
    -t          tekuai
    -k          kuaisu
    -z          zhida
    
Example:
    tickets beijing shanghai 2016-08-25
'''

import re
import requests
from prettytable import PrettyTable

from docopt import docopt

import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def colored(color,text):
    table = {'red':'\033[31m', 
        'green':'\033[32m',
        'nc':'\033[0m'}  #字典存放颜色
    cv = table.get(color)
    nc = table.get('nc')
    return ''.join([cv,text,nc])


class TrainCollection(object):
    header = 'train station time duration first second softsleep hardsleep hardsit'.split()

    def __init__(self, rows):
        self.rows = rows
        
    def _get_duration(self, row):        
        duration = row.get('lishi').replace(':', 'h') + 'm'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration
    
    @property
    def trains(self):
        for row in self.rows:
            train = [
                row['station_train_code'],
                '\n'.join([colored('green',row['from_station_name']), colored('red',row['to_station_name'])]),
                '\n'.join([colored('green',row['start_time']), colored('red',row['arrive_time'])]),
                self._get_duration(row),
                row['zy_num'],
                row['ze_num'],
                row['rw_num'],
                row['yw_num'],
                row['yz_num']
            ]
            yield train
            
    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header) #添加title
        pt.add_row(self.header)
        for train in self.trains:
            pt.add_row(train)  #加每一行的数据
        print pt 


def client():
    """command-line interface"""    
    arguments = docopt(__doc__)  #?????
    #print (arguments)
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8967'
    r = requests.get(url, verify = False).text     
    stations = re.findall(r'([A-Z]+)\|([a-z]+)', r)
    stations = dict(stations)
    sta = dict(zip(stations.values(),stations.keys()))
    from_station = sta[arguments.get('<from>')]
    print from_station
    to_station = sta[arguments.get('<to>')]
    queryDate = arguments.get('<date>')
    url1 = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(queryDate,from_station,to_station)
    print url1
    r1 = requests.get(url1, verify = False)
    rows = r1.json()['data']['datas']
    #print rows
    trains = TrainCollection(rows)
    trains.pretty_print()


if __name__== '__main__':
    client()
