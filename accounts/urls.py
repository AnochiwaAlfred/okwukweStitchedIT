<<<<<<< HEAD
from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
    path('subscribe', views.subscribeView, name='subscribe'),
    path('profile', views.profileView, name='profile'),

    # path('add-user', views.addUser, name='add-user'),
    # path('add-user/add', views.add, name='add'),
    # path('delete-user/<int:id>', views.deleteUser, name='delete-user'),
    # path('delete-user/delete/<int:id>', views.delete, name='delete'),
    # path('edit-user/<int:id>', views.editUser, name='edit-user'),
    # path('edit-user/<int:id>/edit', views.edit, name='edit'),
    # path('cancel', views.cancel, name='cancel'),
    # path('details/<int:id>', views.details, name='details'),
=======
from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
    path('subscribe', views.subscribeView, name='subscribe'),
    path('profile', views.profileView, name='profile'),

    # path('add-user', views.addUser, name='add-user'),
    # path('add-user/add', views.add, name='add'),
    # path('delete-user/<int:id>', views.deleteUser, name='delete-user'),
    # path('delete-user/delete/<int:id>', views.delete, name='delete'),
    # path('edit-user/<int:id>', views.editUser, name='edit-user'),
    # path('edit-user/<int:id>/edit', views.edit, name='edit'),
    # path('cancel', views.cancel, name='cancel'),
    # path('details/<int:id>', views.details, name='details'),
>>>>>>> 4a8e8a410c304b57e382320e48a01d181f4dd41f
]