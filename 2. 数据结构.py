data = {'permissions__title': '客户管理', 'permissions__url': '/customer/list/', 'permissions__menu__name': '信息管理',
        'permissions__menu__icon': 'fa-clipboard', 'permissions__menu__id': 1}, {'permissions__title': '添加客户',
                                                                                 'permissions__url': '/customer/add/',
                                                                                 'permissions__menu__name': None,
                                                                                 'permissions__menu__icon': None,
                                                                                 'permissions__menu__id': None}, {
           'permissions__title': '编辑客户', 'permissions__url': '/customer/edit/(\\d+)/', 'permissions__menu__name': None,
           'permissions__menu__icon': None, 'permissions__menu__id': None}, {'permissions__title': '删除客户',
                                                                             'permissions__url': '/customer/del/(\\d+)/',
                                                                             'permissions__menu__name': None,
                                                                             'permissions__menu__icon': None,
                                                                             'permissions__menu__id': None}, {
           'permissions__title': '财务管理', 'permissions__url': '/payment/list/', 'permissions__menu__name': '金融管理',
           'permissions__menu__icon': 'fa-clipboard', 'permissions__menu__id': 2}, {'permissions__title': '增加缴费',
                                                                                    'permissions__url': '/payment/add/',
                                                                                    'permissions__menu__name': None,
                                                                                    'permissions__menu__icon': None,
                                                                                    'permissions__menu__id': None}, {
           'permissions__title': '编辑缴费', 'permissions__url': '/payment/edit/(\\d+)/', 'permissions__menu__name': None,
           'permissions__menu__icon': None, 'permissions__menu__id': None}, {'permissions__title': '删除缴费',
                                                                             'permissions__url': '/payment/del/(\\d+)/',
                                                                             'permissions__menu__name': None,
                                                                             'permissions__menu__icon': None,
                                                                             'permissions__menu__id': None}

"""
{
    1: {
        'name': 信息管理,
        'icon': 'fa-sssss',
        'children': [
            {'title': 客户管理, 'url': '/customer/list/'},
            {'title': 用户管理, 'url': '/user/list/'}
        ]

    }
}
"""

menu_dict = {}

for item in data:
    menu_id = item.get('permissions__menu__id')

    if not menu_id:
        continue

    if menu_id not in menu_dict:
        menu_dict[menu_id] = {'name': item['permissions__menu__name'], 'icon': item['permissions__menu__icon'],
                              'children': [{'title': item['permissions__title'], 'url': item['permissions__url']}]}
    else:
        menu_dict[menu_id]['children'].append({'title': item['permissions__title'], 'url': item['permissions__url']})

print(menu_dict)
