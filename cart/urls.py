from django.urls import path
from . import views

urlpatterns=[
    path('',views.CartCreateListView.as_view(),name='cart'),
    path('remove-cart/<int:cart_id>',views.CartDetailView.as_view(),name='delete-cart'),
    path('update/cart-quantity/<int:cart_id>',views.UpdateQuantityView.as_view(),name='update-cart-quantity'),
]