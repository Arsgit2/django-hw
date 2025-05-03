from django.shortcuts import render, redirect
from .forms import DocumentForm

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = DocumentForm()
    return render(request, 'upload_file.html', {'form': form})
