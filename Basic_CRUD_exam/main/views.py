from django.shortcuts import render, redirect

from Basic_CRUD_exam.main.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from Basic_CRUD_exam.main.models import Profile, Album


def get_profile():
    profile = Profile.objects.first()
    return profile


def home_page(request):
    profile = get_profile()
    album = Album.objects.all()
    if not profile:
        return redirect('profile create page')
    context = {
        'profile': profile,
        'albums': album,
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
        form = CreateProfileForm(request.POST)
        context = {
            'form': form,
            'no_profile': True,
        }
        return render(request, 'home-no-profile.html', context)
    form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def album_add(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
        form = CreateAlbumForm(request.POST)
        return render(request, 'add-album.html', {'form': form})
    form = CreateAlbumForm()
    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(id=pk)
    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = EditAlbumForm(instance=album)
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(instance=album)
        form.save()
        return redirect('home page')
    form = DeleteAlbumForm(instance=album)
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'delete-album.html', context)


def profile_page(request):
    albums = Album.objects.count()
    profile = get_profile()
    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == "POST":
        form = DeleteProfileForm(instance=profile)
        form.save()
        return redirect('home page')
    return render(request, 'profile-delete.html')
