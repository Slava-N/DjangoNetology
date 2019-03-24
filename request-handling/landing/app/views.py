from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    landing_name = request.GET.get('from-landing')
    counter_click[landing_name] += 1
    print(counter_click)
    return render_to_response('index.html')

def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    ab_argument = request.GET.get('ab-test-arg')
    # render_variable = 'landing.html'

    if ab_argument == 'original':
        render_variable = 'landing.html'

    elif ab_argument == 'test':
        render_variable = 'landing_alternate.html'

    counter_show[ab_argument] += 1
    print('SHOW',counter_show)
    return render_to_response(render_variable)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    try:
        test_conversion = counter_click ['test'] / counter_show['test']
    except BaseException:
        test_conversion = 0

    try:
        original_conversion = counter_click ['original'] / counter_show['original']
    except BaseException:
        original_conversion = 0


    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
