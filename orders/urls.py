from django.urls import path
from . import views

urlpatterns=[
    path('',views.OrderCreateListView.as_view(),name='orders'),
    path('<int:order_id>',views.OrderDetailView.as_view(),name='detail-order'),
    path('update-status/<int:order_id>',views.UpdateOrderStatus.as_view(),name='status-update'),
    path('customer/<int:customer_id>',views.CustomerOrderView.as_view(),name='customer-order'),
]