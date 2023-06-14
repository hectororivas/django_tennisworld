from django.db import models

class Member(models.Model):
  """
  class used to store membership information
  for tennis club members"
  """
  firstname = models.CharField(max_length=255)
  lastname  = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
