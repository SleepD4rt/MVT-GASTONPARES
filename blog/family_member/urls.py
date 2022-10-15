from django.urls import path

from family_member import views

app_name = 'family_member'

urlpatterns = [
    path("family_member", views.family_member, name="member-list"),
]