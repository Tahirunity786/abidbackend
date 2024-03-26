from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.

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

    def get(self, request):

        return render(request, self.template_name)


class Faqs(TemplateView):
    template_name = 'core_control/freq-q-ans.html'

    def get(self,request):

        return render(request, self.template_name)
    

class Contact(TemplateView):
    template_name = 'core_control/contact.html'

    def get(self,request):

        return render(request, self.template_name)