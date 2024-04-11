from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from core_control.models import Product


class Index(TemplateView):

    template_name  =  'index.html'

    model = Product.objects.all()

    def get(self, request):
        print(self.model)
        data={
            "products":self.model
        }
        return render(request, self.template_name, data)
    