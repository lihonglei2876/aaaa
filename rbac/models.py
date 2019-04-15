from django.db import models


class Menu(models.Model):
    """
    菜单表  一级菜单
    """
    name = models.CharField(max_length=32)
    icon = models.CharField(max_length=56, verbose_name='图标', blank=True, null=True)
    weight = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Permission(models.Model):
    """
    权限表
    是否管联一级菜单
    权限 关联   菜单  表示 当前的权限是二级菜单
    权限 不关联 菜单  表示 当前的权限不是菜单
    """
    url = models.CharField(max_length=256, verbose_name='权限', unique=True)
    title = models.CharField(max_length=32, verbose_name='标题')
    menu = models.ForeignKey('Menu', blank=True, null=True, )

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色表
    """
    name = models.CharField(max_length=32, verbose_name='角色名称')
    permissions = models.ManyToManyField('Permission', blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=32, verbose_name='用户名')
    pwd = models.CharField(max_length=32, verbose_name='密码')
    roles = models.ManyToManyField('Role', blank=True)

    def __str__(self):
        return self.name
