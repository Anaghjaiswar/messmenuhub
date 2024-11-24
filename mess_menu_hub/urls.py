from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/menus/', include('menus.urls')),
    # path('api/users/', include('users.urls')),
    # path('api/feedback/', include('feedback.urls')),
    # path('owners/', include('owners.urls')),
]
