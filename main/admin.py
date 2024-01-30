from django.contrib import admin
from .models import Profession_images, Portfolio, Services, About_body_images,About_main_image,About_page_delivery,About_work_structure, Form_message
from modeltranslation.admin import TranslationAdmin


# Register your models here.

admin.site.register(About_body_images)
admin.site.register(About_main_image)
admin.site.register(Form_message)
admin.site.register(Profession_images)

@admin.register(Portfolio)
class Portfolio_trans(TranslationAdmin):
    list_display = ('title', 'text', 'image',)

@admin.register(Services)
class Services_Trans(TranslationAdmin):
    list_display = ('title', 'text', 'image',)

@admin.register(About_page_delivery)
class About_delivery_Trans(TranslationAdmin):
    list_display = ('title', 'text',)

@admin.register(About_work_structure)
class About_work_Trans(TranslationAdmin):
    list_display = ('title', 'text', 'image', )