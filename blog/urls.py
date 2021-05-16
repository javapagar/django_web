from django.urls import path
from . import views

urlpatterns = [
    path("",views.posts_list,name="posts_list"),
    path("<int:pk>/",views.detalle_post,name="detalle_post"),
    path("<category>/",views.post_category,name="post_category")
]