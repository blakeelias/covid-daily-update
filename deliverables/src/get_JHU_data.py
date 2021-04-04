import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def get_JHU_data():
    df = pd.read_csv('data/JH/COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
    focus = df.copy().drop(['Lat','Long'], axis=1).set_index(['Country/Region','Province/State'])
    for i in focus.loc['US'].index:
        if ',' in i:
            focus.drop(i, level='Province/State', inplace=True)
    confirm = focus.groupby('Country/Region').sum()

    df = pd.read_csv('data/JH/COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')
    focus = df.copy().drop(['Lat','Long'], axis=1).set_index(['Country/Region','Province/State'])
    for i in focus.loc['US'].index:
        if ',' in i:
            focus.drop(i, level='Province/State', inplace=True)
    death = focus.groupby('Country/Region').sum()

    df = pd.read_csv('data/JH/COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')
    focus = df.copy().drop(['Lat','Long'], axis=1).set_index(['Country/Region','Province/State'])
    for i in focus.loc['US'].index:
        if ',' in i:
            focus.drop(i, level='Province/State', inplace=True)
    recover = focus.groupby('Country/Region').sum()
    
    data = {'Confirmed':confirm, 'Death':death, 'Recovered':recover}
    return data