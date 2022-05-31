from django.shortcuts import render
from django.forms.models import model_to_dict

from app_1.models import Players, Category, Winners
from app_1.forms import PlayersForm, CategoryForm, WinnersForm

# Create your views here.
def index(request):
    return render(request, "app_1/index.html")

#------------------------------------------------------Players---------------------------------------------
def players(request):
    players = Players.objects.all()

    context_dict = {
        'players': players
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_1/players.html"
    )


def new_players(request):
    if request.method == 'POST':
        profesor_form = PlayersForm(request.POST)
        if profesor_form.is_valid():
            data = profesor_form.cleaned_data
            profesor = Players(
                name=data['name'],
                last_name=data['last_name'],
                position=data['position'],
            )
            profesor.save()

            players = Players.objects.all()
            context_dict = {
                'players': players
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_1/players.html"
            )
    players_form = PlayersForm(request.POST)
    context_dict = {
        'players_form': players_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_1/new_player.html'
    )


def player_edit(request, pk: int):
    player = Players.objects.get(pk=pk)

    if request.method == 'POST':
        player_form = PlayersForm(request.POST)
        if player_form.is_valid():
            data = player_form.cleaned_data
            player.name = data['name']
            player.last_name = data['last_name']
            player.position = data['position']
            player.save()

            players = Players.objects.all()
            context_dict = {
                'players': players
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_1/players.html"
            )

    player_form = PlayersForm(model_to_dict(player))
    context_dict = {
        'player': player,
        'player_form': player_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_1/edit_player.html'
    )


def delete_player(request, pk: int):
    player = Players.objects.get(pk=pk)
    if request.method == 'POST':
        player.delete()

        players = Players.objects.all()
        context_dict = {
            'players': players
        }
        return render(
            request=request,
            context=context_dict,
            template_name="app_1/players.html"
        )

    context_dict = {
        'player': player,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_1/delete_player.html'
    )

#------------------------------------------------Category--------------------------------------------------
def category(request):
    category = Category.objects.all()

    context_dict = {
        'category': category
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_1/category.html"
    )


def new_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            data = category_form.cleaned_data
            course = Category(category=data['category'], n_category=data['n_category'])
            course.save()

            category = Category.objects.all()
            context_dict = {
                'category': category
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_1/category.html"
            )

    category_form = CategoryForm(request.POST)
    context_dict = {
        'category_form': category_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_1/new_category.html'
    )


def delete_category(request, pk: int):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()

        category = Category.objects.all()
        context_dict = {
            'category': category
        }
        return render(
            request=request,
            context=context_dict,
            template_name="app_1/category.html"
        )

    context_dict = {
        'category': category,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_1/delete_category.html'
    )


def category_edit(request, pk: int):
    category = Category.objects.get(pk=pk)

    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            data = category_form.cleaned_data
            category.category = data['category']
            category.n_category = data['n_category']
            category.save()

            category = Category.objects.all()
            context_dict = {
                'category': category
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_1/category.html"
            )

    category_form = CategoryForm(model_to_dict(category))
    context_dict = {
        'category': category,
        'category_form': category_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_1/edit_category.html'
    )

#----------------------------------------Winners-------------------------------------------------------------
def winners(request):
    winners = Winners.objects.all()

    context_dict = {
        'winners': winners
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_1/winners.html"
    )


def new_winners(request):
    if request.method == 'POST':
        winners_form = WinnersForm(request.POST)
        if winners_form.is_valid():
            data = winners_form.cleaned_data
            winners = Winners(name_couple=data['name_couple'])
            winners.save()

            winners = Winners.objects.all()
            context_dict = {
                'winners': winners
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_1/winners.html"
            )

    winners_form = WinnersForm(request.POST)
    context_dict = {
        'winners_form': winners_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_1/new_winners.html'
    )


def delete_winners(request, pk: int):
    winners = Winners.objects.get(pk=pk)
    if request.method == 'POST':
        winners.delete()

        winners = Winners.objects.all()
        context_dict = {
            'winners': winners
        }
        return render(
            request=request,
            context=context_dict,
            template_name="app_1/winners.html"
        )

    context_dict = {
        'winners': winners,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_1/delete_winners.html'
    )


def winners_edit(request, pk: int):
    winners = Winners.objects.get(pk=pk)

    if request.method == 'POST':
        winners_form = WinnersForm(request.POST)
        if winners_form.is_valid():
            data = winners_form.cleaned_data
            winners.name_couple = data['name_couple']
            winners.save()

            winners = Winners.objects.all()
            context_dict = {
                'winners': winners
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_1/winners.html"
            )

    winners_form = WinnersForm(model_to_dict(winners))
    context_dict = {
        'winners': winners,
        'winners_form': winners_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_1/edit_category.html'
    )