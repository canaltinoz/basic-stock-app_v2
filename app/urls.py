from django.urls import path,include
from app import views

urlpatterns = [
    path('index',views.home,name='home'),
    path('signup/',views.signup,name='user_signup'),
    path('login/',views.login_view,name='user_login'),
    path('logout/', views.user_logout, name="user_logout"),
    path('user-details/', views.user_details, name="user_details"),
    path('borrow/', views.flavour_transaction, name='flavour_transaction'),
    path('add-flavour/', views.add_flavour, name='add_flavour'),
    path('list-flavour/', views.list_flavour, name='list_flavour'),
    path('delete/<id>',views.delete,name='delete')

    
]
