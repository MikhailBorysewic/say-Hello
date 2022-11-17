from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse


class Hello(View):
    def get(self, request):
        return HttpResponse(f"Hello {request.GET.get('name', 'Anonim')}! {request.GET.get('message', 'How are you')}!")
