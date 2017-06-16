from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.getCommCareAuth, name='getCommCareAuth'),
    url(r'^passform/', views.getCommCareFormPass, name='getCommCarePass'),
    url(r'^savecommcaredata/$', views.saveCommCareData, name='saveCommCareData'),
    url(r'^logout/$',views.commcareLogout, name='commcareLogout'),
]