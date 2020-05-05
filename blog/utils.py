from django.shortcuts import render, get_object_or_404, redirect
from .models import *

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request,
                      self.template,
                      {self.model.__name__.lower(): obj, 'admin_obj': obj, 'detail_page': True})


class ObjectCreateMixin:
    model_form = None

    def get(self, request):
        form = self.model_form()
        return render(request,
                      'blog/obj_create.html',
                      {'form': form, 'model': self.model_form.Meta.model.__name__.lower()})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request,
                      'blog/obj_create.html',
                      {'form': bound_form, 'model': self.model_form.Meta.model.__name__.lower()})


class ObjectUpdateMixin():
    model = None
    model_form = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request,
                      'blog/obj_update.html',
                      {'form': bound_form, 'obj': obj, 'model': self.model.__name__.lower()})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request,
                      'blog/obj_update.html',
                      {'form': bound_form, 'obj': obj, 'model': self.model.__name__.lower()})


class ObjectDeleteMixin():
    model = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request,
                      'blog/obj_delete.html',
                      {'obj': obj, 'model': self.model.__name__.lower()})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))