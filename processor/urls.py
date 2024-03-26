
from django.contrib import admin
from django.urls import path, include
from processor.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="Home"),
    path('aqib-plaltes/',include('core_control.urls')),
    path('aqib-plaltes/',include('core_account.urls')),

]
