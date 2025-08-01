from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Model For Category
class Category(models.Model):
    category_name=models.CharField(max_length=256,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.category_name
#Model For Product
class Product(models.Model):
    product_name=models.CharField(max_length=256,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images",null=True)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=256,null=True)

    def __str__(self):
        return self.product_name
#Model For Cart
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    quantity=models.PositiveIntegerField(default=1)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=256,choices=options,default="in-cart")
    def __str__(self):
        return self.product
#Model For Order
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    options=(
        ("order-placed","order-placed"),
        ("dispatched","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        # ("order-pending","order-pending"),
        # ("order-completed","order-completed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=256,choices=options,default="order-placed")
    delivery_address=models.CharField(max_length=256,null=True)
    def __str__(self):
        return self.product
#Model For Review
class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=256)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    def __str__(self):
        return self.comment
    









