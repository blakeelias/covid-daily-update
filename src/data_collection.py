import pandas as pd
import numpy as np
import inspect

# display source code
def get_Code(f):
    lines = inspect.getsource(f)
    print(lines)

# Data collection of the world by country
def get_global_cases_total():
    df = pd.read_csv('data/JH/confirm_agg.csv').set_index('Country/Region').T.fillna(0).astype('int')
    df['Global'] = df.sum(axis=1)
    df = df[df.iloc[-1].sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Global', inplace=True)
    print('Global cases (total) by country fetched for %s'%df.index[-1].strftime('%m-%d'))
    return(df)

def get_global_deaths_total():
    df = pd.read_csv('data/JH/death_agg.csv').set_index('Country/Region').T.fillna(0).astype('int')
    df['Global'] = df.sum(axis=1)
    df = df[df.iloc[-1].sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Global', inplace=True)
    print('Global deaths (total) by country fetched for %s'%df.index[-1].strftime('%m-%d'))
    return(df)

def get_global_recovers_total():
    df = pd.read_csv('data/JH/recover_agg.csv').set_index('Country/Region').T.fillna(0).astype('int')
    df['Global'] = df.sum(axis=1)
    df = df[df.iloc[-1].sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Global', inplace=True)
    print('Global recovers (total) by country fetched for %s'%df.index[-1].strftime('%m-%d'))
    return(df)




# Data collection of a country by state
def get_US():
    df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
    df = df.pivot(index='date', columns='state', values='cases')
    df = df.diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('US', inplace=True)
    print('US cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))
    return(df)

def get_US_death():
    df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
    df = df.pivot(index='date', columns='state', values='deaths')
    df = df.diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('US', inplace=True)
    print('US deaths by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))
    return(df)

def get_Brazil():
    df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')
    df = df.pivot_table(index='date',columns='state',values='newCases').fillna(0).drop('TOTAL',axis=1).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Brazil', inplace=True)
    print('Brazil cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))
    return(df)

def get_Switzerland():
    df = pd.read_csv('https://raw.githubusercontent.com/daenuprobst/covid19-cases-switzerland/master/covid19_cases_switzerland_openzh.csv')
    df = df.set_index('Date').diff().fillna(0).astype(int).drop('CH', axis=1)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Switzerland', inplace=True)
    print('Switzerland cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))
    return(df)

def get_South_Africa():
    df = pd.read_csv('https://raw.githubusercontent.com/SimonRosen173/Covid19SAData/master/data/confirmed_by_prov_timeline.csv')
    df = df.pivot_table(index='date', columns='province', values='daily_no')
    df = df.rename(columns={'EC':'Eastern Cape',
                       'FS':'Free State',
                       'GP':'Gauteng',
                       'KZN':'KwaZulu-Natal',
                       'LP':'Limpopo',
                       'MP':'Mpumalanga',
                       'NC':'Northern Cape',
                       'NW':'North West',
                       'WC':'Western Cape'
                      })
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('South Africa', inplace=True)
    print('South Africa cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))    
    return df

def get_Russia():
    df = pd.read_csv('https://raw.githubusercontent.com/PhtRaveller/covid19-ru/master/data/covid_stats.csv')
    df = df.query('category=="total"').drop(['category',
                                             'Наблюдение (всего)',
                                             'Россия - сумма по регионам',
                                             'Россия',
                                             'Наблюдение'], axis=1)
    df.index = pd.to_datetime(df.date, dayfirst=True)
    df.drop('date', axis=1, inplace=True)
    df = df.diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index.rename('Russia', inplace=True)
    print('Russia cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))
    return(df)

def get_Spain():
    df = pd.read_csv('https://raw.githubusercontent.com/Secuoyas-Experience/covid-19-es/master/datos-comunidades-csv/covid-19-ES-CCAA-DatosCasos.csv')
    df = df.pivot_table(index='fecha', columns='nombreCcaa', values='casosConfirmados').diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Spain', inplace=True)
    print('Spain cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))    
    return df

def get_UK():
    # only public lab results, less than total
    df = pd.read_csv('https://raw.githubusercontent.com/tomwhite/covid-19-uk-data/master/data/covid-19-cases-uk.csv')
    df['Area_full'] = df['Country'] + '-' + df['Area']
    df = df.pivot_table(index='Date', columns='Area_full', values='TotalCases').diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('UK', inplace=True)
    print('UK cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))    
    return df

def get_Italy():
    df = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv')
    df.data = df.data.apply(lambda i:i.split('T')[0])
    # df.data = pd.to_datetime(df.data)
    df = df.pivot_table(index='data',columns='denominazione_regione',values='nuovi_positivi')
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Italy', inplace=True)
    print('Italy cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))    
    return df  

def get_India():
    df = pd.read_csv('https://raw.githubusercontent.com/pratik-bose/CoronaTracker/V1/CoronaData.csv')
    df = df.pivot_table(index='Date',columns='Name_1',values='TotalCases').diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('India', inplace=True)
    print('India cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))    
    return df    

def get_Germany():
    df = pd.read_csv('https://raw.githubusercontent.com/averissimo/covid19.de.data/master/data/rki.covid19.csv', sep=';')
    df = df.groupby(['date','state']).agg(sum)['cases'].unstack().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Germany', inplace=True)
    print('Germany cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))    
    return df    

def get_Mexico():
    df = pd.read_csv('https://raw.githubusercontent.com/mariorz/covid19-mx-time-series/master/data/covid19_confirmed_mx.csv')
    df = df.set_index('Estado').T
    df.index = pd.to_datetime(df.index, dayfirst=True)
    df = df.diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index.rename('Mexico', inplace=True)
    print('Mexico cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))    
    return df    

def get_Canada():
    df = pd.read_csv('https://raw.githubusercontent.com/ishaberry/Covid19Canada/master/timeseries_prov/active_timeseries_prov.csv')
    df['date_active'] = pd.to_datetime(df['date_active'], dayfirst=True)
    # df = df.sort_values('date_active')
    df = df.pivot_table(index='date_active',columns='province',values='cumulative_cases').diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index.rename('Canada', inplace=True)
    print('Canada cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))    
    return df

def get_Peru():
    df = pd.read_csv('https://raw.githubusercontent.com/jmcastagnetto/covid-19-peru-data/main/datos/covid-19-peru-data.csv')
    df = df.pivot_table(index='date',columns='region',values='confirmed').fillna(0).diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Peru', inplace=True)
    print('Peru cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))    
    return df

def get_Chile():
    df = pd.read_csv('https://raw.githubusercontent.com/jorgeperezrojas/covid19-data/master/csv/confirmados.csv')
    df = df.T.drop_duplicates().T
    df = df.set_index('region').drop('codigo', axis=1).T.diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Chile', inplace=True)
    print('Chile cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))    
    return df

def get_Sweden():
    df = pd.read_csv('https://raw.githubusercontent.com/shortlisted/covid-19-sweden/master/cases_by_date_and_region.csv')
    df.drop('Totalt_antal_fall', axis=1, inplace=True)
    df.set_index('Statistikdatum', inplace=True)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Sweden', inplace=True)
    print('Sweden cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))
    return df

def get_Argentina():
    df = pd.read_csv('https://raw.githubusercontent.com/lucia15/Datos-Covid19-Argentina/master/Argentina-covid19-por-provincia.csv')
    df = df.pivot_table(index='fecha', columns='provincia', values='casos_total').fillna(0).diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Argentina', inplace=True)
    print('Argentina cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))
    return df

def get_Indonesia():
#     https://github.com/erlange/INACOVID
    df = pd.read_csv('https://raw.githubusercontent.com/erlange/INACOVID/master/data/csv/basic.csv')
    df = df.pivot_table(index='Date', columns='Location', values='Confirmed').drop('National', axis=1).diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Indonesia', inplace=True)
    print('Indonesia cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))
    return df

def get_Japan():
    df = pd.read_csv('https://raw.githubusercontent.com/swsoyee/2019-ncov-japan/master/50_Data/byDate.csv')
    df = df.set_index('date')
    df.index = pd.to_datetime(df.index,format='%Y%m%d')
    df = df.fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index.rename('Japan', inplace=True)
    print('Japan cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))
    return(df)

def get_Ireland():
    df = pd.read_csv('https://raw.githubusercontent.com/DavideMagno/IrelandCovidData/master/Covid19_Data_By_County.csv')
    df = df.pivot_table(index='Date', columns='County', values='Value')
    df.index = pd.to_datetime(df.index)
    df = df[df.sum().sort_values(ascending=False).index].diff().fillna(0).astype(int)
    df.index.rename('Ireland', inplace=True)
    print('Ireland cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))
    return (df)

def get_Australia():
    df = pd.read_json('https://raw.githubusercontent.com/covid-19-au/covid-19-au.github.io/prod/src/data/state.json')
    for i in df.columns:
        df[i] = df[i].apply(lambda x:x[0])
    df = df.T.diff().fillna(0).astype(int)
    df.index = pd.to_datetime(df.index)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index.rename('Australia', inplace=True)
    print('Australia cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))
    return df    

def get_Colombia():
    df = pd.read_csv('https://raw.githubusercontent.com/sebaxtian/colombia_covid_19_pipe/master/input/covid19co_official.csv')
    df = df.groupby(['fecha reporte web','Departamento o Distrito ']).agg('count')['ID de caso'].unstack().fillna(0).astype(int)
    df.index = pd.to_datetime(df.index)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index.rename('Colombia', inplace=True)
    print('Colombia cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))
    return df    

def get_Pakistan():
    df = pd.read_csv('https://raw.githubusercontent.com/stevenliuyi/covid19/master/data/pakistan-data/pakistan.csv')
    df = df.pivot_table(index='date',columns='province', values='confirmed').diff().fillna(0).astype(int)
    df = df[df.sum().sort_values(ascending=False).index]
    df.index = pd.to_datetime(df.index)
    df.index.rename('Pakistan', inplace=True)
    print('Pakistan cases by state fetched for %s'%df.index[-1].strftime('%Y-%m-%d'))    
    return df   