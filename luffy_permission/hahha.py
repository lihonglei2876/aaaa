from django.conf import settings
def init_permission(request,obj):
    permission_query=obj.roles.all().filter(permissions__url__is=False).values('permissions__title',
                                                                               'permissions__url',
                                                                               'permissions__menu__name',
                                                                               'permissions__menu__icon',
                                                                               'permissions__menu__weight',
                                                                                'permissions__menu__id',).distinct()
    permission_list=[]
    menu_dict={}
    for item in permission_query:
        permission_list.append({'url':item['permissions__url']})
        menu_id=item.get('permissions__menu__id')
        if not menu_id:
            continue
        if menu_id not in menu_dict:
            menu_dict[menu_id]={'name':item['permissions__menu__name'],
                                'icon':item['permissions__menu__icon'],
                                'weight':item['permissions__menu__weight'],
                                'children':[{'title':item['permissions__title'],'url':item['permissions__url']}]}
        else:
            menu_dict[menu_id]['children'].append(
                {'title':item['persiions__title'],'url':item['permissions__url']}

            )
    request.session[settings.PERMISSION_SESSION_KEY]=permission_list
    request.session[settings.MENU_SESSION_KEY]=menu_dict