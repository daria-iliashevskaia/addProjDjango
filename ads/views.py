from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Ads, User, Location, Selections
from ads.permissions import SelectionsUpdatePermission, AdsUpdatePermission
from ads.serializers import CategorySerializer, AdsSerializer, UserSerializer, LocationSerializer, SelectionsSerializer, \
    SelectionsCreateSerializer


def index(request):
    response = {"status": "ok"}
    return JsonResponse(response, status=200)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdsListView(ListAPIView):

    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

    def get(self, request, *args, **kwargs):
        category_id = request.GET.get('cat', None)
        if category_id:
            self.queryset = self.queryset.filter(id__exact=category_id)

        ads_name = request.GET.get('text', None)
        if ads_name:
            self.queryset = self.queryset.filter(name__icontains=ads_name)

        location_name = request.GET.get('location', None)
        if location_name:
            self.queryset = self.queryset.filter(author__location__name__icontains=location_name)

        if request.GET.get("price_from", None):
            self.queryset = self.queryset.filter(price__gte=request.GET.get("price_from"))

        if request.GET.get("price_to", None):
            self.queryset = self.queryset.filter(price__lte=request.GET.get("price_to"))
        return super().get(request, *args, **kwargs)


class AdsDetailView(RetrieveAPIView):

    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    # permission_classes = [IsAuthenticated]


class AdsCreateView(CreateAPIView):

    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    # permission_classes = [IsAuthenticated]


class AdsUpdateView(UpdateAPIView):

    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated, AdsUpdatePermission]


class AdsDeleteView(DestroyAPIView):

    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated, AdsUpdatePermission]


class UserListView(ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(DestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class SelectionsListView(ListAPIView):

    queryset = Selections.objects.all()
    serializer_class = SelectionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SelectionsDetailView(RetrieveAPIView):

    queryset = Selections.objects.all()
    serializer_class = SelectionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SelectionsCreateView(CreateAPIView):

    queryset = Selections.objects.all()
    serializer_class = SelectionsCreateSerializer
    # permission_classes = [IsAuthenticated]


class SelectionsUpdateView(UpdateAPIView):

    queryset = Selections.objects.all()
    serializer_class = SelectionsCreateSerializer
    permission_classes = [IsAuthenticated, SelectionsUpdatePermission]


class SelectionsDeleteView(DestroyAPIView):

    queryset = Selections.objects.all()
    serializer_class = SelectionsSerializer
    permission_classes = [IsAuthenticated, SelectionsUpdatePermission]
