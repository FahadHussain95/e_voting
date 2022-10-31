from django.db import models

# Create your models here.

class Voters(models.Model):
    voter_name = models.CharField(max_length=50, verbose_name='Voter Name')
    voter_nic = models.CharField(max_length=500, verbose_name='Voter NIC Number', db_index=True, null=False, blank=False)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=500, null=True, blank=True)
    email = models.CharField(verbose_name='Email', max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Voter'
        verbose_name_plural = 'Voters'

    def __str__(self):
        return "%s -- %s" % (self.voter_name, self.voter_nic)


class Candidate(models.Model):
    candidate_name = models.CharField(max_length=50, verbose_name='Candidate Name')
    candidate_nic = models.CharField(max_length=500, verbose_name='Candidate NIC Number', db_index=True, null=False, blank=False)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=500, null=True, blank=True)
    vote_count = models.PositiveIntegerField(verbose_name='Vote Count', default=0)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    #email = models.CharField(verbose_name='Email', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'

    def __str__(self):
        return "%s" % (self.candidate_name)