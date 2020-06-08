from django.db import models

#model with choices

class Person(models.Model):
	SHIRT_SIZES=(('L','LARGE'),
			('M','MEDIUM'),
			('S', 'SMALL'),
		)
	name=models.CharField(max_length=50)
	shirt_size=models.CharField(max_length=1, choices=SHIRT_SIZES)


	class Meta:
		pass
	def __str__(self):
		return '{}, {}'.format(self.name, self.shirt_size)


class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)


class Publisher(models.Model):
	name=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	city=models.CharField(max_length=20)
	state_province=models.CharField(max_length=20)
	country=models.CharField(max_length=20)
	website=models.URLField()

	class Meta:
		ordering=['-name']

	def __str__(self):
		return self.name


class Author(models.Model):
	salutation=models.CharField(max_length=5)
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=100)
	headshot=models.FileField(help_text='Please upload photo. (jpg, jpeg, png)')

	def __str__(self):
		return self.name


class Book(models.Model):
	title=models.CharField(max_length=5)
	authors=models.ManyToManyField(Author)
	publisher=models.ForeignKey(Publisher, on_delete=models.CASCADE)
	publication_date=models.DateField()

	def __str__(self):
		return self.title
		

class User_Profile(models.Model):
	fname=models.CharField(max_length=200)
	lname=models.CharField(max_length=200)
	technologies=models.CharField(max_length=200)
	email=models.EmailField(max_length=200)
	display_picture=models.FileField()

	def __str__(self):
		return self.fname