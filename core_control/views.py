from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from core_control.models import Product

# Create your views here.

class Login(TemplateView):

    template_name = 'core_control/login.html'

    def get(self, request):

        return render(request, self.template_name)
    



class Register(TemplateView):
    template_name = 'core_control/form.html'

    def get(self, request):
        # Render the registration form
        return render(request, self.template_name)


class Plate_Detail(TemplateView):

    template_name = 'core_control/product-detail.html'

    def get(self, request):

        return render(request, self.template_name)
    
class Cart(TemplateView):

    template_name = 'core_control/cart.html'

    def get(self, request):

        return render(request, self.template_name)
    

class Private_Plate(TemplateView):

    template_name = 'core_control/private-plates.html'
    model = Product.objects.all()

    def get(self, request):
        data={
            "product":self.model
        }
        return render(request, self.template_name, data)


class Faqs(TemplateView):
    template_name = 'core_control/freq-q-ans.html'

    def get(self,request):

        return render(request, self.template_name)
    

class Contact(TemplateView):
    template_name = 'core_control/contact.html'

    def get(self,request):

        return render(request, self.template_name)
    



