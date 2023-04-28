from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Cake(models.Model):
    name=models.CharField(max_length=200)
    option=(
        ("round","round"),
        ("square","square"),
        ("triangle","triangle")
    )
    shape=models.CharField(choices=option,null=True,max_length=100)
    layer=(
        ("1","1"),
        ("2","2"),
        ("3","3")
    )
    layers=models.CharField(choices=layer,null=False,max_length=100)
    image=models.ImageField(upload_to="images",null=True)
    weight=models.CharField(max_length=100)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Orders(models.Model):
    cake=models.ForeignKey(Cake,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    available_option=(
        ("order-placed","order-placed"),
        ("shipped","shipped"),
        ("in-cart","in-cart"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("return","return")
    )
    status=models.CharField(choices=available_option,default="order-placed",max_length=100)

class Cart(models.Model):
    cake=models.ForeignKey(Cake,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    status_update=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
    )
    status=models.CharField(choices=status_update,default="in-cart",max_length=100)

class Review(models.Model):
    cake=models.ForeignKey(Cake,on_delete=models.CASCADE,related_name="cakes")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=300)
    rating=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(5)])

    def __str__(self):
        return self.comment