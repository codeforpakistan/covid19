from django.shortcuts import render
import pandas, json


def index(request):

    df_local = pandas.read_csv('SHEETS.csv', header=1)
    df_local['Date'] = pandas.to_datetime(df_local['Date'], format='%d-%m-%y')

    df_table = df_local[df_local['Date'] == df_local['Date'].max()].groupby('Province').sum()
    df_table = df_table[['Suspected_Cum','Tested_Cum','Confirmed_Cum','Admitted_Cum','Discharged_Cum','Expired_Cum']]

    df_dates = df_local.groupby('Date').sum()

    df_intl = pandas.read_csv('INTL.csv', header=1)
    
    return render(request, 'api/index.html', {
        'summary': dict(df_local.groupby(['Date']).sum().iloc[-1, :][['Suspected_Cum','Tested_Cum','Confirmed_Cum','Admitted_Cum','Discharged_Cum','Expired_Cum']]),
        'table': df_table.to_json(orient='split'),
        'today': df_local['Date'].max().strftime('%d-%m-%Y'),
        'dates': list(df_local['Date'].sort_values().dt.strftime('%d-%m-%Y').unique()),
        'Balochistan': list(df_local[df_local['Province']=='Balochistan'].groupby(['Date']).sum()['Confirmed_Cum']),
        'Pakhtunkhwa': list(df_local[df_local['Province']=='Khyber Pakhtunkhwa'].groupby(['Date']).sum()['Confirmed_Cum']),
        'Punjab': list(df_local[df_local['Province']=='Punjab'].groupby(['Date']).sum()['Confirmed_Cum']),
        'Sindh': list(df_local[df_local['Province']=='Sindh'].groupby(['Date']).sum()['Confirmed_Cum']),
        'Islamabad': list(df_local[df_local['Province']=='Islamabad'].groupby(['Date']).sum()['Confirmed_Cum']),
        'Gilgit': list(df_local[df_local['Province']=='Gilgit-Baltistan'].groupby(['Date']).sum()['Confirmed_Cum']),
        'Kashmir': list(df_local[df_local['Province']=='Azad Kashmir'].groupby(['Date']).sum()['Confirmed_Cum']),
        'Tribal': list(df_local[df_local['Province']=='KP Tribal Districts'].groupby(['Date']).sum()['Confirmed_Cum']),
        'comparison': df_intl.to_json(orient='columns')
    })
