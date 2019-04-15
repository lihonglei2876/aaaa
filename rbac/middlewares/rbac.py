from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import HttpResponse, redirect, reverse
import re

class RbacMidlleware(MiddlewareMixin):

    def process_request(self, request):
        # 获取当前访问的url
        url = request.path_info

        # 白名单
        for i in settings.WHITE_LIST:
            if re.match(i, url):
                return

        # 获取权限信息
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        print(permission_list)

        # 登陆后没有权限
        if not permission_list:
            return redirect(reverse('login'))

        # 权限的校验
        for i in permission_list:
            if re.match("^{}$".format(i['url']), url):
                return

        return HttpResponse('没有访问权限')
