from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('set_budget/', views.set_budget, name='set_budget'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('expense/<int:pk>/delete/', views.delete_expense, name='delete_expense'),
    path('edit_expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),


    path('set_budget/', views.set_budget, name='set_budget'),
    path('update_budget/', views.update_budget, name='update_budget'),
    path('delete_budget/', views.delete_budget, name='delete_budget'),

    path('download/', views.download_records, name='download_records'),
]
