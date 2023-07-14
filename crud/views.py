from django.shortcuts import render , HttpResponseRedirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def addShow(request):
    if request.method=='POST':
        fm = StudentForm(request.POST)
        fm.is_valid()
        nm = fm.cleaned_data['name']
        em = fm.cleaned_data['email']
        pw = fm.cleaned_data['password']

        st = Student(name=nm, email=em, password=pw)
        st.save()
        fm = StudentForm()

    else:
        fm = StudentForm()
    stu = Student.objects.all()
    return render(request, 'crud/addshow.html' , {'fm':fm , 'stu':stu})
def update_data(request , id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm= StudentForm(request.POST , instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm= StudentForm(instance=pi)
    return render(request,'crud/update.html',{'fm':fm})

def delete_data(request ,id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()

        return HttpResponseRedirect('/')