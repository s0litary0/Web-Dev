from django.urls import path, re_path
import api.views as views

urlpatterns = [
    path('products/', views.get_products),
    re_path(r'^products/(\d+)$', views.get_products_by_id),
    path('categories/', views.get_categories),
    re_path(r'^categories/(\d+)$', views.get_category_by_id),
    re_path(r'categories/(\d+)/products', views.get_products_of_category_by_id)
]