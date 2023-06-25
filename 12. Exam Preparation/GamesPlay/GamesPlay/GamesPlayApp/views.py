from django.shortcuts import render, redirect

from GamesPlayApp.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, ProfileDeleteForm
from GamesPlayApp.models import ProfileModel, GameModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except:
        return None


def get_games():
    return GameModel.objects.all()


def get_game(pk):
    return GameModel.objects.filter(pk=pk).get()


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'base/home-page.html', context)


def dashboard(request):
    profile = get_profile()
    games = get_games()

    context = {
        'profile': profile,
        'games': games,
    }

    return render(request, 'base/dashboard.html', context)


def game_create(request):
    profile = get_profile()

    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'games/create-game.html', context)


def game_details(request, pk):
    profile = get_profile()
    game = get_game(pk)

    context = {
        'profile': profile,
        'game': game
    }

    return render(request, 'games/details-game.html', context)


def game_edit(request, pk):
    profile = get_profile()
    game = get_game(pk)

    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'games/edit-game.html', context)


def game_delete(request, pk):
    profile = get_profile()
    game = get_game(pk)

    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'games/delete-game.html', context)


def profile_create(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profiles/create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    games = get_games()
    average_rating = sum([g.rating for g in games]) / len(games) if len(games) > 0 else 0.0

    context = {
        'profile': profile,
        'games_length': len(games),
        'average_rating': average_rating
    }

    return render(request, 'profiles/details-profile.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    games = get_games()

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        form.save()
        for game in games:
            game_form = GameDeleteForm(request.POST, instance=game)
            game_form.save()
        return redirect('index')

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/delete-profile.html', context)
