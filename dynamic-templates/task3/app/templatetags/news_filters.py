from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):

    # print(value)

    print()

    time_delta = ( datetime.now().timestamp() - value ) / 60

    value_new = time_delta
    value_new = {
               time_delta < 10: 'Только что',
        10 <= time_delta < 60 * 24:   '{0:0.0f} часов назад'.format(time_delta / 60),
          60 * 24 <= time_delta :  datetime.date(datetime.fromtimestamp(value))
       }[True]
    return value_new


# необходимо добавить фильтр для поля `score`


@register.filter
def popularity(value):


    value_new = {
        value < -5 : 'Очень плохо',
        -5 <= value <5: 'Нейтрально',
        5 <= value: 'Очень хорошо'
    }[True]

    return value_new



@register.filter
def format_num_comments(value):
    # Ваш код
    value_new = {
        value == 0 : 'Оставьте комментарий',
        0 < value <= 50: value,
        50 < value: '50+'
    }[True]

    return value_new


@register.filter
def format_selftext(value, count):
    value_split = value.split()
    print(value_split)
    value_raw = []
    value_raw.extend(value_split[:10])
    value_raw.append('...')
    value_raw.extend(value_split[-10:])
    print(value_raw)
    value_new = " ".join(value_raw)

    return value_new