
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from destinations import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('destinations/list/', views.destination_list, name='destination-list'),
    path('destinations/detail/<int:destination_id>/',
         views.destination_detail, name='destination-detail'),
    path('destinations/create/', views.destination_create,
         name='destination-create'),
    path('destinations/update/<int:destination_id>/',
         views.destination_update, name='destination-update'),
    path('destinations/delete/<int:destination_id>/',
         views.destination_delete, name='destination-delete'),
]

if settings.DEBUG:
    '''Uncomment the next line to include your static files'''
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
