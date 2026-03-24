from django import forms
from app.models import *

class DeptForms(forms.Form):
    deptno=forms.IntegerField()
    dname=forms.CharField()
    dlocation=forms.CharField()



class EmpForms(forms.Form):
    empno=forms.IntegerField()
    ename=forms.CharField()
    job=forms.CharField()
    sal=forms.DecimalField()
    comm=forms.DecimalField()
    hiredate=forms.DateField()
    deptno=forms.ModelChoiceField(queryset=Dept.objects.all())
    mgr=forms.ModelChoiceField(queryset=Emp.objects.all())


class SalgradeForm(forms.Form):
    grade=forms.IntegerField()
    losal=forms.DecimalField()
    hisal=forms.DecimalField()