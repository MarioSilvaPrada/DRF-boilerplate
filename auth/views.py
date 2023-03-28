from django.views.generic import TemplateView
from allauth.account.views import ConfirmEmailView
from rest_framework.permissions import AllowAny


class SuccessVerifyView(TemplateView):
    template_name = 'account/success_verification.html'


success_verify = SuccessVerifyView.as_view()


class CustomConfirmEmailView(ConfirmEmailView, TemplateView):
    permission_classes = [AllowAny]
    template_name = 'account/email_confirm.html'


confirm_email_view = CustomConfirmEmailView.as_view()
