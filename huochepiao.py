#!/ user/bin/env python3

'''Train tickets query via command-line.
Usage:
    tickets [-gdtkz] <from> <to> <date>
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
import requests
import prettytable
import re
from docopt import docopt
from pprint import pprint
from prettytable import PrettyTable

def colored(color,text):
    table = {'red':'\033[91m',
        'green':'\033[92m',
        'nc':'\033[0m'}  #字典存放颜色
    cv = table.get(color)
    nc = table.get('nc')
    return ''.join([cv,text,nc])

class TrainCollection(object):
    # 显示车次、出发/到达站、 出发/到达时间、历时、一等坐、二等坐、软卧、硬卧、硬座
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
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)

def cli():
    '''command-line interface'''
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8967'
    r = requests.get(url, verify = False)
    stations = r.text
    stations = re.findall(r'([A-Z]+)\|([a-z]+)',stations)
    stations = dict(stations)
    stations = dict(zip(stations.values(),stations.keys()))
    #pprint(stations,indent=4)

    arguments = docopt(__doc__) 
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    url1 = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(date,from_station,to_station)
    print(url1)
    r = requests.get(url1,verify = False)
    print(r.json())
    rows = r.json()['data']['datas']
    trains = TrainCollection(rows)
    trains.pretty_print()

if __name__ == '__main__':
    cli()
    