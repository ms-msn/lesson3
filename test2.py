import json
from datetime import datetime
date_now = datetime.now()



with open('data.json', 'r', encoding='Windows-1251') as fh: #открываем файл на чтение
    data = json.load(fh) #загружаем из файла данные в словарь data
for d in data :
    #print(d["NameOfStation"],len(d['RepairOfEscalators']))
    if len(d['RepairOfEscalators']) > 0 :
        date_last = d['RepairOfEscalators'][len(d['RepairOfEscalators']) -1]['RepairOfEscalators']
        #print(date_last)
        date_last_split = date_last.split('-')
        deadline = datetime.strptime(date_last_split[1], "%d.%m.%Y")
        #print(deadline)
        #print(date_now)
        if deadline > date_now:
            print(d["Name"])
            print(deadline)