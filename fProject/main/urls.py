from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path('items', views.product_list, name='product_list'),
    path('items/<slug:category_slug>/', views.product_list, name="product_list_by_category"),
    path('items/<str:nameFilter>/', views.product_list, name="product_filtered"),
    path('items/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('items/create', views.create, name='add_product'),
    path('items/update/<int:pk>', views.update, name='update_product'),
    path(r'^items/del/(?P<pk>\d+)/$', views.delete, name='delete_product')
]