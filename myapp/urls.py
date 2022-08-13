"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>', views.home, name='home'),
    path('events', views.eventview, name='events'),
    path('addvenue', views.addvenueview, name='addvenue'),
    path('venues', views.venuelistview, name='venuelist'),
    path('venuedetail/<venue_id>', views.venuedetailview, name='venuedetail'),
    path('eventdetail/<event_id>', views.eventdetailview, name="eventdetail"),
    path('searchvenue', views.searchvenueview, name='searchvenue'),
    path('updatevenue/<venue_id>', views.updatevenueview, name='updatevenue'),
    path('deletevenue/<venue_id>', views.deletevenueview, name='deletevenue'),
    path('venuetext', views.venuetext, name='venuetext'),
    path('venuecsv', views.venuecsv, name='venuecsv'),
    path('venuepdf', views.venuepdf, name='venuepdf'),
    path('addevent', views.addeventview, name='addevent'),
    path('editevent/<event_id>', views.editeventview, name='editevent'),
    path('searchevent', views.searcheventview, name="searchevent"),
    path('adminapproval', views.adminpprovalview, name="adminapproval"),
    path('eventvenuecategory/<venue_id>', views.eventvenuecategoryview, name="eventvenuecategory"),
    
]
