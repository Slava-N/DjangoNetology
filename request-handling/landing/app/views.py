from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()


def index(request):
    landing_name = request.GET.get('from-landing')
    counter_click[landing_name] += 1

    return render_to_response('index.html')

def landing(request):
    dict_renders = {'original': 'landing.html',
                    'test': 'landing_alternate.html'}
    ab_argument = request.GET.get('ab-test-arg')
    counter_show[ab_argument] += 1

    return render_to_response(dict_renders.get(ab_argument, ''))


def stats(request):
    test_conversion = counter_click['test'] / counter_show['test'] if counter_show['test'] else 0
    original_conversion = counter_click ['original'] / counter_show['original'] if counter_show['original'] else 0

    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
