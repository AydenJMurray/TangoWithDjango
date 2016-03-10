from django import template
from Rango.models import Category

register = template.Library()

@register.inclustion_tag('Rango/cats.html')
	def get_category_list():
		return{'cats': Category.objects.all()}