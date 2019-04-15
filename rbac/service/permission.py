from django.conf import settings


def init_permission(request, obj):
    # 保存权限信息
    # 查询
    permission_query = obj.roles.all().filter(permissions__url__isnull=False).values('permissions__title',
                                                                                     'permissions__url',
                                                                                     'permissions__menu__name',
                                                                                     'permissions__menu__icon',
                                                                                     'permissions__menu__weight',
                                                                                     'permissions__menu__id',
                                                                                     ).distinct()

    print(permission_query)
    # 存放权限信息的列表
    permission_list = []
    # 存放菜单信息的列表
    menu_dict = {}

    for item in permission_query:
        # 将权限信息放入permission_list
        permission_list.append({'url': item['permissions__url']})

        # 放入菜单信息
        menu_id = item.get('permissions__menu__id')

        # 不是菜单
        if not menu_id:
            continue

        if menu_id not in menu_dict:
            menu_dict[menu_id] = {'name': item['permissions__menu__name'],
                                  'icon': item['permissions__menu__icon'],
                                  'weight': item['permissions__menu__weight'],
                                  'children': [{'title': item['permissions__title'], 'url': item['permissions__url']}]}
        else:
            menu_dict[menu_id]['children'].append(
                {'title': item['permissions__title'], 'url': item['permissions__url']})

    # 权限信息放入session
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list

    # 菜单信息放入session
    request.session[settings.MENU_SESSION_KEY] = menu_dict
