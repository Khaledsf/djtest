from django.db import models

# Create your models here.
class Grain(models.Model):
	variety = models.CharField(max_length = 20)
	place = models.CharField(max_length = 20)
	region = models.CharField(max_length = 100)
	rediness = models.BooleanField()
	img = models.ImageField(null=True, blank=True, upload_to='media', default=None)

class Roast(models.Model):
	temp = models.DecimalField(decimal_places = 2, max_digits = 5)
	time = models.IntegerField()
	is_strong = models.BooleanField()