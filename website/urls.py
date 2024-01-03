from django.urls import path,re_path
from . import views, python_script

urlpatterns = [
    path("", views.website_index, name="website_index"),
    path("post/<int:pk>/", views.website_detail, name="website_detail"),
    path("category/<category>/", views.website_category, name="website_category"),
    re_path(r'^$', python_script.button),
    re_path(r'^output', python_script.output,name="script")

]