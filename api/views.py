from django.contrib.auth.models import User, Group
from django.core.management import call_command
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle
from django.shortcuts import render
from django.conf import settings
import os, pandas, numpy, json


def index(request):

    df_local = pandas.read_csv('SHEETS.csv', header=1)
    df_local['Date'] = pandas.to_datetime(df_local['Date'], format='%d-%m-%y')

    df_table = df_local[df_local['Date'] == df_local['Date'].max()].groupby('Province').sum()
    df_table = df_table[['Suspected_Cum','Tested_Cum','Confirmed_Cum','Admitted_Cum','Discharged_Cum','Expired_Cum']]

    df_dates = df_local.groupby('Date').sum()

    df_intl = pandas.read_csv('INTL.csv', header=1)
    
    return render(request, 'api/index.html', {
        'summary': dict(df_local.groupby(['Date']).sum().iloc[-1, :][['Suspected_Cum','Tested_Cum','Confirmed_Cum','Admitted_Cum','Discharged_Cum','Expired_Cum']]),

        'epiDailyCases': list(df_local.groupby('Date').sum()['Confirmed_24']),
        'epiDailyDeaths': list(df_local.groupby('Date').sum()['Expired_24']),
        
        'epiTotalCases': list(df_local.groupby('Date').sum()['Confirmed_Cum']),
        'epiTotalDeaths': list(df_local.groupby('Date').sum()['Expired_Cum']),
        
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
        # 'Tribal': list(df_local[df_local['Province']=='KP Tribal Districts'].groupby(['Date']).sum()['Confirmed_Cum']),
        'comparison': df_intl.to_json(orient='columns')
    })


class TenPerDayThrottle(UserRateThrottle):
    rate = '10/day'


@api_view()
@permission_classes([IsAuthenticated])
def summary(request):
    with open(os.path.join(settings.STATIC_ROOT, 'summary.json'), 'r') as infile:
        output = json.load(infile)

    return Response(data=output)

@api_view()
@permission_classes([IsAdminUser])
@throttle_classes([TenPerDayThrottle])
def compile(request):

    call_command('sheets')
    call_command('comparison')

    df = pandas.read_csv('SHEETS.csv', header=1)
    df['Date'] = pandas.to_datetime(df['Date'], format='%d-%m-%y')
    df.fillna(0, inplace=True)
    df = df[df['Province'] != 'KP Tribal Districts']

    df_total = df.rename(columns={ 'Suspected_Cum': 'Suspected', 'Tested_Cum': 'Tested', 'Confirmed_Cum': 'Confirmed', 'Admitted_Cum': 'Admitted', 'Discharged_Cum': 'Discharged', 'Expired_Cum': 'Expired' })
    df_today = df.rename(columns={ 'Suspected_24': 'Suspected', 'Tested_24': 'Tested', 'Confirmed_24': 'Confirmed', 'Admitted_24': 'Admitted', 'Discharged_24': 'Discharged', 'Expired_24': 'Expired' })

    output = {
        'updated': df['Date'].max().strftime('%d-%m-%Y'),
        'total': dict(df_total.groupby(['Date']).sum().iloc[-1, :][['Suspected','Tested','Confirmed','Admitted','Discharged','Expired']].astype(int)),
        'today': dict(df_today.groupby(['Date']).sum().iloc[-1, :][['Suspected','Tested','Confirmed','Admitted','Discharged','Expired']].astype(int)),
        'province_total': dict(pandas.pivot_table(df, values='Confirmed_Cum', index=df['Date'], columns=df['Province'], aggfunc='sum').iloc[-1, :].astype(int))
    }

    with open(os.path.join(settings.STATIC_ROOT, 'summary.json'), 'w') as outfile:
        json.dump(output, outfile, cls=IntEncoder)

    return Response(data='JSON Compiled', status=status.HTTP_201_CREATED)


class IntEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super(IntEncoder, self).default(obj)