"""Views for the triptales app."""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime
from triptales.forms import *
from triptales.models import *
from django.views import View
from django.utils.decorators import method_decorator


# Create your views here.
def index(request):
    context_dict = {}

    # visitor_cookie_handler(request)

    response = render(request, 'triptales/index.html', context=context_dict)
    return response


def posts_by_continent(request, continent_name):
    continent_name = continent_name.replace('-', '').replace('.png', '')

    countries = Country.objects.filter(continent__iexact=continent_name)

    posts = VacationPost.objects.filter(country__in=countries).distinct()

    context_dict = {
        'continent_name': continent_name,
        'posts': posts,
    }

    return render(request, 'triptales/posts_by_continent.html', context=context_dict)


def post_detail(request, post_id):
    post = get_object_or_404(VacationPost, pk=post_id)
    context = {'post': post}
    return render(request, 'triptales/post_detail.html', context)


@login_required
def create_post(request):
    locations = Location.objects.all()
    form = VacationPostForm()

    if request.method == 'POST':
        form = VacationPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.likes = 0
            currentLocation = Location.objects.get(id=post.location.id)
            post.country = currentLocation.country
            post.save()
            form.save_m2m()
            return redirect(reverse('triptales:index'))  # Redirect to the desired page after successful form submission
        else:
            print(form.errors)


    return render(request, 'triptales/create_post.html', {'form': form, 'locations': locations})

@login_required
def add_country(request):

    form = CountryForm()

    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.save(commit=True)
            country.posts = 0
            country.views = 0
            country.save()
            return redirect(reverse('triptales:index'))
        else:
            print(form.errors)

    return render(request, 'triptales/add_country.html', {'form': form })

@login_required
def add_location(request):
    form = LocationForm()

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.posts = 0
            location.views = 0
            location.save()
            return redirect(reverse('triptales:index'))
        else:
            print(form.errors)

    return render(request, 'triptales/add_location.html', {'form':form})

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
    visitor_cookie_handler(request)
    return render(request, 'triptales/about.html')


def FAQ(request):
    visitor_cookie_handler(request)
    return render(request, 'triptales/FAQ.html')


def contact_us(request):
    visitor_cookie_handler(request)
    return render(request, 'triptales/contact_us.html')


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
    # return render(request, 'triptales/add_location.html', context_dict)


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


def quiz(request):
    return HttpResponse("Not implemented yet.")


def basetest(request, continent):
    context_dict = {'continent': continent}
    return render(request, 'triptales/basetest.html', context=context_dict)


@login_required
def register_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect(reverse('triptales:index'))
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'triptales/profile_registration.html', context_dict)


@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    form = UserProfileForm({'bio': user_profile.bio,
                            'picture': user_profile.picture})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect('triptales:profile', request.user.username)
        else:
            print(form.errors)

    context_dict = {'user_profile': user_profile, 'form': form}
    return render(request, 'triptales/userprofile_form_base.html', context_dict)


class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        print(f"User_profile {user_profile.bio}")
        form = UserProfileForm({'bio': user_profile.bio,
                                'picture': user_profile.picture})

        return (user, user_profile, form)

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('triptales:index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}
        return render(request, 'triptales/profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        # Check if the user is the same as the one who is logged in
        if request.user.username != username:
            return redirect(reverse('triptales:index'))

        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('triptales:index'))

        liked_posts = user_profile.liked_posts.all()
        saved_posts = user_profile.saved_posts.all()
        user_posts = user_profile.posts_made.all()

        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect('triptales:profile', user.username)
        else:
            print(form.errors)

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'liked_posts': liked_posts,
                        'saved_posts': saved_posts,
                        'user_posts': user_posts,
                        'form': form}

        return render(request, 'triptales/profile.html', context_dict)



