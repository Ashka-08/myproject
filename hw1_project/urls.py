from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw1/', include('hw1_app.urls')),
    path('hw2/', include('hw2_app.urls')),
    path('hw3/', include('hw3_app.urls')),
    path('hw4/', include('hw4_app.urls')),
    path('hw5/', include('hw5_app.urls')),
    path('', include('hw6_app.urls')),
]
