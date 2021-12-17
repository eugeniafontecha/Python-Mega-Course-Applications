from django.shortcuts import render
from . import translate
# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        output = translate.translate(original_text)
        return render(request, 'translator.html', {'original_text':original_text,'output_text':output})
    else: #get request
        return render(request, 'translator.html')