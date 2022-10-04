from django.contrib import admin

from site_content.models import Voters, Candidate

# Register your models here.
admin.site.register(Voters)
admin.site.register(Candidate)