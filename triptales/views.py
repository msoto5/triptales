"""Views for the triptales app."""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from triptales.forms import *
from triptales.models import *


# Create your views here.
def index(request):
    return HttpResponse("Not implemented yet.")

    category_list = []
    pages_list = []

    context_dict = {}
    context_dict['boldmessage'] = "Crunchy, creamy, cookie, candy, cupcake!"
    context_dict['categories'] = category_list
    context_dict['pages'] = pages_list

    context_dict = {}

    visitor_cookie_handler(request)

    response = render(request, 'triptales/index.html', context=context_dict)
    return response

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', 
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits

def about(request):
    context_dict = {'boldmessage': "Miguel"}

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    response = render(request, 'triptales/about.html', context=context_dict)
    return response

def show_category(request, category_name_slug):
    return HttpResponse("Not implemented yet.")

    # Tango_with_django project:
    # context_dict = {}
    # try:
    #     category = [Category.objects.get(slug=category_name_slug)]
    #     pages = Page.objects.filter(category=category).order_by('-views')
    #     context_dict['pages'] = pages
    #     context_dict['category'] = category
    # except Category.DoesNotExist:
    #     context_dict['category'] = None
    #     context_dict['pages'] = None
        
    # return render(request, 'triptales/category.html', context=context_dict)

@login_required
def add_category(request):
    return HttpResponse("Not implemented yet.")
    # form = CategoryForm()

    # if request.method == 'POST':
    #     form = CategoryForm(request.POST)

    #     if form.is_valid():
    #         form.save(commit=True)
    #         return redirect('/triptales/')
    #     else:
    #         print(form.errors)

    # return render(request, 'triptales/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
    return HttpResponse("Not implemented yet.")
    # try:
    #     category = Category.objects.get(slug=category_name_slug)
    # except:
    #     category = None
    
    # if category is None:
    #     return redirect('/triptales/')

    # form = PageForm()

    # if request.method == 'POST':
    #     form = PageForm(request.POST)

    #     if form.is_valid():
    #         if category:
    #             page = form.save(commit=False)
    #             page.category = category
    #             page.views = 0
    #             page.save()

    #             return redirect(reverse('triptales:show_category',
    #                                     kwargs={'category_name_slug':
    #                                              category_name_slug}))
    #     else:
    #         print(form.errors)

    # context_dict = {'form': form, 'category': category}
    # return render(request, 'triptales/add_page.html', context_dict)

def goto_url(request):
    return HttpResponse("Not implemented yet.")
    # if request.method == 'GET':
    #     try:
    #         page_id = request.GET['page_id']
    #         selected_page = Page.objects.get(id=page_id)
    #         selected_page.views += 1
    #         selected_page.save()
    #         return redirect(selected_page.url)
    #     except Page.DoesNotExist:
    #         return redirect(reverse('triptales:index'))
