# Create your views here. 
#from django.shortcuts import render
#from django.http import HttpResponseRedirect
from trebble.models import Employee, Job, Contract, Company, CompanyForm
from django.shortcuts import render_to_response, get_object_or_404



def show_company_list(request, template_name="index.html"):
	company_list = Company.objects.order_by("name")
	return render_to_response(template_name,{'company_list':company_list})

def show_company(request,company_id, template_name="edit_company.html"):
	c = get_object_or_404(Company, id=company_id)			
	form = CompanyForm(instance=c)
	return render_to_response(template_name,{'form': form})

def add_company(request, template_name="add_company.html"):
	
	if request.method == 'POST':
		form = CompanyForm(request.POST)
		if form.is_valid():
			form.save()
			
			
	else:
		form = CompanyForm()
		return render_to_response(template_name,{'form': form})
	
	
"""

def index(request, template_name="index.html"):
	page_title = ''
	employees = Employee.all()
	companies = Company.all()
	contracts = Contract.all()
	jobs = Job.all()
	


def show_company(request, template_name="company.html"):
	try:
		company = Company.objects.get(name='company_name')
	except Company.DoesNotExist:
		print "This company is not existent"
	company_contracts = Contract.objects.filter(company=company_name)
	
		
		
	
	
def show_employees(request, template_name="employees.html")
	employees = Employee.all()
	return render_to_response(template_name,locals()) 
	
def update_employee(request, template_name="update_employee.html")
"""	