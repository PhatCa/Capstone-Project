from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from recipecard import views as recipe_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',recipe_views.recipe_list, name="home"),
    path('recipe/',include('recipecard.urls')),
    path('accounts/',include('accounts.urls')),
    
]

urlpatterns += staticfiles_urlpatterns()