from django.db import models

from tokenize import Name
from django.db import models
from django.contrib.auth.models import User

from Branch.models import  Branch_model
from Department.models import Department_model

'''class RoleDefined(models.Model):
	role = models.CharField(max_length=30)

class DepartmentDefined(models.Model):
	department = models.CharField(max_length=30)

class LocationDefined(models.Model):
	location = models.CharField(max_length=30)


class UserRole(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.OneToOneField(RoleDefined, on_delete=models.CASCADE)

class UserDepartment(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	department = models.OneToOneField(DepartmentDefined, on_delete=models.CASCADE)

class UserLocation(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	location = models.OneToOneField(LocationDefined, on_delete=models.CASCADE)'''

class User_models(models.Model):
					User_Name = models.OneToOneField(User,on_delete=models.CASCADE)
					Branch = models.OneToOneField(Branch_model,on_delete=models.CASCADE)
					Department = models.OneToOneField(Department_model,on_delete=models.CASCADE)
					#first_name = models.OneToOneField(first_name ,on_delete=models.CASCADE)
					#first_name = models.OneToOneField(last_name ,on_delete=models.CASCADE)