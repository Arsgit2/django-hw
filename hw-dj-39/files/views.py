
from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = UploadForm()
    files = UploadedFile.objects.all()
    return render(request, 'files/upload.html', {'form': form, 'files': files})
