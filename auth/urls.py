
from django.urls import path, re_path, include
from .views import success_verify, confirm_email_view

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
    re_path(
        r'^account-confirm-email/(?P<key>[-:\w]+)/$', confirm_email_view,
        name='account_confirm_email',
    ),
    path('success_verify/', success_verify,
         name='account_email_verification_sent',),
]
