from django.shortcuts import render
from collections import Counter
from .models import PlayerGameInfo, Player, Game

counter_players = Counter()


def show_home(request):
    counter_players['player_number']

    player_id = request.session.get('player_id')
    # print(request.POST.get('set_number'))
    # print()

    if not player_id:
            if len(Player.objects.all()):
                highest_id_player = Player.objects.all().order_by("-id")[0]
                print(highest_id_player)
                current_player_id=int(highest_id_player.id) + 1
            else:
                current_player_id = 1
            player = Player.objects.create(player_id=current_player_id)

    


    return render(
        request,
        'set_number.html'
    )

def start_game(player_id):
    pass
