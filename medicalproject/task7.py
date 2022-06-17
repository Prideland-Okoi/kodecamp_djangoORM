from home.models import People, Product

# I. Insert a new record into the Product Model
new_product = Product(product_name = "Beecham Amoxil", product_price = 1000)
new_product.save()

#Assigns chris record to a1
a1 = People.objects.get(user_name = "Joshua")

#select a buyer for the product
new_product.buyers.add(a1)



# II. get all the product
Product.objects.all()

# III. Filter products by their name
Product.objects.filter(product_name = "Beecham Amoxil")

# IV. Get a single record from the product table
new_price = Product.objects.get(pk = 4)
#displays current price
new_price.product_price 

# V. Change a product price

new_price.product_price = 1900
new_price.save()I
