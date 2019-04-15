data = {
    1: {
        'name': '信息管理',
        'icon': 'fa-sssss',
        'weight': 100,
        'children': [
            {'title': '客户管理', 'url': '/customer/list/'},
            {'title': '用户管理', 'url': '/user/list/'}
        ]

    },
    2: {
        'name': '金融管理',
        'icon': 'fa-sssss',
        'weight': 10000,
        'children': [
            {'title': '客户管理', 'url': '/customer/list/'},
            {'title': '用户管理', 'url': '/user/list/'}
        ]

    }
}
ret = sorted(data,key=lambda i:data[i]['weight'],reverse=True)
print(ret)

from collections import OrderedDict
order_dic = OrderedDict()
for i in sorted(data, key=lambda i: data[i]['weight'], reverse=True):
    order_dic[i] = data[i]

print(order_dic)
