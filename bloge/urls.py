from django.urls import path
from .views import post_list , post_details , new_post , post_delete 






app_name='bloge'

urlpatterns = [
    path('',post_list),
    path('<int:post_id>',post_details,name='post'),
    path('newpost',new_post,name='new'),
    path('<int:post_id>/delete',post_delete,name='post_delete'),




]


