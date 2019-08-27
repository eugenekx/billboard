from django.shortcuts import render
from .models import Place, Event, Artist, Org
from django.views.generic.detail import DetailView
from .forms import EventForm, ArtistForm, OrgForm, PlaceForm


def index(request):
	name = request.GET.get('name', '')
	date = request.GET.get('date', '')
	price_from = request.GET.get('price_from', '')
	price_to = request.GET.get('price_to', '')
	tags = request.GET.get('tags', '')
	
	events = Event.objects.all()
	

	if name != '':
		events = events.filter(name__icontains=name)

	if date != '':
		events = events.filter(datetime__date=date)
	
	if price_from != '' and price_from.isdigit():
		events = events.filter(price__gte=price_from)

	if price_to != '' and price_to.isdigit():
		events = events.filter(price__lte=price_to)

	tags = tags.split()


	if tags != '':
		for tag in tags:
			events = events.filter(tags__name__iexact=tag)
	
	events = events.order_by('datetime')

	empty_flag = False
	if len(events) == 0:
		empty_flag = True


	form = EventForm(request.GET)
	return render(request,
        'index.html',
        context={'events': events, 'empty_flag': empty_flag, 'form': form})

def artists(request):
	name = request.GET.get('name', '')
	tags = request.GET.get('tags', '')

	a = Artist.objects.all()
	
	if name != '':
		a = a.filter(name__icontains=name)

	tags = tags.split()

	if tags != '':
			for tag in tags:
				a = a.filter(tags__name__iexact=tag)	

	empty_flag = False
	if len(a) == 0:
		empty_flag = True
	
	form = ArtistForm(request.GET)

	return render(request,
        'artists.html',
        context={'artists': a, 'empty_flag': empty_flag, 'form': form})

def orgs(request):
	name = request.GET.get('name', '')
	tags = request.GET.get('tags', '')

	o = Org.objects.all()

	if name != '':
		o = o.filter(name__icontains=name)

	tags = tags.split()

	if tags != '':
			for tag in tags:
				o = o.filter(tags__name__iexact=tag)	

	empty_flag = False
	if len(o) == 0:
		empty_flag = True
	
	form = OrgForm(request.GET)
	return render(request,
        'orgs.html',
        context={'orgs': o, 'empty_flag': empty_flag, 'form': form})

def places(request):
	name = request.GET.get('name', '')
	address = request.GET.get('address', '')
	tags = request.GET.get('tags', '')

	p = Place.objects.all()

	if name != '':
		p = p.filter(name__icontains=name)

	if address != '':
		a_s = address.split()
		for it in a_s:
			p = p.filter(address__icontains=it)
	
	tags = tags.split()

	if tags != '':
			for tag in tags:
				p = p.filter(tags__name__iexact=tag)
	

	empty_flag = False
	if len(p) == 0:
		empty_flag = True
	
	form = PlaceForm(request.GET)

	return render(request,
        'places.html',
        context={'places': p, 'empty_flag': empty_flag, 'form': form})




class EventDetailView(DetailView):
	model = Event

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['artists'] = self.get_object().artists.all()
		context['orgs'] = self.get_object().org.all()
		context['tags'] = self.get_object().tags.all()
		return context


class PlaceDetailView(DetailView):
	model = Place

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['events'] = self.get_object().event_set.all().order_by('datetime')
		return context


class OrgDetailView(DetailView):
	model = Org


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['events'] = self.get_object().event_set.all().order_by('datetime')
		return context

class ArtistDetailView(DetailView):
	model = Artist


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['events'] = self.get_object().event_set.all().order_by('datetime')
		context['tags'] = self.get_object().tags.all()
		return context