from django.db import models

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=200, unique=True)
	def __str__(self):
		return self.name

class Place(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	link = models.URLField()
	address = models.CharField(max_length=200)
	image = models.ImageField(upload_to='places', default='/')

	def __str__(self):
		return self.name


class Org(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	link = models.URLField()
	tags = models.ManyToManyField(Tag)
	image = models.ImageField(upload_to='orgs', default='/')

	def __str__(self):
		return self.name

class Artist(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	link = models.URLField()
	tags = models.ManyToManyField(Tag)
	image = models.ImageField(upload_to='artists', default='/')
	def __str__(self):
		return self.name

class Event(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	
	CONCERT = 'CON'
	FESTIVAL = 'FES'
	LECTION = 'LEC'
	EXPO = 'EXP'
	FORUM = 'FOR'
	OTHER = 'OTH'

	EVENT_CHOICES = [
		(CONCERT, 'Концерт'),
		(FESTIVAL, 'Фестиваль'),
		(LECTION, 'Лекция'),
		(EXPO, 'Выставка'),
		(FORUM, 'Форум'),
		(OTHER, 'Другое'),
	]

	event_type = models.CharField(
		max_length=3,
		choices=EVENT_CHOICES,
		default=CONCERT,
	)
	
	price = models.IntegerField()
	link = models.URLField()

	datetime = models.DateTimeField()
	artists = models.ManyToManyField(Artist)
	org = models.ManyToManyField(Org)
	place = models.ForeignKey('Place', on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag)

	image = models.ImageField(upload_to='events', default='/')
	
	def get_day(self):
		t = str(self.datetime.day)
		if len(t) == 1:
			t = '0'+t
		return t

	def get_month(self):
		t = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
		return t[self.datetime.month-1]
	
	def get_week_day(self):
		t = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
		return t[self.datetime.weekday()]
	def get_tags(self):
		return self.tags.all()

	def __str__(self):
		return self.name
	