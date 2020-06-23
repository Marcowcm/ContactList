from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Contact(models.Model):

    class TitleChoices(models.TextChoices):
        MISTER = 'MR', _('Mr.')
        MISS = 'MISS', _('Miss.')
        MS = 'MS',_('Ms.')
        MISTRESS = 'MRS', _('Mrs.')
        DOCTOR = 'DR',_('Dr.')
    
    title = models.CharField(_("Title"),choices=TitleChoices.choices, max_length=10,default=TitleChoices.MISTER)
    first_name = models.CharField(_("first name"), max_length=50,blank=True,null=True)
    last_name = models.CharField(_("last name"), max_length=50, blank=True,null=True)
    phone = PhoneNumberField(_("Phone No."),blank=True)
    email = models.EmailField(_("e-mail"), max_length=254,blank=True)
 
    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return '%s %s'%(self.first_name,self.last_name)
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else: 
            return 'Unknown'

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return '%s %s'%(self.title,self.full_name)

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})
