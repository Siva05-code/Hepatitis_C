from django.contrib import admin
from .models import HepatitisRecord

admin.site.register(HepatitisRecord)

admin.site.site_header = "Hepatitis Stage Prediction Admin"
admin.site.site_title = "Hepatitis Admin Portal"
admin.site.index_title = "Welcome to the Hepatitis Prediction Dashboard"

