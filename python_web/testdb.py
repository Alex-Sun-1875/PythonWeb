# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

"""
# 数据库操作
def testdb(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过 objects 这个模型管理器的 all()获得所有数据航,相当于 sql 中的 select * from
    list = Test.objects.all()

    # filter 相当于 sql 中的 where,可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据,相当于 sql 中的 offset 0 limit 2
    Test.objects.order_by('name')[0:2]

    # 数据排序
    Test.objects.order_by('id')

    # 上面的方法可以连锁使用
    Test.objects.filter(name='test_db').order_by('id')

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
"""

"""
def testdb(request):
    # 修改 id = 1  的 name 字段,再 save,相当于 sql 中的 update
    test1 = Test.objects.get(id=1)
    test1.name = "Google"
    test1.save()

    # 另外一种方式
    Test.objects.filter(id=2).update(name='Apple')

    # 修改所有的列
    # Test.object.all().update(name="MicroSoft")

    response = ""
    
    list = Test.objects.all()
    for var in list[0:2]:
        response += "<p>" + var.name + "</p>"

    return HttpResponse("<p>" + response + "</p>")
"""

def testdb(request):
    # 删除 id=1 的数据
    # test1 = Test.objects.get(id=1)
    # test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")