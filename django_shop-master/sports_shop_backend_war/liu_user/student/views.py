from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
# 在views.py文件中导入数据模型类
from .models import Student

# Create your views here.
def index(request):
    return render(request,'index.html')

# 增加数据
def add_student(request):
    # save方法
    student = Student()
    student.name = 'Tom'
    student.age = 18
    student.save()
    return HttpResponse('增加数据成功')
# 查询数据
def query_student(request):
    # all
    students = Student.objects.all()

    return JsonResponse(students)