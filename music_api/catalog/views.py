from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication
from catalog.serializers import UserSerializer, ArtistSerializer, AlbumSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets
from .models import Artist, Album

class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited
	"""

	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.AllowAny]

class OncePerDayUserThrottle(UserRateThrottle):
	rate = '1/day'

@api_view(['GET', 'POST'])
@throttle_classes([OncePerDayUserThrottle])
def hello_world(request):
	if request.method == 'POST':
		print(request.data)
		return Response({'message': 'Got some data: ' + str(request.data)})
	return Response({'message': 'hello world!'})

# class ArtistView(APIView):
# 	authentication_classes = [authentication.TokenAuthentication]
# 	permisson_classes = [permissions.IsAuthenticated]
# 	throttle_classes = [OncePerDayUserThrottle]

# 	def get(self, request):
# 		artists = Artist.objects.all()
# 		return Response(artists)
# 	def post(self, request):
# 		return Response({'data': request.data})

# GenericAPIView
# /artists/
# Creating new artists, listing out all artists
class ArtistGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer
	permission_classes = [permissions.AllowAny]

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

# /artists/<pk>/
# retrieve the object by id, update the object by id, delete object by id
class ArtistDetailGenericView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

class ArtistView(ListCreateAPIView):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer
	permission_classes = [permissions.AllowAny]

class ArtistDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
	# queryset = Album.objects.all()
	serializer_class = AlbumSerializer

	def get_queryset(self):
		return Album.objects.all()
