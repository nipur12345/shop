from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='ShopHome'),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="Contactus"),
    path("tracker/",views.trackeer,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("products/<int:myid>",views.prodView,name="Search"),
    path("checkout/",views.checkout,name="Checkout"),
    path("clearCart/",views.clearCart,name="ClearCart"),
    # path("handlerequest/", views.handlerequest, name="HandleRequest")
]

