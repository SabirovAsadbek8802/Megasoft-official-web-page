from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

class Profession_images(models.Model):
    class Meta:
        verbose_name = 'pro image'
    image1 = models.ImageField(upload_to='media/')
    image2 = models.ImageField(upload_to='media/', blank=True)
    image3 = models.ImageField(upload_to='media/', blank=True)
    
    def __str__(self):
        return f"image - {self.pk}"
    

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    text = models.TextField()

    def __str__(self):
        return self.title
    
# def validate_svg_file(value):
#     if not value.name.endswith('.svg'):
#         raise ValidationError('Only SVG file are allowed')


class Services(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='media/', validators=[FileExtensionValidator(['svg'])])
    text = models.TextField()

    def __str__(self):
        return self.title
    

class About_page_delivery(models.Model):
    class Meta:
        verbose_name_plural = 'deliveries'
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

class About_work_structure(models.Model):
    class Meta:
        verbose_name = 'work detail'
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='media/about/', validators=[FileExtensionValidator(['svg'])])
    text = models.TextField()

    def __str__(self):
        return self.title

class About_main_image(models.Model):
    class Meta:
        verbose_name = 'main image'
    image = models.ImageField(upload_to='media/about/')

    def __str__(self):
        return f'rasm - {self.pk}'

class About_body_images(models.Model):
    class Meta:
        verbose_name = 'body image'
    image1 = models.ImageField(upload_to='media/about/')
    image2 = models.ImageField(upload_to='media/about/', blank=True)
    image3 = models.ImageField(upload_to='media/about/', blank=True)

    def __str__(self):
        return f'rasm - {self.pk}'
    

class Form_message(models.Model):
    class Meta:
        verbose_name = 'message'
    title = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    call_num = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=150,null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.title
    