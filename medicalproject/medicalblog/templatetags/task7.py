from dataclasses import field
from django import template
from ..models import Post

register = template.Library()
@register.filter
def new_record():
    return Post.objects.filter()


#insert a new record into the Product Model
#Get all the records in the product table

#Filter products by their name

#Get a single record from the product table

#Change a product price

#NB. Use the .save() method where necessary