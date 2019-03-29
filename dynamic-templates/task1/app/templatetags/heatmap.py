from django import template
import math

register = template.Library()

@register.filter
def heatmap(value):
    # print(float(value))
    try:
        intencivity = -math.log((abs(float(value))), 10) * 255
        color_schemes = [[255,intencivity,intencivity],[intencivity,255,intencivity],[255,255,255]]
        if float(value) > 0:
            base_color = color_schemes[0]
        elif float(value) < 0:
            base_color = color_schemes[1]
        else:
            base_color = color_schemes[2]
    except:
        base_color = [255,255,255]

    color_name = "RGB({0},{1},{2})".format(*base_color)
    print(color_name)
    return color_name
