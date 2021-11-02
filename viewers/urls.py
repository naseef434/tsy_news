from django.urls import path

from tsynews import settings
from . import views


app_name = 'viewers'


urlpatterns = (
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('kerala/',views.kerala,name='kerala'),
    path('gulf/',views.gulf,name='gulf'),
    path('local/',views.local,name='local'),
    path('latest/',views.latest,name='latest'),
    path('international/',views.internation,name='international'),
    path('sports/',views.sports,name='sports'),
    path('more/',views.more,name='more'),
    path('news_view/<int:id>/',views.news_view,name='news_view'),
    path('about/', views.about,name='about'),
)
