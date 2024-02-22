from django.db.models import *
from universities.models import University
from faculty_fields.models import(
    Tuition_language,
    Education_forms,
    Subject
)

class Faculty(Model):

    university = ForeignKey(
        University,
        verbose_name = 'University',
        on_delete=CASCADE
    )

    name = CharField(
        'Faculty name',
        max_length=256
    )

    tuition_language = ManyToManyField(
        Tuition_language,
        verbose_name='Tuition language'
    )

    education_form = ManyToManyField(
        Education_forms,
        verbose_name='Education form'
    )

    acceptance = PositiveSmallIntegerField(
        'Acceptance number',
    )

    grant = DecimalField(
        'Grand score',
        decimal_places=1,
        blank=True,
        null=True,
        max_digits=4
    )

    contract = DecimalField(
        'Contract score',
        decimal_places=1,
        blank=True,
        null=True,
        max_digits=4
    )

    first_subject = ForeignKey(
        Subject,
        verbose_name = 'First subject',
        on_delete=CASCADE,
        related_name='subjects'
    )

    second_subject = ForeignKey(
        Subject,
        verbose_name='Second subject',
        on_delete=CASCADE
    )

    class Meta:
        verbose_name='Faculty'
        verbose_name_plural='Faculties'