from django.urls import path
from core_control.views import Private_Plate, Faqs, Plate_Detail, Cart, Contact

urlpatterns = [
    path('private-plate/faq', Faqs.as_view(), name="Faqs"),
    path('private-plate/cart', Cart.as_view(), name="Cart"),
    path('private-plate/contact', Contact.as_view(), name="Contact"),
    path('private-plate/explore', Private_Plate.as_view(), name="Explore"),
    path('private-plate/number-plate/detail', Plate_Detail.as_view(), name="Details"),
]
