import json

from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ads


def index(request):
    response = {"status": "ok"}
    return JsonResponse(response, status=200)


def insert_categories(request):
    with open("category.json", 'r', encoding='utf-8') as f:
        categories = json.load(f)

    for cat in categories:
        category = Category(name=cat['name'])
        category.save()


def insert_ads(request):
    with open("ads.json", 'r', encoding='utf-8') as f:
        ads = json.load(f)

    for i in ads:
        ad = Ads(name=i['name'],
                 author=i['author'],
                 price=i['price'],
                 description=i['description'],
                 address=i['address']
                 )
        ad.save()


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):

    def get(self, request):
        if request.method == "GET":
            category = Category.objects.all()

            response = []

            for cat in category:
                response.append({
                    "id": cat.id,
                    "name": cat.name
                })

            return JsonResponse(response, safe=False)

    def post(self, request):
        if request.method == "POST":
            cat_data = json.loads(request.body)

            category = Category(name=cat_data['name'])
            category.save()

            return JsonResponse({"id": category.id,
                                 "name": category.name
                                 })

@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):

    def get(self, request):
        ads = Ads.objects.all()

        response = []

        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        if request.method == "POST":
            ads_data = json.loads(request.body)

            ads = Ads(name=ads_data['name'],
                      author=ads_data['author'],
                      price=ads_data['price'],
                      description=ads_data['description'],
                      address=ads_data['address']
                      )
            ads.save()

            return JsonResponse({
                "id": ads.id,
                "name": ads.name,
                "author": ads.author,
                "price": ads.price,
                "description": ads.description,
                "address": ads.address,
                "is_published": ads.is_published
                })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Http404:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            ads = self.get_object()
        except Http404:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })


