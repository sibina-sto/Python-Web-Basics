from django.shortcuts import render, redirect

from GamesPlay_App.web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from GamesPlay_App.web.models import Profile, Game


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]


def show_index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context)


def show_dashboard(request):
    profile = get_profile()
    games = Game.objects.all()

    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'dashboard.html', context)


def create_game(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateGameForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'create-game.html', context)


def show_game_details(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
        'profile': profile,
    }
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditGameForm(instance=game)

    context = {
        'form': form,
        'game': game,
        'profile': profile,
    }
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=game)

    context = {
        'form': form,
        'game': game,
        'profile': profile,
    }
    return render(request, 'delete-game.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'create-profile.html', context)


def show_profile_details(request):
    profile = get_profile()
    games = Game.objects.all()
    games_count = len(games)
    if games:
        average_rating = sum(game.rating for game in games) / games_count
    else:
        average_rating = 0
    context = {
        'profile': profile,
        'games_count': games_count,
        'average_rating': average_rating,
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)
