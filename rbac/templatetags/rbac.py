from django import template
import re
from collections import OrderedDict

register = template.Library()

from django.conf import settings


# from luffy_permission import settings

@register.inclusion_tag('menu.html')
def menu(request):
    menu_dict = request.session.get(settings.MENU_SESSION_KEY)

    order_dic = OrderedDict()

    for key in sorted(menu_dict, key=lambda i: menu_dict[i]['weight'], reverse=True):

        order_dic[key] = item = menu_dict[key]

        item['class'] = 'hide'

        for i in item['children']:
            if re.match("^{}$".format(i['url']), request.path_info):
                i['class'] = 'active'
                item['class'] = ''
                break

    return {'menu_list': order_dic.values()}
