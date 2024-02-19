# # converter/views.py
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import ConvertedFile
from .utils import convert_pdf_to_word
import os

def convert_file(request):
    converted_files = ConvertedFile.objects.all()

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['file']
            converted_file_path = convert_pdf_to_word(pdf_file)
            
            # Save the original and converted files to the database
            instance = form.save(commit=False)
            instance.converted_file.save(
                name=f'{pdf_file.name.replace("pdf", "docx")}',
                content=converted_file_path,
            )
            instance.save()

            return redirect('convert_file')
    else:
        form = FileUploadForm()

    return render(request, 'converter/convert_file.html', {'form': form, 'converted_files': converted_files})

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def view_converted_file(request, file_id):
    converted_file = get_object_or_404(ConvertedFile, id=file_id)
    with open(converted_file.converted_file.path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'inline; filename={converted_file.converted_file.name}'
        return response

# converter/views.py


# views.py

from django.shortcuts import render

def your_view(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'converter/home.html')

def about(request):
    return render(request, 'converter/about.html')

def contact(request):
    return render(request, 'converter/contact.html')