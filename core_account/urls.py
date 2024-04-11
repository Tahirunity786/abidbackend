from django.urls import path
from core_account.views import Profile, Address_Book, Orders, Orders_Cancelation,Orders_Return, Saved
# REST APIs
from core_account.views import UserRegistration, UserLogin, EmailAvailability, Profile, Profile_Viewer, ProfileUpdate

urlpatterns = [
    path('user/profile', Profile.as_view(), name="Profile" ),
    path('user/profile/orders', Orders.as_view(), name="Orders" ),
    path('user/profile/items/saved', Saved.as_view(), name="Saved" ),
    path('user/profile/address-book', Address_Book.as_view(), name="Address" ),
    path('user/profile/order-return', Orders_Return.as_view(), name="Order-return" ),
    path('user/profile/order-cancelation', Orders_Cancelation.as_view(), name="Order-Cencelation" ),


    # REST APIs
    path('account/login-user', UserLogin.as_view(), name="LOGIN"),
    path('create/user', UserRegistration.as_view(), name="REG"),
    path('account/user/available', EmailAvailability.as_view(), name="Available"),
    path('account/user/profile', Profile_Viewer.as_view(), name="profile-view"),
    path('account/user/profile/update', ProfileUpdate.as_view(), name="profile-update-view"),
]
