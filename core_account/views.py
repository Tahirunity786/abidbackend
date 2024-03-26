from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Profile(TemplateView):

    template_name = 'core_account/account.html'

    def get(self, request):

        return render(request, self.template_name)
    

class Address_Book(TemplateView):

    template_name = 'core_account/accounts/address-book.html'

    def get(self, request):

        return render(request, self.template_name)
    

class Orders(TemplateView):

    template_name = 'core_account/accounts/order.html'

    def get(self, request):

        return render(request, self.template_name)
    

class Orders_Cancelation(TemplateView):

    template_name = 'core_account/accounts/order_cancelation.html'

    def get(self, request):

        return render(request, self.template_name)
    

class Orders_Return(TemplateView):

    template_name = 'core_account/accounts/order-returns.html'

    def get(self, request):

        return render(request, self.template_name)


class Saved(TemplateView):

    template_name = 'core_account/accounts/saved.html'

    def get(self, request):

        return render(request, self.template_name)