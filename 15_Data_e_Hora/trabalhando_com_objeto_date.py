'''
O móodulo 'datetime' em Python é usado para lidar com datas e horas. Ele possui várias classes úteis como date, time e timedelta

Exemplo
from datetime import date

d = date(2025, 7, 30)
print(d) #2025-07-30

# Manipulando datas

from datetime import date, datetime, time, timedelta

d = date(2025, 7, 30)
print(d) #2025-07-30
print(date.today())

data_hora = datetime(2025, 7, 30, 10)
print(data_hora)
print(datetime.today())

hora = time(10, 20)
print(hora)

# timedelta
data = datetime(2025, 7, 30)
print(data)
# Adicioonando uma semana
d = data + timedelta(weeks=1)
print(d)


# Formatar e converter datas com strftime e strptime

import datetime
d = datetime.datetime.now()

# formatano data e hora
print(d.strftime('%d/%m/%Y %H:%M'))

# convertendo string para datetime
date_string = '30/07/2025 15:05'
d = datetime.datetime.strptime(date_string, '%d/%m/%Y %H:%M')
print(d)



'''
# Trabalhando com timezone
import datetime
import pytz

# criando datetime com timezone
data_sao_paulo = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
data_oslo = datetime.datetime.now(pytz.timezone('Europe/Oslo'))
print(data_sao_paulo)
print(data_oslo)
