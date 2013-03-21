from django.db import models
from django.forms import ModelForm

# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True,
		help_text="Unique value for product page URL, created from name.")

	def __unicode__(self):
		return self.name

		@models.permalink
		def get_absolute_url(self):
			return "/employee/"+self.id
		

class Job(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return "/job/"+self.name

	
	
class Company(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name
	
	@models.permalink
	def get_absolute_url(self):
		return "/company/"+self.id
		
class CompanyForm(ModelForm):
	class Meta:
		model=Company


			
class Contract(models.Model):
	company = models.ForeignKey(Company)
	job = models.ForeignKey(Job) 
	employee = models.ForeignKey(Employee)
	@models.permalink
	def get_absolute_url(self):
		return "/contract/"+self.id
	

			
	

