from django.db import models
from django.urls import reverse
class user_groups(models.Model):
	user_cat = (
		('D','Doctor'),
		('P','Patient'),
		('S','Staff'),
		)
	usr_g=models.CharField(max_length=1, choices=user_cat)

	def __str__(self):
	 	return self.usr_g

class user(models.Model):
	user_group = models.ForeignKey(user_groups,on_delete=models.CASCADE)
	userid  = models.CharField(max_length=10,primary_key=True)
	password = models.CharField(max_length=8)


	def __str__(self):
	 	return self.userid

class doctor(models.Model):
	sex=(
		('M','Male'),
		('F','Female'),
		('T','Transgender'),
		)
	
	profile_pic=models.FileField()
	name = models.CharField(max_length=100)
	sex=models.CharField(max_length=1,choices=sex)
	dob=models.DateField()
	phone_no=models.CharField(max_length=10)
	qualifications=models.TextField(max_length=100)
	address=models.CharField(max_length=250)
	speciality = models.TextField(max_length=100)
	user=models.ForeignKey(user,on_delete=models.CASCADE)
	def get_absolute_url(self):
            return reverse('hospital:index')
	def __str__(self):
	    return self.name

class Patient(models.Model):
	sex=(
		('M','Male'),
		('F','Female'),
		('T','Transgender'),
		)
	profile_pic=models.FileField()
	name = models.CharField(max_length=100)
	sex=models.CharField(max_length=1,choices=sex)
	dob=models.DateField()
	phone_no=models.CharField(max_length=10)
	problem=models.TextField(max_length=250)
	address=models.CharField(max_length=250)
	symptomps = models.TextField(max_length=100)
	user=models.ForeignKey(user,on_delete=models.CASCADE)

	def get_absolute_url(self):
	    return reverse('hospital:index')		

	def __str__(self):
		return self.name

	
