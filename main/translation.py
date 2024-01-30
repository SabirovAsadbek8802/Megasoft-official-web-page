from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Portfolio)
class Portfolio_Trans(TranslationOptions):
    fields = ('title', 'text',)

@register(Services)
class Services_Trans(TranslationOptions):
    fields = ('title', 'text',)

@register(About_page_delivery)
class About_delivery_Trans(TranslationOptions):
    fields = ('title', 'text',)

@register(About_work_structure)
class About_work_Trans(TranslationOptions):
    fields = ('title', 'text',)