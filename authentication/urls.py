from django.urls import path
from . import views
# (?P<year>[0-9]{4})/$
urlpatterns=[
    path('signup/',views.UserCreateView.as_view(),name='sign up'),
    path('login/<str:email>/<str:password>',views.UserLoginView.as_view(),name='login'),
    path('signup/<int:user_id>',views.UserDetailView.as_view(),name='detail'),
]