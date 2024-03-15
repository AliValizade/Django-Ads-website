from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _


class Ad(models.Model):
    title = models.CharField(_('Ad Title'), max_length=100)
    description = models.TextField(_('Ad Descriptin'), max_length=2000)
    keywords = models.CharField(_('Keywords'), max_length=255)
    link = models.URLField(_('Ad Link'))
    advertiser_name = models.CharField(_('Name/Company'), max_length=100)
    phone = models.CharField(_('Phone Number'), max_length=15)
    mobile = models.CharField(_('Mobile'), max_length=15)
    instagram_id = models.CharField(_('Instagram Id'), max_length=100, blank=True, null=True)
    whatsapp = models.CharField(_('Whatsapp Number'), max_length=15, blank=True, null=True)
    state = models.CharField(_('State'), max_length=50)
    city = models.CharField(_('City'), max_length=50)
    address = models.TextField(_('Address'), max_length=500)
    main_image = models.ForeignKey('AdImage', on_delete=models.SET_NULL, related_name='main_image', null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("ad_detail", args=[self.pk])

    class Meta:
        verbose_name = _('Ad')
        verbose_name_plural = _('Ads')


class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='images', blank=True, )
    image = models.ImageField(_("Ad image"), upload_to='ads/ad_cover/')

    def __str__(self):
        return f"Image of {self.ad.title}"

