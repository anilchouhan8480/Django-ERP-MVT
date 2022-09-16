from django.contrib import admin
from .models import TallyModel


@admin.register(TallyModel)
class Tally_Admin(admin.ModelAdmin):

	list_display= ['Data_Name','Transection_No',
    ]