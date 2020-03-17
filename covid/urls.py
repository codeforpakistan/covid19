"""covid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'provinces', views.ProvinceViewSet)
router.register(r'cities', views.CityViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'source', views.SourceViewSet)
router.register(r'hospitals', views.HospitalViewSet)
router.register(r'genders', views.GenderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index),
    path('api/cases/', views.cases),
    path('api/province_status/', views.province_status),
    path('api/age_gender/', views.age_gender),
    path('api/gender/', views.gender),
    path('api/source/', views.source),
    path('api/status/', views.status),
    path('api/province/', views.province),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]