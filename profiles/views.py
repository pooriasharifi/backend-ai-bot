from .models import Profiles
from .serializers import ProfileSerializerV1,ProfileSerializerV2
from rest_framework import generics
from misc.custom_generic_views import PartialUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from misc.custom_permissions import IsOwner


# Create your views here.



from rest_framework.reverse import reverse

class ProfileView(generics.ListCreateAPIView):
    # serializer_class = ProfileSerializer
    queryset = Profiles.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if  self.request.version == 'v1':
            return ProfileSerializerV1
        elif self.request.version=='v2':
            return ProfileSerializerV2

    def get(self, request, *args, **kwargs):

        return super(ProfileView, self).get(request, *args, **kwargs)


class ProfileRetrive(PartialUpdateAPIView):
    serializer_class = ProfileSerializerV1
    queryset = Profiles.objects.all()
    permission_classes = (IsOwner,)
