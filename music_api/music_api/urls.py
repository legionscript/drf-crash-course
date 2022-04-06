from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from catalog import views
from rest_framework.schemas import get_schema_view
from django.views.generic.base import TemplateView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'albums', views.AlbumViewSet, basename='albums')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('hello-world/', views.hello_world, name='hello-world'),
    path('artists/', views.ArtistView.as_view(), name='artists'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artist-detail'),
    path(r'openapi-schema', get_schema_view(
        title="Music API",  # Title of your app
        description="Music catalog API",  # Description of your app
        version="1.0.0",
        public=True,
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='catalog/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
        ), name='swagger-ui')

]
