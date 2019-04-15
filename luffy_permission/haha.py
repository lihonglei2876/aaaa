# from django.utils.deprecation import MiddlewareMixin
# from django.conf import settings
# from django.shortcuts import HttpResponse, redirect, reverse
# import re
#
#
# class RbacMidlleware(MiddlewareMixin):
#     def process_request(self,request):
#         url=request.path_info
#
#         for i in settings.WHITE_LIST:
#             if re.match(i,url):
#                 return
#         permission_list=request.session.get(settings.PERMISSION_SESSION_KEY)
#
#         if not permission_list:
#             return redirect(reverse('login'))
#
#
#         for i in permission_list:
#             if re.match('^{}$'.format(i['url']),url):
#                 return
#         return HttpResponse('没有访问权限')

class MyChar(models.Field):
    def __init__(self,max_lenght,*args,**kwargs):
        self.max_lenght=max_lenght
        super(MyChar,self).__init__(max_lenght=max_lenght,*args,**kwargs)
    def db_type(self,connection):
        return 'char(%s)'%self.max_lenght