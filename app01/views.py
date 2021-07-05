from django.shortcuts import render, redirect
from app01 import models


# 添加出版社
def add_publisher(request):
    if request.method == "POST":
        # 获取表单提交内容
        publisher_name = request.POST.get("name")
        publisher_address = request.POST.get("address")
        # 保存到数据库中
        models.publisher.objects.create(name=publisher_name, address=publisher_address)
        return redirect("/app01/publisher_list")
    return render(request, "add_publisher.html")


# 出版社列表页面
def publisher_list(request):
    # 查询数据库中的所有信息
    publisher_list = models.publisher.objects.all()
    return render(request, "publisher_list.html", {"publisher_obj_list": publisher_list})


# 出版社修改
def edit_publisher(request):
    if request.method == 'POST':
        # 1获取表单提交过来的内容
        id = request.POST.get('id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        # 2根据id 去数据库查找对象
        publisher_obj = models.publisher.objects.get(id=id)
        # 3修改
        publisher_obj.name = name
        publisher_obj.address = address
        publisher_obj.save()
        # 4重定向到出版社列表
        return redirect('/app01/publisher_list/')
    else:
        # 1获取id
        id = request.GET.get('id')
        # 2去数据库中查找相应的数据
        publisher_obj = models.publisher.objects.get(id=id)
        publisher_obj_list = models.publisher.objects.all()
        # 3返回页面
        return render(request, 'edit_publisher.html',
                      {"publisher_obj": publisher_obj, "publisher_obj_list": publisher_obj_list})


# 删除出版社
def delete_publisher(request):
    # 1获取删除图书的id
    id = request.GET.get("id")
    # 2 根据id删除数据库中的记录
    models.publisher.objects.filter(id=id).delete()
    return redirect("/app01/publisher_list")


# 图书列表
def book_list(request):
    # 获取图书信息
    book_obj_list = models.Book.objects.all()
    # 2.将数据放到页面上
    return render(request, 'book_list.html', {"book_obj_list": book_obj_list})
