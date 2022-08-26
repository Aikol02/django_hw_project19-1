from django.db import models


class Client(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255, null=True, blank=True)
	active = models.BooleanField(default=True, verbose_name="Является активным покупателем!")
	bottles_ordered = models.IntegerField(default=1)
	photo = models.ImageField(
		verbose_name="Фото",
		upload_to='photos',
		null=True,
		blank=True
	)

	def __str__(self):
		return f'{self.name}'


class Order(models.Model):
	client = models.ForeignKey(
		to=Client,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='order'
	)

	created_at = models.DateTimeField(
		verbose_name="Date and time of creation of order",
		auto_now_add=True,
	)
	updated_at = models.DateTimeField(
		verbose_name="Date and time of update of order",
		auto_now=True,
	)
	description = models.TextField(null=True, blank=True)
	name = models.CharField(max_length=255)
	contacts = models.CharField(null=True, blank=True, max_length=255)
	finished = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.name} - {self.contacts}'
