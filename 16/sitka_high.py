#!/usr/bin/env python3

from contextlib import redirect_stderr
from pickle import HIGHEST_PROTOCOL
import csv
from fileinput import filename
import matplotlib.pyplot as plt
from datetime import datetime


from pygments import highlight
filename = 'data/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows =[], [], []
    for row in reader:
        current_date = datetime.strptime(row[0],'%Y-%m-%d')
        high = int(row[1])
        low = int(row[3])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title('zuigaowendu', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('wendu(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
