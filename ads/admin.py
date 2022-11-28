from django.contrib import admin

from ads.models import Category, Ads, User, Location, Selections

admin.site.register(Category)
admin.site.register(Ads)
admin.site.register(User)
admin.site.register(Location)
admin.site.register(Selections)
