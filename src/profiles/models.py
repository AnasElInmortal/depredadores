from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Cinta(models.Model):
    cintaCode = models.CharField(max_length=200, unique=True, null=False)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cintaCode

class Certificado(models.Model):
    folio = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField("Fecha", null=False, default=datetime.date.today)
    idCinta = models.ForeignKey(Cinta, on_delete=models.CASCADE, verbose_name="Cinta")
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return self.folio

class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)
    idCinta = models.ForeignKey(Cinta, null=True, on_delete=models.SET_NULL, verbose_name="Cinta")

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)
