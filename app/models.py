

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices

SKILL = [
    (1, 'ระดับปฏิบัติการ'),
    (2, 'ระดับชำนาญการ'),
    (3, 'ระดับชำนาญการพิเศษ'),
    (4, 'ระดับเชี่ยวชาญ'),
]

SEX_P = [
    (1, 'ชาย'),
    (2, 'หญิง'),

]


class Doctor(models.Model):
    """Model definition for Doctor."""

    # TODO: Define fields here
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    skill = models.IntegerField(choices=SKILL)

    class Meta:
        """Meta definition for Doctor."""

        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        """Unicode representation of Doctor."""
        return self.first_name+''+self.last_name


class Hospital(models.Model):
    """Model definition for Hospital."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Hospital."""

        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitals'

    def __str__(self):
        """Unicode representation of Hospital."""
        return self.name


class Patient(models.Model):
    """Model definition for patient."""

    # TODO: Define fields here
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    sex = models.IntegerField(choices=SEX_P)

    class Meta:
        """Meta definition for patient."""

        verbose_name = 'patient'
        verbose_name_plural = 'patients'

    def __str__(self):
        """Unicode representation of patient."""
        return self.f_name+''+self.l_name
