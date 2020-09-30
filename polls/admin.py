from django.contrib import admin
from .models import Poll, Choice

# Registered Apps
admin.site.register(Poll)
admin.site.register(Choice)


# Headers
admin.site.site_header = "Polls Api Administration"
