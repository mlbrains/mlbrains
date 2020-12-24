from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.homepageView, name="homepage"),
    path('login/', views.loginView, name="login"),
    path('signup/', views.signupView, name="signup"),    
    path('logout/',views.logoutView,name="logout"),
    path('landingpage/', views.landingpage, name="landingpage")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
