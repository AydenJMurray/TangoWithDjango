from django.shortcuts import render
from django.http import HttpResponse
from Rango.models import Category, Page
from Rango.forms import CategoryForm
from Rango.forms import PageForm

def index(request):
	category_list = Category.objects.order_by('-likes')[:7]
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
		context_dict['slug'] = category_name_slug
		
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
	
def add_page(request, category_name_slug):

		try:
			cat = Category.objects.get(slug=category_name_slug)
		except Category.DoesNotExist:
				cat = None
		if request.method == 'POST':
			form = PageForm(request.POST)
			if form.is_valid():
				if cat:
					page = form.save(commit=False)
					page.category = cat
					page.views = 0
					page.save()
					return category(request, category_name_slug)
				
			else:
				print form.errors
		else:
			form = PageForm()
			
		context_dict = {'form':form, 'category':cat, 'slug': category_name_slug}
		
		return render(request, 'rango/add_page.html', context_dict)
				