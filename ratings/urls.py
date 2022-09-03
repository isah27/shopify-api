from django.urls import path
from . import views

urlpatterns=[
    path('',views.RatinCreationView.as_view(),name='ratings'),
    path('<int:product_id>',views.RatinDetailiew.as_view(),name="specific_rating"),
    
]