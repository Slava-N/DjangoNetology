from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):

    # print(value)

    print()

    time_delta = ( datetime.now().timestamp() - value ) / 60

    if time_delta < 10:
        value_new = 'Только что'
    elif time_delta < 60 * 24:
        value_new = '{0:0.0f} часов назад'.format(time_delta / 60)
    else:
        value_new = datetime.date(datetime.fromtimestamp(value))
    return value_new

@register.filter
def popularity(value):

    if value < -5:
        value_new = 'Очень плохо'
    elif value < 5:
        value_new = 'Нейтрально'
    else:
        value_new = 'Очень хорошо'

    return value_new



@register.filter
def format_num_comments(value):

    if value == 0:
        value_new = 'Оставьте комментарий'
    elif value <= 50:
        value_new = value
    else:
        value_new = '50+'

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