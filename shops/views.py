from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop


longitude = 43.252077
latitude = 76.947657

user_location = Point(longitude, latitude, srid=4326)


class ShopList(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(
        distance=Distance('location', user_location)
    ).order_by('distance')[0:6]
    template_name = 'shops/index.html'
