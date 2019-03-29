from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'^$',views.photos_today,name='photosToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastphotos'),
    url(r'^search/', views.search_results, name='search_results'),   
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^photo/image$', views.photo_image, name='photo_image'),   
    url(r'^upload/profile', views.upload_profile, name='upload_profile'),
    url(r'^profile/', views.profile, name='profile'),
 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)