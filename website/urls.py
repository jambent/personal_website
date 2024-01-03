from django.urls import path
from . import views

urlpatterns = [
    path("", views.website_index, name="website_index"),
    path("post/<int:pk>/", views.website_detail, name="website_detail"),
    path("category/<category>/", views.website_category, name="website_category"),
]