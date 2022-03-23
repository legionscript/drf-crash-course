from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from catalog import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'albums', views.AlbumViewSet, basename='albums')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('hello-world/', views.hello_world, name='hello-world'),
    path('artists/', views.ArtistView.as_view(), name='artists'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artist-detail'),
]
