from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),  # Home page showing all recipes
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('find/',views.find_recipe,name="find_receipe"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
