from django.contrib import admin

<<<<<<< HEAD
# Register your models here.
from .models import Post
admin.site.register(Post)
=======
from .models import People, Address, Doctor, Product, Bio

#from .models import People, Address, Doctor, Product, Bio

admin.site.register(People)
admin.site.register(Address)
admin.site.register(Doctor)
admin.site.register(Product)
admin.site.register(Bio)
>>>>>>> b4fa796 (task solved)
