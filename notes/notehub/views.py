from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    notes = Note.objects.all().order_by('-created_at')
    context = {
        'notes': notes,
    }
    return render(request,'notehub/index.html',context)

@login_required
def my_notes(request):
    notes = Note.objects.filter(author=request.user)
    context = {
        'notes':notes
    }

    return render(request,'notehub/my_notes.html',context)

@login_required
def create_note_view(request):
    if request.method == 'POST':
        form = CreateForm(request.POST,request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            note.categories.set(form.cleaned_data['categories'])
            return redirect('notehub:my-notes')
    else:
        form = CreateForm()

    return render(request,'notehub/create_notes.html',{'form':form})


@login_required
def edit_note_view(request,slug):
    note = get_object_or_404(Note, slug=slug, author=request.user)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notehub:my-notes')
    else:
        form = EditForm(instance=note)
    
    return render(request,'notehub/edit_notes.html',{'form':form})


@login_required
def delete_note_view(request,slug):
    note = get_object_or_404(Note,slug=slug, author=request.user)
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            note.delete()
            return redirect('notehub:my-notes')
    else:
        form = DeleteForm()
    return render(request,'notehub/delete_note.html',{'form':form})


def category_note_view(request,slug):
    categories = get_object_or_404(Category, slug=slug)
    notes = Note.objects.filter(categories=categories).order_by('-created_at')

    return render(request,'notehub/category_notes.html',{'notes':notes,'categories':categories})


