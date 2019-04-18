from django.shortcuts import render
from collections import Counter
from .models import PlayerGameInfo, Player, Game
from django.utils import timezone

counter_players = Counter()
counter_game = 1000


def show_home(request):
    counter_players['player_number']

    player_id = request.session.get('player_id')
    request.session['player_id'] = 28
    # print(request.session['player_id'])

    if not player_id:
            if len(Player.objects.all()):
                highest_id_player = Player.objects.all().order_by("-id")[0]
                print(highest_id_player)
                current_player_id=int(highest_id_player.id) + 1
            else:
                current_player_id = 1
            player = Player.objects.create(player_id=current_player_id)
            request.session['player_id'] = player.player_id

    else:
        print(player_id)
        player = Player.objects.get(pk = player_id)

    if request.POST.get('set_number'):
        secret_number = request.POST.get('set_number')
        game = Game.objects.create(secret_number = secret_number, active = True, game_id = counter_game)
        player_action = PlayerGameInfo.objects.create(player = player, game = game, guess = False, time = timezone.now())



        print(request.POST.get('set_number'))



    return render(
        request,
        'set_number.html'
    )

def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                         "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN,
                        secure=settings.SESSION_COOKIE_SECURE or None)



def start_game(player_id):
    pass
