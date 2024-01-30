from django.shortcuts import render
from django.views import View
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse
from django.urls.base import resolve,reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from .models import Profession_images, Portfolio, Services, About_page_delivery, About_work_structure, About_body_images, About_main_image, Form_message
import re 





# def change_lang(request, language_code):
#     # Set the language code in the session
#     request.session[translation.LANGUAGE_SESSION_KEY] = language_code

#     # Update the language cookie
#     response = HttpResponseRedirect(reverse('index'))
#     response.set_cookie(
#         translation.LANGUAGE_COOKIE_NAME,
#         language_code,
#         max_age=365 * 24 * 60 * 60,  # 1 year
#     )

    # return response


def change_lang(request, lang):
    for language, _ in settings.LANGUAGES:
        translation.activate(language)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERRER")).path)
        except Resolver404:
            view=None
        if view:
            break

        if view:
            translation.activate(lang)
            next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
            responce = HttpResponseRedirect(next_url)
            responce.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
        else:
            responce=HttpResponseRedirect('/')

        return responce
    


def mainpage(request):
    # profession 3 images
    images = Profession_images.objects.all()

    # portfolio items
    portfolio = Portfolio.objects.order_by("-id")
    portfolio1 = portfolio.first()
    portfolio2 = portfolio[1]
    portfolio3 = portfolio[2]
    portfolio4 = portfolio[3]
    

    #services
    service1 = Services.objects.all()

    #about page work structure
    about_working = About_work_structure.objects.all()


    return render(request, "index.html", {
        'images':images,
        "portfolio1":portfolio1,
        "portfolio2":portfolio2,
        "portfolio3":portfolio3,
        "portfolio4":portfolio4,
        'services1':service1,
        'works':about_working,
        
    })
        

def about(request):
    
    #about page
    about_page = About_page_delivery.objects.all()

    #about page work structure
    about_working = About_work_structure.objects.all()

    #about page body images
    body_images = About_body_images.objects.order_by('-id').first()

    #about page main image
    main_image = About_main_image.objects.order_by('-id').first()
    

    return render(request, "about.html", {
        'about_page':about_page,
        'works':about_working,
        'body_images':body_images,
        'main_image':main_image,
    })

def conditions(request):
    return render(request, "conditions.html")

def contact(request):
    return render(request, "contact.html")

def portfolio(request):
    blog_items_row1 = Portfolio.objects.all()[0::2]
    blog_items_row2 = Portfolio.objects.all()[1::2]

    return render(request, "portfolio.html", {
        'blog_items1':blog_items_row1,
        'blog_items2':blog_items_row2,
    })

def privacy(request):
    return render(request, "privacy.html")

def services(request):
    service1 = Services.objects.all()


    return render(request, "services.html", {
        'services':service1,
    })

class Contact(View):
    def post(self, request):
        
        try:
            title = request.POST.get('name')
            email = request.POST.get('email')
            call_num = request.POST.get('number')
            message = request.POST.get('message')
            company = request.POST.get('company')

            phone_regex = r'^\+[1-9]\d{1,14}$'
            email_regex = r'\S+@\S+\.\S+'

            if call_num:
                if not re.search(phone_regex, call_num):
                    return JsonResponse({'message': _('Invalid phone number'), 'success': False}, status=200)
            
            
            if email:
                if not re.search(email_regex, email):
                    return JsonResponse({'message': _('Invalid email addres'), 'success': False}, status=200)
            
            if not email and not call_num:
                return JsonResponse({'message': _('Fill all required fields!'), 'success': False}, status=200)

            if not title and not message:
                return JsonResponse({'message': _('Fill all required fields!'), 'success': False}, status=200)
            
            if not title:
                return JsonResponse({'message': _('Name is required!'), 'success': False}, status=200)
            
            if not message:
                return JsonResponse({'message': _('Message text is required!'), 'success': False}, status=200)

            if len(title) <= 3:
                return JsonResponse({'message': _('Invalid name'), 'success': False}, status=200)
            

            Form_message.objects.create(title=title, email=email, message=message, company=company, call_num=call_num)
            return JsonResponse({'message': _('Xabar qabul qilindi.'), 'success': True})
        
        except Exception as e:
            print(e)
            return JsonResponse({'message': str(e), 'success': False}, status=200)
        
    # def get(self,request):
    #     return HttpResponseRedirect('/')