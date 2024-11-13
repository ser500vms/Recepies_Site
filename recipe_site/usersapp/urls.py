from django.urls import path, reverse_lazy
from .views import (
    HomeView,
    RegistrationView,
    LkView,
    MyLoginView,
    MyLogoutView,
    AboutUserView,
    UserDeleteView,
    UserUpdateView,
    UserPasswordChangeView,
    UserPasswordResetView,
    UserPasswordResetDoneView,
    UserPasswordResetConfirmView,
    UserPasswordResetCompleteView

)



urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('reg/', RegistrationView.as_view(), name='registration_page'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('user/change-password/', UserPasswordChangeView.as_view(), name='password_change'),

    path('password-reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('password-reset/complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('lk/<int:pk>/', LkView.as_view(), name='lk_page'),
    path('user-info/<int:pk>/', AboutUserView.as_view(), name='user_info'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='update_user'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='delete_user'),
]