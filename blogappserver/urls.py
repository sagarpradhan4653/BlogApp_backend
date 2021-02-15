from rest_framework import routers
from django.urls import include, path
from . import views






router = routers.DefaultRouter()
router.register(r'bloggers',views.BloggerViewSet)
router.register(r'users',views.UserViewSet)


urlpatterns = [
    path('details/',views.getDetails,name="getDetails"),
    path('',include(router.urls)),
    # path('api-auth/',include('rest_framework.urls',namespace= 'rest_framework'))
    path('api-auth/',views.CustomAuthToken.as_view())



]

