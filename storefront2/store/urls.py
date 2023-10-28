from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
from pprint import pprint

router = SimpleRouter()

router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
pprint(router.urls)

# URLConf
urlpattern = router.urls