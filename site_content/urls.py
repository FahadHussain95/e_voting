from django.urls import path
from site_content.views import *

urlpatterns = [
    path('/get_form_data', HelloView.as_view(), name='get-form-data')
]