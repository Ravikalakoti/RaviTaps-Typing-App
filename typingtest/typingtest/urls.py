from django.urls import path
from core import views

urlpatterns = [
    path('', views.test_selection_view, name='home'),
    path('test/', views.typing_test_view, name='typing-test'),
    path('save-result/', views.save_result, name='save_result'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('my-results/', views.my_results_view, name='my-results'),
    path("certificate/<int:pk>/", views.print_certificate, name="print_certificate"),

]
