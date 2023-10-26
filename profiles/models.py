from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), default="/profile_default.png"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    country = CountryField(
        verbose_name=_("Country"), default="US", blank=False, null=False
    )
    state = models.CharField(
        max_length=180,
        default="Texas",
    )
    account_number = models.IntegerField(
        default=9118872201,
    )
    account_type = models.CharField(
        max_length=180,
        default="E Checking",
    )
    opening_date = models.CharField(
        max_length=180,
        default="4/6/2000",
    )
    opening_amount = models.FloatField(
        default=4800000.00,
    )
    present_amount = models.FloatField(
        default=97000000.00,
    )
    next_of_kin = models.CharField(
        default="Monika A. Hinks",
        max_length=200
    )
    maiden_name = models.CharField(
        default="Sylvester",
        max_length=200
    )
    pet_name = models.CharField(
        default="Jack",
        max_length=200
    )
    favorite_color = models.CharField(
        default="white",
        max_length=200
    )
     


    def __str__(self):
        return f"{self.user.username}'s profile"