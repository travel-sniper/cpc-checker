from django.contrib import admin
from django.urls import path
from cpc_checker import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_cpc_costs', views.get_cpc_costs, name='get_cpc_costs'),
    path('admin/', admin.site.urls),
]
