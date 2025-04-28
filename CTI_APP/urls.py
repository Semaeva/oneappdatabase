from django.urls import path
from django.contrib.auth import views as auth_views  # Импортируем auth_views для стандартных представлени
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('', views.cti_list, name='cti_list'),
    path('log/<int:log_id>/', views.cti_detail, name='cti_detail'),
    path('search/', views.ctilog_search, name='ctilog_search'),
    path('create/', views.cti_create, name='cti_create'),
    path('ip/', views.block_ip, name='ip'),  # Добавьте URL для /ip
    path('url/', views.url_ip, name='url'),  # Добавьте URL для /ip
    path('export-cti-logs-csv/', views.export_cti_logs_to_csv, name='export_cti_logs_csv'),
    path('export_block_ip_csv/', views.export_block_ip_csv, name='export_block_ip_csv'),
    path('export_url_csv/', views.export_url_csv, name='export_url_csv'),


    # Стандартные URL для входа и выхода
    path('accounts/logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/password_change/', PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    # jwt auth
    path("api/token/get", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify", TokenVerifyView.as_view(), name="token_verify"),
]
