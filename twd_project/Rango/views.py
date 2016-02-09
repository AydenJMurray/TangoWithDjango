from django.shortcuts import render
from django.http import HttpResponse
from Rango.models import Category, Page
from Rango.forms import CategoryForm

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	popular_pages = Page.objects.order_by('-views')[:5]
	context_dict = {'categories': category_list, 'pages': popular_pages}
	return render(request, 'Rango/index.html', context_dict)
	
def about(request):
	return render(request, 'Rango/about.html')
	
def category(request, category_name_slug):
	context_dict = {}
	
	try:
		category = Category.objects.get(slug = category_name_slug)
		
		context_dict['category_name'] = category.name
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass
		
	return render(request, 'rango/category.html', context_dict)
	
def add_category(request):
	#HTTP Post??
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		
		#Checking form validity
		if form.is_valid():
			#save
			form.save(commit=True)
		
			return index(request)
		else:
			print form.errors
	else:
		form = CategoryForm()
	
	return render(request, 'rango/add_category.html', {'form':form})
		