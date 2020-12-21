from django.db import models
from zutils.models import UtilConfs
from django.utils.text import slugify
from django.urls import reverse

class State(UtilConfs):
    name = models.CharField(verbose_name='اسم الولاية',max_length=50)
    slug = models.SlugField(editable=False)
    is_active = models.BooleanField(default=True)

    def save(self,*args , **kwargs):
        self.slug = slugify(self.name,allow_unicode=True)
        super(State,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return  reverse('locations:state_detail',args=[str(self.id)])
        return reverse('locations:state_list')

class Locality(UtilConfs):
    name = models.CharField(verbose_name='اسم المحلية',max_length=50)
    state = models.ForeignKey(State,verbose_name='الولاية',on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    is_active = models.BooleanField(default=True)

    class Meta :
        verbose_name_plural = 'Localities'

    def save(self,*args , **kwargs):
        self.slug = slugify(self.name,allow_unicode=True)
        super(Locality,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return  reverse('locations:state_detail',args=[str(self.id)])
        return reverse('locations:locality_list')

class Unity(UtilConfs):
    name = models.CharField(verbose_name='اسم الوحدة الادارية',max_length=50)
    locality = models.ForeignKey(Locality,verbose_name='المحلية',on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    is_active = models.BooleanField(default=True)

    class Meta :
        verbose_name_plural = 'Unities'

    def save(self,*args , **kwargs):
        self.slug = slugify(self.name,allow_unicode=True)
        super(Unity,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return  reverse('locations:state_detail',args=[str(self.id)])
        return reverse('locations:unity_list')

class City(UtilConfs):
    name = models.CharField(verbose_name='اسم المدينة',max_length=50)
    unity = models.ForeignKey(Unity,verbose_name='الوحدة الادارية',on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    is_active = models.BooleanField(default=True)

    class Meta :
        verbose_name_plural = 'Cities'

    def save(self,*args , **kwargs):
        self.slug = slugify(self.name,allow_unicode=True)
        super(City,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return  reverse('locations:state_detail',args=[str(self.id)])
        return reverse('locations:city_list')

class District(UtilConfs):
    name = models.CharField(verbose_name='القرية / الحى',max_length=50)
    city = models.ForeignKey(City,verbose_name='المدينة',on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    is_active = models.BooleanField(default=True)

    def save(self,*args , **kwargs):
        self.slug = slugify(self.name,allow_unicode=True)
        super(District,self).save(*args,**kwargs)

    def __str__(self):
        return self.name
