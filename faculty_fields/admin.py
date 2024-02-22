from django.contrib.admin import *

from .models import (
    Tuition_language,
    Education_forms, 
    Subject
)

@register(Tuition_language)
class Tuition_languageAdmin(ModelAdmin):
    list_display=('id', 'language')
    list_display_links=('id',  'language')

@register(Education_forms)
class Education_formAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_display_links=('id', 'name')

@register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_display_links=('id', 'name')