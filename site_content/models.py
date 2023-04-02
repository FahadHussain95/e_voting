from django.db import models
from django.utils import timezone as dj_datetime
import time
# Create your models here.


def file_upload_to(instance, filename):
    # return str(instance.id)
    return '/'.join([instance.__class__.__name__, str(dj_datetime.now().strftime('%Y/%m/%d')),
                     str(int(time.time())) + filename])


class Party(models.Model):
    party_name = models.CharField(max_length=50, verbose_name='Party Name')
    part_logo = models.ImageField(verbose_name='Small Image', upload_to=file_upload_to, null=True)
    party_rid = models.CharField(max_length=50, verbose_name='Registration Number')
    party_phone_number = models.CharField(verbose_name='Head Office Number', max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Party'
        verbose_name_plural = 'Parties'

    def __str__(self):
        return "%s -- %s" % (self.party_name, self.party_rid)


class Candidate(models.Model):
    candidate_party = models.ForeignKey(Party, verbose_name="Candidate Party", related_name="related_candidate",
                                        default=None, on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=50, verbose_name='Candidate Name')
    candidate_picture = models.ImageField(verbose_name="Profile Picture", upload_to=file_upload_to, max_length=2000,
                                        null=True)
    candidate_email = models.EmailField(verbose_name='Email', max_length=255, null=True, blank=True, unique=True)
    candidate_nic = models.CharField(max_length=500, verbose_name='Candidate NIC Number', db_index=True, null=False, blank=False)
    candidate_city = models.CharField(max_length=500, verbose_name='Candidate City', null=False, blank=False, default="N/A")
    candidate_state = models.CharField(max_length=500, verbose_name='Candidate State', null=False, blank=False, default="N/A")
    candidate_area_code = models.CharField(max_length=500, verbose_name='Candidate Area Code', db_index=True,
                                           null=False, blank=False, default=None)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=500, null=True, blank=True)
    vote_count = models.PositiveIntegerField(verbose_name='Vote Count', default=0)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'

    def __str__(self):
        return "%s" % (self.candidate_name)