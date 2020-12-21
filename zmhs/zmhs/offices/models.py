from django.db import models
from zutils.models import UtilConfs
from zmhs.locations.models import State
from django.utils.text import slugify
from django.urls import reverse

class HQuarter(UtilConfs):
    name = models.CharField(verbose_name='أمانة',max_length=50)
    state = models.ForeignKey(State,verbose_name='الولاية',on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)

    def save(self,*args , **kwargs):
        self.slug = slugify(self.name,allow_unicode=True)
        super(HQuarter,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('offices:hq_list')


class Sector(UtilConfs):
    name = models.CharField(verbose_name='القطاع',max_length=50)
    hquarter = models.ForeignKey(HQuarter,verbose_name='الرئاسة',on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)

    def save(self,*args , **kwargs):
        self.slug = slugify(self.name,allow_unicode=True)
        super(Sector,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('offices:hq_list')

class Office(UtilConfs):
    name = models.CharField(verbose_name='المكتب',max_length=50)
    sector = models.ForeignKey(Sector,verbose_name='القطاع',on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)

    def save(self,*args , **kwargs):
        self.slug = slugify(self.name,allow_unicode=True)
        super(Office,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('offices:hq_list')
