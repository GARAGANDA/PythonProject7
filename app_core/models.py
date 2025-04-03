from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length = 20)
    price = models.DecimalField(decimal_places = 2, max_digits = 10)
    compounds = models.ManyToManyField("Compound", through = "DishCompound")
    def __str__(self):
        return self.name

class Compound(models.Model):
    name = models.CharField(max_length = 20)
    count = models.IntegerField()
    def __str__(self):
        return self.name

class Order(models.Model):
    waiter = models.ForeignKey("Waiter", on_delete = models.CASCADE)
    dishes = models.ManyToManyField("Dish")
    table = models.IntegerField()
    is_served = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.waiter.name+" | "+str(self.table)

class Check(models.Model):
    final_price = models.DecimalField(decimal_places = 2, max_digits = 10)
    orders = models.ManyToManyField("Order", through = "CheckOrder")
    is_paid = models.BooleanField()
    def __str__(self):
        return str(self.final_price)

class Waiter(models.Model):
    surname = models.CharField(max_length = 30)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length = 30, choices = [("Администратор", "Admin"),("Старший официант", "Senior_Waiter"),("Официант", "Waiter")])
    def __str__(self):
        return self.name

class DishCompound(models.Model):
    dish = models.ForeignKey("Dish", on_delete = models.CASCADE)
    compound = models.ForeignKey("Compound", on_delete = models.CASCADE)
    count = models.IntegerField()

class CheckOrder(models.Model):
    price_check = models.ForeignKey("Check", on_delete = models.CASCADE)
    order = models.ForeignKey("Order", unique = True, on_delete = models.CASCADE)