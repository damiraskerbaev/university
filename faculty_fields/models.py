from django.db.models import *

class Tuition_language(Model):

    language = CharField(
        'Language',
        max_length=32
    )

    def __str__(self):
        return f'{self.language}'
    
    class Meta:
        verbose_name = 'Tuition language'
        verbose_name_plural = 'Tuition languages'


class Education_forms(Model):

    name = CharField(
        'Education forms name',
        max_length=32
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Education form'
        verbose_name_plural = 'Education forms'

class Subject(Model):

    name = CharField(
        'Subject name',
        max_length=32
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'