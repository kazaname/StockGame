from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from .views import UserSignUpView, activate

app_name = 'account'

urlpatterns = [
    path('register', UserSignUpView.as_view(), name='register'),
    path('login', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('activate/<uidb64>[0-9A-Za-z_\-]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/', activate, name='activate'),

    path('password-reset', auth_views.PasswordResetView.as_view(
                                                    template_name='account/password_reset_form.html',
                                                    email_template_name='account/password_reset_email.html',
                                                    success_url=reverse_lazy('account:password_reset_done')
                                                    ),
                                                    name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
                                                    template_name='account/password_reset_done.html'),
                                                    name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
                                                    template_name='account/password_reset_confirm.html',
                                                    success_url=reverse_lazy('account:password_reset_complete')
                                                    ),
                                                    name='password_reset_confirm'),
    path('password-reset/complete', auth_views.PasswordResetCompleteView.as_view(
                                                    template_name='account/password_reset_complete.html'
    ),
                                                    name='password_reset_complete'),
]
