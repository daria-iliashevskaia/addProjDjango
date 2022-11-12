import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from addProj import settings
from ads.models import Category, Ads, User, Location


def index(request):
    response = {"status": "ok"}
    return JsonResponse(response, status=200)


class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        """
        Возвращает список категорий в JSON формате
        """

        category = Category.objects.all()

        category = category.order_by("name")

        response = []

        for cat in category:
            response.append({
                "id": cat.id,
                "name": cat.name
            })

        return JsonResponse(response, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        """
        Возвращает карточку выбранной категории в JSON формате
        """

        try:
            category = self.get_object()
        except Http404:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]
    success_url = 'cat/'

    def post(self, request, *args, **kwargs):
        """
        Принимает POST запрос на добавление новой категории
        """

        cat_data = json.loads(request.body)

        category = Category.objects.create(name=cat_data['name'])

        return JsonResponse({"id": category.id,
                             "name": category.name
                             })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        """
        Принимает PATCH запрос на добавление новой категории
        """

        super().post(request, *args, **kwargs)

        cat_data = json.loads(request.body)

        self.object.name = cat_data['name']
        self.object.save()

        return JsonResponse({"id": self.object.id,
                             "name": self.object.name
                             })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = 'cat/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


class AdsListView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        """
        Возвращает список объявлений в JSON формате
        """

        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.select_related("author").select_related("category").order_by("-price")

        paginator = Paginator(self.object_list, 5)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)


        response = []

        for ad in page_obj:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "image": ad.image.url if ad.image else None,
                "author": ad.author.first_name,
                "category": ad.category.name
            })

        return JsonResponse(response, safe=False)


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        """
        Возвращает карточку выбранного объявления в JSON формате
        """

        try:
            ad = self.get_object()
        except Http404:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,
            "author": ad.author.first_name,
            "category": ad.category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdsCreateView(CreateView):
    model = Ads
    fields = ["name", "price", "description", "image", "author", "category"]

    def post(self, request, *args, **kwargs):
        """
        Принимает POST запрос на добавление нового объявления
        """

        ads_data = json.loads(request.body)

        ads = Ads.objects.create(
                  name=ads_data['name'],
                  price=ads_data['price'],
                  description=ads_data['description'],
                  image=ads_data['image'],
                  author_id=ads_data['author'],
                  category_id=ads_data['category']
                  )

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "price": ads.price,
            "description": ads.description,
            'image': ads.image.url,
            "author": ads.author.first_name,
            "is_published": ads.is_published,
            "category": ads.category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdsUpdateView(UpdateView):
    model = Ads
    fields = ["name", "price", "description", "image", "author", "category"]

    def patch(self, request, *args, **kwargs):
        """
        Принимает PATCH запрос на изменение объявления
        """

        super().post(request, *args, **kwargs)

        ads_data = json.loads(request.body)

        self.object.name = ads_data['name']
        self.object.price = ads_data['price']
        self.object.description = ads_data['description']
        self.object.image = ads_data['image']
        self.object.category_id = ads_data['category']

        self.object.save()

        return JsonResponse({
                    "id": self.object.id,
                    "name": self.object.name,
                    "price": self.object.price,
                    "description": self.object.description,
                    'image': self.object.image.url,
                    "author": self.object.author.first_name,
                    "is_published": self.object.is_published,
                    "category": self.object.category.name
                    })


@method_decorator(csrf_exempt, name='dispatch')
class AdsDeleteView(DeleteView):
    model = Ads
    success_url = 'ad/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsImageView(UpdateView):
    model = Ads
    fields = ["image"]

    def patch(self, request, *args, **kwargs):

        self.object = self.get_object()
        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
                            "id": self.object.id,
                            "name": self.object.name,
                            "price": self.object.price,
                            "description": self.object.description,
                            'image': self.object.image.url,
                            "author": self.object.author.first_name,
                            "is_published": self.object.is_published,
                            "category": self.object.category.name
                         })


class UserListView(ListView):

    model = User

    def get(self, request, *args, **kwargs):
        """
        Возвращает список юзеров в JSON формате
        """

        users = User.objects.annotate(total_ads=Count('ads', filter=Q(ads__is_published=True)))

        paginator = Paginator(users, 5)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)

        response = []

        for user in page_obj:
            response.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "password": user.password,
                "role": user.role,
                "age": user.age,
                "location": list(user.location.all().values_list("name", flat=True)),
                "total_ads": user.total_ads
            })

        return JsonResponse(response, safe=False)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        """
        Возвращает карточку выбранного юзера в JSON формате
        """

        try:
            user = self.get_object()
        except Http404:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "age": user.age,
            "location": list(user.location.all().values_list("name", flat=True))
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ["first_name", "last_name", "username", "password", "role", "age", "location"]

    def post(self, request, *args, **kwargs):
        """
        Принимает POST запрос на добавление нового юзера
        """

        user_data = json.loads(request.body)

        user = User.objects.create(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            username=user_data['username'],
            password=user_data['password'],
            role=user_data['role'],
            age=user_data['age']
        )

        for location in user_data["location"]:
            try:
                location_obj = Location.objects.get(name=location)
            except Location.DoesNotExist:
                location_obj = Location(name=location)
                location_obj.save()

        user.location.add(location_obj)
        user.save()



        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "age": user.age,
            "location": list(user.location.all().values_list("name", flat=True))
        })

@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ["first_name", "last_name", "username", "password", "role", "age", "location"]

    def patch(self, request, *args, **kwargs):
        """
        Принимает PATCH запрос на изменение данных юзера
        """
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)

        self.object.first_name=user_data['first_name']
        self.object.last_name=user_data['last_name']
        self.object.username=user_data['username']
        self.object.password=user_data['password']
        self.object.role=user_data['role']
        self.object.age=user_data['age']


        for location in user_data["location"]:
            try:
                location_obj = Location.objects.get(name=location)
            except Location.DoesNotExist:
                location_obj = Location(name=location)
                location_obj.save()

        self.object.location.add(location_obj)
        self.object.save()


        return JsonResponse({
            "id": self.object.id,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "username": self.object.username,
            "password": self.object.password,
            "role": self.object.role,
            "age": self.object.age,
            "location": list(self.object.location.all().values_list("name", flat=True))
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = 'user/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)