from django.db.models import *

class University(Model):

    name = CharField(
        'Name of the university',
        max_length=256
    )

    address = TextField(
        'Address of the university'
    )

    phone_number = CharField(
        'University phone number',
        max_length=13
    )

    image = ImageField(
        'Image of the university',
        upload_to='university-images/'
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='University'
        verbose_name_plural='Universities'