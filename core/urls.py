from django.urls import path
from .views import (
    CheckoutView,
    product_view,
    HomeView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
)

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove_from_cart/<slug>', remove_from_cart, name='remove_from_cart'),
    path('remove_item_from_cart/<slug>',
         remove_single_item_from_cart, name='remove_item_from_cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('payment/<payment_option>', PaymentView.as_view(), name='payment'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')

]
