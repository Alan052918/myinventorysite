from django.urls import path

from inventories import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:sku>/", views.detail, name="detail"),
]
