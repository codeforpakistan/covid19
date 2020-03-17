from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions
from api import models, serializers
from django.db import connection
import pandas

@api_view(('GET',))
def index(request):
    return Response(data='COVID19 Dashboard API')


query = "select ap.age as 'Age', ac.name as 'City', apr.name as 'Province', ag.name as 'Gender', ast.name as 'Status', aso.name as 'Source'  from api_patient ap\
        join api_city ac on ac.id = ap.city_id\
        join api_province apr on apr.id = ap.province_id\
        join api_gender ag on ag.id = ap.gender_id\
        join api_status as ast on ast.id = ap.status_id\
        join api_source as aso on aso.id = ap.source_id\
        join api_hospital as ah on ah.id = ap.hospital_id"

@api_view()
@permission_classes([IsAuthenticated])
def cases(request):
    df = pandas.read_sql(query, connection)
    return Response(df.to_json(orient='columns'))

@api_view()
@permission_classes([IsAuthenticated])
def province_status(request):
    df = pandas.read_sql(query, connection)
    df = pandas.crosstab(df['Province'], df['Status'])
    return Response(df.to_json(orient='columns'))

@api_view()
@permission_classes([IsAuthenticated])
def map(request):
    df = pandas.read_sql(query, connection)
    c = df.groupby('Province').size()
    return Response(c)

@api_view()
@permission_classes([IsAuthenticated])
def age_gender(request):
    df = pandas.read_sql(query, connection)
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    labels = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100']
    df['binned'] = pandas.cut(df['Age'], bins=bins, labels=labels)
    df = pandas.crosstab(df.binned, df.Gender)
    return Response(df.to_json(orient='columns'))


@api_view()
@permission_classes([IsAuthenticated])
def status(request):
    df = pandas.read_sql(query, connection)
    return Response(dict(pandas.value_counts(df['Status'])))


@api_view()
@permission_classes([IsAuthenticated])
def gender(request):
    df = pandas.read_sql(query, connection)
    return Response(dict(pandas.value_counts(df['Gender'])))


@api_view()
@permission_classes([IsAuthenticated])
def source(request):
    df = pandas.read_sql(query, connection)
    return Response(dict(pandas.value_counts(df['Source'])))

@api_view()
@permission_classes([IsAuthenticated])
def province(request):
    df = pandas.read_sql(query, connection)
    hist = dict(pandas.value_counts(df['Province'], normalize=True))
    hist.update((x, int(y*100)) for x, y in hist.items())
    return Response(hist)


@api_view()
@permission_classes([IsAuthenticated])
def query(request):
    df = pandas.read_csv('SHEETS.csv', header=1)
    df['Date'] = pandas.to_datetime(df['Date'], format='%d-%m-%y')

    if (request.GET):
        if 'date' in request.GET:
            df = df[df['Date'] == request.GET.get('date')]
        if 'province' in request.GET:
            df = df[df['Province'] == request.GET.get('province')]
        if 'groupby' in request.GET:
            df = df.groupby([request.GET.get('groupby')])

        if 'measure' in request.GET:
            if 'aggregate' in request.GET:
                aggregate = request.GET.get('aggregate')
                if aggregate == 'Sum':
                    df = df.sum()[request.GET.get('measure')]
                elif aggregate == 'Mean':
                    df = df.mean()[request.GET.get('measure')]
                else:
                    return Response('Invalid aggregate method', status=400)
            else: 
                return Response('No aggregate selected', status=400)
        else:
            return Response('No measure selected', status=400)

        if 'groupby' in request.GET:
            if request.GET.get('groupby') == 'Date':
                return Response({x.strftime("%Y-%m-%d"):y for (x,y) in dict(df).items()})
            else:
                return Response(dict(df))
        else:
            return Response(df)

    return Response('No inputs provided', status=400)
    

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer
    permission_classes = [permissions.IsAuthenticated]


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    permission_classes = [permissions.IsAuthenticated]


class StatusViewSet(viewsets.ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class SourceViewSet(viewsets.ModelViewSet):
    queryset = models.Source.objects.all()
    serializer_class = serializers.SourceSerializer
    permission_classes = [permissions.IsAuthenticated]


class GenderViewSet(viewsets.ModelViewSet):
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderSerializer
    permission_classes = [permissions.IsAuthenticated]


class LaboratoryViewSet(viewsets.ModelViewSet):
    queryset = models.Laboratory.objects.all()
    serializer_class = serializers.LaboratorySerializer
    permission_classes = [permissions.IsAuthenticated]
