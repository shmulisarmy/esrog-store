from django.urls import path

from . import views

from .interfaces import actions, apis
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('all_esrog_data', apis.main),
    path('price_filter/<int:min_price>/<int:max_price>', apis.price_filter),

    path('', views.main),


    #posts
    path('reserve', actions.reserve),






]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)