from django.urls import path
from . import views

urlpatterns=[
    path('',views.CategoryCreateListView.as_view(),name='category'),
    path('<int:category_id>',views.CategoryDetailView.as_view(),name="detal category"),
    # path('user/<int:vendor_id>/products',views.UserProductView.as_view(),name='vendor_order')
]