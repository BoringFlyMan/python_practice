#!/usr/bin/env python3

import csv
import enum
from fileinput import filename
from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows =[], [], []
    for row in reader:
        current_date = datetime.strptime(row[0],'%Y-%m-%d')
        try:    
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title('zuigaowendu', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('wendu(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()