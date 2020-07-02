from django.urls import path, include

from banks.views import *

urlpatterns = [
    path("get_branch_details/", get_branch_details, name="get_branch_details"),
    path("get_branches_in_city/", get_branches_in_city, name="get_branches_in_city"),
]
