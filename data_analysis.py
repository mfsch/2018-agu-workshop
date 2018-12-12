"""
Load and process time series from from Berkeley Earth.
"""

import numpy as np
import requests

def gen_url(location):
    url = 'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/%s-TAVG-Trend.txt' % location.lower()
    return url

def fetch_data(location):
    url = gen_url(location)
    response = requests.get(url)
    data = np.loadtxt(response.iter_lines(), comments="%")
    return data

def moving_average(data, window):
    avg = np.full(data.size, np.nan)
    for i in range(6, data.size - 6):
        avg[i] = np.mean(data[i-6:i+6])
    return avg

def test_moving_average():
    avg = moving_average(np.ones(10), 2)
    assert np.all(np.isnan(avg[0:2]))
    assert np.all(np.isnan(avg[-2:]))
    assert np.allclose(avg[2:-2], 1)
