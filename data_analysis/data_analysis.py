"""
Load and process time series from from Berkeley Earth.
"""

import numpy as np
import requests

def gen_url(location):
    url = 'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/%s-TAVG-Trend.txt' % location.lower()
    return url

"""
Download data for a given location.
"""
def fetch_data(location):
    url = gen_url(location)
    response = requests.get(url)
    data = np.loadtxt(response.iter_lines(), comments="%")
    return data

def moving_average(data, window):
    avg = np.full(data.size, np.nan)
    for i in range(window, data.size - window):
        avg[i] = np.mean(data[i-window:i+window])
    return avg
