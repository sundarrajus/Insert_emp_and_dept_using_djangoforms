from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_emp(request):
    EEFO=EmpForms()
    d={'EEFO':EEFO}
    if request.method=='POST':
        EFDO=EmpForms(request.POST)
        if EFDO.is_valid():
            eno=EFDO.cleaned_data['empno']
            en=EFDO.cleaned_data['ename']
            j=EFDO.cleaned_data['job']
            s=EFDO.cleaned_data['sal']
            com=EFDO.cleaned_data['comm']
            hi=EFDO.cleaned_data['hiredate']
            dept=EFDO.cleaned_data['deptno']
            m=EFDO.cleaned_data['mgr']
            TEO=Emp.objects.get_or_create(empno=eno,ename=en,job=j,sal=s,comm=com,hiredate=hi,deptno=dept,mgr=m)
            if TEO[1]:
                return HttpResponse('Created')
            return HttpResponse('already exists')
        else:
            return HttpResponse('invalid')
    return render(request,'insert_emp.html',d)

def insert_dept(request):
    EDFO=DeptForms()
    d={'EDFO':EDFO}
    if request.method=='POST':
        DFDO=DeptForms(request.POST)
        if DFDO.is_valid():
            dno=DFDO.cleaned_data['deptno']
            dn=DFDO.cleaned_data['dname']
            dl=DFDO.cleaned_data['dlocation']
            
            TEO=Dept.objects.get_or_create(deptno=dno,dname=dn,dlocation=dl)
            if TEO[1]:
                return HttpResponse('Created')
            return HttpResponse('already exists')
        else:
            return HttpResponse('invalid')
    return render(request,'insert_dept.html',d)