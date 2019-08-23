from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from .views import EventDetailView, PlaceDetailView, ArtistDetailView, OrgDetailView

urlpatterns = [
	re_path(r'^afisha/$', views.index, name='index'),
    re_path(r'^artists/$', views.artists, name='artists'),
    re_path(r'^places/$', views.places, name='places'),
    re_path(r'^orgs/$', views.orgs, name='orgs'),
	path('afisha/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
	path('places/<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),
	path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist-detail'),
	path('orgs/<int:pk>/', OrgDetailView.as_view(), name='artist-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)