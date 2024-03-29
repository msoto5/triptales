"""triptales_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, messages
from django.urls import path, reverse
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView
from triptales import views

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('triptales:register_profile')

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print(form.errors)
        messages.error(self.request, form.errors)
        return response
    

    
urlpatterns = [
    path('get_all_posts/<str:type>/', views.get_all_posts, name='get_all_posts'),
    path('filter_sort_by/<str:sort_type>/<str:filter_type>/<str:continent>/', views.filter_sort_by, name='filter_sort_by'),
    path('', views.index, name='index'),
    path('triptales/', include('triptales.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
