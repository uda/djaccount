from django.conf.urls import url
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from .views import AccountView

app_name = 'account'

urlpatterns = [
    url(r'^$', AccountView.as_view(), name='view'),
    url(r'^(?P<pk>\d+)/$', AccountView.as_view(), name='view-one'),
    url(r'^profile/$', AccountView.as_view(), name='profile'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    url(r'^password/change/$', PasswordChangeView.as_view(), name='password-change',
        kwargs={'post_change_redirect': 'account:password-change-done'}),
    url(r'^password/change/done/$', PasswordChangeDoneView.as_view(), name='password-change-done'),
    url(r'^password/reset/$', PasswordResetView.as_view(), name='password-reset',
        kwargs={'post_reset_redirect': 'account:password-reset-done'}),
    url(r'^password/reset/done/$', PasswordResetDoneView.as_view(), name='password-reset-done'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(), name='password-reset-confirm',
        kwargs={'post_reset_redirect': 'account:password-reset-complete'}),
    url(r'^password/reset/complete/$', PasswordResetCompleteView.as_view(), name='password-reset-complete'),
]
