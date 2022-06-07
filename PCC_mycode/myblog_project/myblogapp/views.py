from django.shortcuts import render, redirect

from myblogapp.models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def index(request):
    """The homepage for myblogapp."""
    return render(request, 'myblogapp/index.html')

def titles(request):
    """Shows all title of blog entries."""
    titles = BlogPost.objects.order_by('date_added')
    context = {'titles': titles}
    return render(request, 'myblogapp/titles.html', context)

def entry(request, entry_id):
    """Display title, date and text of a blog entry."""
    entry = BlogPost.objects.get(id=entry_id)
    context = {'entry': entry}
    return render(request, 'myblogapp/entry.html', context)

def new_entry(request):
    """Add a new Blog entry."""
    if request.method != 'POST': 
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else: 
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('myblogapp:titles')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'myblogapp/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = BlogPost.objects.get(id=entry_id)
    if request.method != 'POST':
        # Initial request; pre-fill the form with the current entry.
        form = BlogPostForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('myblogapp:entry', entry_id=entry_id)
    
    context = {'entry': entry, 'form': form}
    return render(request, 'myblogapp/edit_entry.html', context)