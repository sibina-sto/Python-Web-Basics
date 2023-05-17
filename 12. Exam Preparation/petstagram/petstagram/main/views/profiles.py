from django.shortcuts import render, redirect


from petstagram.main.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.common.helpers import get_profile
from petstagram.main.models import PetsPhoto, Profile, Pet



