from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    # path('toggle_switch', views.toggle_switch, name='toggle_switch'),
    path('add-to-cart/<int:id>/<int:productID>', views.addToCart, name='add-to-cart'),
    path('remove-from-cart/<int:id>/<int:itemID>', views.removeFromCart, name='remove-from-cart'),
    path('clear-cart/<int:id>', views.clearCart, name='clear-cart'),
    path('cart/<int:id>', views.cart, name='cart'),
    path('cart/<int:id>/order', views.orderRequest, name='order'),
    path('cart/checkout', views.checkoutCart, name='checkout'),
    path('cart/<int:id>/<int:item_id>/update-cart', views.updateCart, name='update-cart'),
    path('about', views.aboutView, name='about'),
    path('contact', views.contactView, name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
