from django.contrib import admin
from .models import Member


# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  """
  class used to control the fields to display
  by specifying them in in a list_display property
  in the admin.py file.
  """
  list_display = ("firstname", "lastname", "joined_date",)
  prepopulated_fields = {"slug": ("firstname", "lastname")}


admin.site.register(Member, MemberAdmin)

