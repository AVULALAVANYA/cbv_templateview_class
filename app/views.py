from django.shortcuts import render
from typing import Any, Dict
# Create your views here.
from django.views.generic import TemplateView
class cbv_context(TemplateView):
    template_name='cbv_context.html'

    def get_context_data(self, **kwargs):
        EDCO=super().get_context_data(**kwargs)

        EDCO['name']="Lavanya"
        EDCO['age']=23
        return EDCO
