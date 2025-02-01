from django.contrib import admin
from django.urls import path, include
from reports.views import report_violation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('report/', report_violation, name="report_violation"),
    path('', include('reports.urls')),
]
