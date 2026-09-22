from django.shortcuts import render
from django.views.generic import View
from crm.models import Employee
from django.http import JsonResponse
from json import loads
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeListCreateView(View):
    def get(self,request):
        qs=Employee.objects.all().values() #values is used to get specific field
        employee_list=list(qs)      
        return JsonResponse(employee_list,safe=False) #convert python-native type to json

    def post(self,request):
        form_data=loads(request.body)
        """
                {
            "name":"zayn",
            "department":"sales",
            "salary":45000,
            "location":"tvm",
            "email":"zayn@gmail.com"
        }
                
       """
        Employee.objects.create(
            name=form_data.get("name"),
            department=form_data.get("department"),
            salary=form_data.get("salary"),
            location=form_data.get("location"),
            email=form_data.get("email"),
        )
        response_data={"message":"employee are added..."}
        return JsonResponse(response_data)

class EmployeeRetreiveUpdateDeleteView(View):
    def get(self,request,pk=None):
        qs=Employee.objects.filter(id=pk).values()
        employee_detail=list(qs)
        return JsonResponse(employee_detail,safe=False)