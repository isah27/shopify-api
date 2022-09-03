from django.urls import path
from . import views

urlpatterns=[
    path('',views.ProductCreateListView.as_view(),name='products'),
    path('<int:product_id>',views.ProductDetailView.as_view(),name="specific_product"),
    path('user/<int:vendor_id>/products',views.UserProductView.as_view(),name='vendor_order')
]