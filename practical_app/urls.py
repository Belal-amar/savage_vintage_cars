from django.urls import path
from . import views


urlpatterns=[
    path('',views.log_reg,name="log_reg"),
    path('create_user',views.create_user,name="create_user"),
    path('login',views.login,name="login"),
    path('cars',views.success,name="cars"),
    path('cars/<int:id>',views.view,name="view"),
    path("logout",views.logged_out,name="logout"),
    path('cars/new',views.new,name="new"),
    path('post',views.post,name="post"),
    path('cars/edit/<int:id>',views.edit,name="edit"),
    path('cancel',views.cancel,name="cancel"),
    path('cars/<int:id>/delete',views.destroy,name='delete')
]