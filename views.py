# I have created this file - Supriyo

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# #def index(request):
# #    return HttpResponse('''<h1>Websites</h1> <p><a href="https://youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" target="blank">Django Playlist (Code With Harry)</a></p>
# #    <p><a href="https://www.w3schools.com/django/" target="blank">Django (w3school)</a><p>''')
#
# #def about(request):
# #    return HttpResponse("<h1>About Supriyo<h1>")
#
def index(request):
#     # return HttpResponse("<h1>Home</h1> <p><a href='/removepunc'>Remove Punctuation</a><p>"
#     #                     "<p><a href='/capatalizefirst'>Capitalize First</a><p>"
#     #                     "<p><a href='/newlineremove'>New Line Remove</a><p>"
#     #                     "<p><a href='/spaceremove'>Space Remove</a><p>"
#     #                     "<p><a href='/charcount'>Character Count</a><p>"
#     #                     )
#     prems = {'name': 'Sanu', 'place': 'Hooghly'}
     return render(request, 'index.html')
#
def analizetext(request):
    djtext = request.POST.get('text', 'default')
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    textcount = request.POST.get('textcount', 'off')

    if(removepunc == "on"):
        analized = ""
        for char in djtext:
            if char not in punctuations:
                analized = analized + char
        djtext = analized

    if(capitalize == "on"):
        analized = djtext.upper()
        djtext = analized

    if(newlineremover == "on"):
        analized = ""
        for char in djtext:
            if(char != '\n' and char != '\r'):
                analized = analized + char
        djtext = analized

    if(extraspaceremover == "on"):
        analized = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analized = analized + char
        djtext = analized

    if(textcount == "on"):
        lowercase = 0
        uppercase = 0
        num = 0
        spec_char = 0
        word = 0
        for char in djtext:
            if('a' <= char <= 'z'):
                lowercase = lowercase+1
            elif('A' <= char <= 'Z'):
                uppercase = uppercase + 1
            elif ('0' <= char <= '9'):
                num = num + 1
            elif(char in punctuations):
                spec_char = spec_char + 1
            else:
                pass

            if(char == " "):
                word = word + 1
        total_count = uppercase + lowercase + num
        analized = f"Total letter: {total_count}  \
                    \nUppercase: {uppercase} \
                    \nLowercase: {lowercase} \
                    \nNumbers: {num} \
                    \nSpecial character: {spec_char} \
                    \nWord:  {word+1} \
                    \nOriginal Text: {djtext}"

    if(removepunc != 'on' and capitalize != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and textcount != 'on'):
        analized = "Sorry! some error occured"
        params = {'purpose': 'Error!', 'analize_text': analized}
        return render(request, 'analize.html', params)

    params = {'purpose': 'Analize Text', 'analize_text': analized}
    return render(request, 'analize.html', params)



def capatalizefirst(request):
    return HttpResponse("<h1>Capitalize Text</h1> <p><a href='/'>Home</a><p>")


def newlineremove(request):
    return HttpResponse("<h1>New Line Remove</h1> <p><a href='/'>Home</a><p>")

def spaceremove(request):
    return HttpResponse("<h1>Space Remove</h1> <p><a href='/'>Home</a><p>")

def charcount(request):
    return HttpResponse("<h1>Character Count</h1> <p><a href='/'>Home</a><p>")



def contact(request):
        # if request.method == 'POST':
        #     form = ContactForm(request.POST)
        #     if form.is_valid():
        #         subject = "Website Inquiry"
        #         body = {
        #             'first_name': form.cleaned_data['first_name'],
        #             'last_name': form.cleaned_data['last_name'],
        #             'email': form.cleaned_data['email_address'],
        #             'message': form.cleaned_data['message'],
        #         }
        #         message = "\n".join(body.values())
        #
        #         try:
        #             send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
        #         except BadHeaderError:
        #             return HttpResponse('Invalid header found.')
        return render(request, 'contact.html')
               # return redirect("/")

        # form = ContactForm()
        # return render(request, "contact.html", {'form': form})

# def switch_html(request):
#     djtext = request.Get.get('text', 'default')
#     return render(request, 'switch_html')

def personalnavigator(request):
    return render(request, 'navg.html')