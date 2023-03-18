from django.contrib import admin

from site_content.models import Party, Candidate


class PartyAdmin(admin.ModelAdmin):
    list_filter = ('related_candidate',)
    # readonly_fields = ('vote_count',)


# Register your models here.
admin.site.register(Party, PartyAdmin),
admin.site.register(Candidate)