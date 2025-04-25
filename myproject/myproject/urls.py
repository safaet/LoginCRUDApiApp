
from django.contrib import admin
from django.urls import path, include
from myapp.views import StudentApi, LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('student/', StudentApi.as_view()),
    path('login/', LoginAPI.as_view())
]
