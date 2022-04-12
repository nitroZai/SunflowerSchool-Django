from multiprocessing import context
from student.models import Student
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'home.html')


def admission(request):
    return render(request, 'newadmin.html')


def success(request):
    data = request

    first_name = request.POST['fname']
    last_name = request.POST['lname']
    DOB = request.POST['dob']
    parent_name = request.POST['pname']
    address = request.POST['address']
    phone = request.POST['phone']
    email = request.POST.get('email')
    branch = request.POST['branch']
    java = request.POST['java']
    python = request.POST['python']
    sql = request.POST['sql']
    picture = request.FILES['picture']

    print(picture.name)
    print(picture.size)

    fss = FileSystemStorage()
    file = fss.save(picture.name, picture)
    file_url = fss.url(file)

    student = Student()
    student.first_name = first_name
    student.last_name = last_name
    student.DOB = DOB
    student.parent_name = parent_name
    student.address = address
    student.phone = (phone)
    student.email = email
    student.java = java
    student.python = python
    student.sql = sql
    student.branch = branch
    student.picture = file_url
    student.save()

    context = {
        'first_name': first_name
    }

    return render(request, 'admission-success.html', context)


def marks(request, id):
    student = Student.objects.get(pk=id)
    context = {
        'student': student
    }
    return render(request, 'specific_profile.html', context)


def complete(request):
    students = Student.objects.all()
    return render(request, 'complete.html', {'students': students})


def completeFilter(request, branch):

    if branch == 'All':
        students = Student.objects.all()
    elif branch == 'CSE':
        students = Student.objects.all().filter(branch__icontains='CSE')
    elif branch == 'IT':
        students = Student.objects.all().filter(branch__icontains='IT')
    elif branch == 'ECE':
        students = Student.objects.all().filter(branch__icontains='ECE')
    else:
        students = None

    context = {
        'students': students
    }

    return render(request, 'complete.html', context)


def completeFilter_details(request, branch, id):

    student = Student.objects.get(
        branch=branch, id=id
    )

    context = {
        'student': student
    }

    return render(request, 'complete.html', context)


def search(request):

    searchVar = request.GET['searchText']

    try:
        student = Student.objects.get(pk=int(searchVar))
    except:
        return render(request, 'invalid-search.html')

    context = {
        'student': student
    }

    return render(request, 'search.html', context)
