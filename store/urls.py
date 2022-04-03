from django.urls import path
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewSet, basename='cart-items')

# URLConf
urlpatterns = router.urls + product_router.urls + cart_router.urls
# urlpatterns = [
    # path('products/', views.product_list),
    # path('products/', views.ProductList.as_view()),
    # path('products/<int:id>/', views.product_detail),
    # path('products/<int:pk>/', views.ProductDetail.as_view()),
    # path('collections/', views.collection_list),
    # path('collections/', views.CollectionList.as_view()),
    # path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),
    # path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
# ]
