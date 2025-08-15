from django.urls import path
from .views import HomeView, AboutView, SpeciesView, GalleryView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('species/', SpeciesView.as_view(), name='species'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('contacts/', ContactView.as_view(), name='contacts'),
]
