from . import views
from django.urls import path
from .views import getAllEmployees,add_employee_view,update_user,add_holiday
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'api'

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name="register"),
    path('login/',views.LoginAPIView.as_view(),name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('send-otp/', views.send_otp, name='send-otp'),
    path('confirm-otp/', views.confirm_otp, name='confirm-otp'),
    path('reset-password/', views.reset_password_view, name='reset-password'),
    path('add-employee/', add_employee_view, name='add-employee'),
    path('get_all_employees/',getAllEmployees, name = 'getAllEmployees'),
    path('update_user/',update_user, name="update_user"),
    path('deactivate_user/',views.deactivate_user, name="deactivate_user"),
    path('users/', views.user_detail_view, name='user-detail'),
    path('add_leave/', views.add_leave, name='add_leave'),
    path('leave_history/', views.get_leave_history, name='leave_history'),
    path('add_holiday/', add_holiday, name='add-holiday'),
    path('get_holidays/', views.get_holidays, name='get-holidays'),
    path('punch-in/',views.punch_in_view, name = "punch_in"), # added by Nageswara and Saikiran
    path('punch-out/',views.punch_out_view,name= "punch_out"), # added by D Hari
    path('upload_profilePic/',views.profilePicApi,name= "profilePicApi"),
]
