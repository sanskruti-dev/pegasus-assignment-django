from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Music, Folder
from .forms import MusicForm, FolderForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def home(request):
    # music_tracks = Music.objects.all()
    # return render(request, 'music/home.html', {'music_tracks': music_tracks})
    music_tracks = Music.objects.all()
    folders = Folder.objects.filter(owner=request.user) if request.user.is_authenticated else []
    favorite_tracks = Music.objects.filter(favorited_by=request.user) if request.user.is_authenticated else []
    return render(request, 'music/home.html', {
        'music_tracks': music_tracks,
        'folders': folders,
        'favorite_tracks': favorite_tracks,
    })

@login_required
def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.owner = request.user
            folder.save()
            return redirect('home')
    else:
        form = FolderForm()
    return render(request, 'music/create_folder.html', {'form': form})

@login_required
def update_folder(request, pk):
    folder = get_object_or_404(Folder, pk=pk)
    if request.user != folder.owner:
        return redirect('home')
    if request.method == 'POST':
        form = FolderForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()
            return redirect('folder_detail', pk=folder.pk)
    else:
        form = FolderForm(instance=folder)
    return render(request, 'music/update_folder.html', {'form': form})

@login_required
def delete_folder(request, pk):
    folder = get_object_or_404(Folder, pk=pk)
    if request.user == folder.owner:
        folder.delete()
    return redirect('home')

@login_required
def add_music_to_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save()
            folder.music_tracks.add(music)
            return redirect('home')
    else:
        form = MusicForm()
    return render(request, 'music/add_music.html', {'form': form, 'folder': folder})

@login_required
def favorite_music(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    if request.user in music.favorited_by.all():
        music.favorited_by.remove(request.user)
    else:
        music.favorited_by.add(request.user)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def create_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MusicForm()
    return render(request, 'music/add_music.html', {'form': form})

@login_required
def update_music(request, pk):
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES, instance=music)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MusicForm(instance=music)
    return render(request, 'music/update_music.html', {'form': form})

@login_required
def delete_music(request, pk):
    music = get_object_or_404(Music, pk=pk)
    music.delete()
    return redirect('home')
