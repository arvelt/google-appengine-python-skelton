# -*- coding: utf-8 -*-

from django import forms

class GreetingForm(forms.Form):
    name=forms.CharField()
