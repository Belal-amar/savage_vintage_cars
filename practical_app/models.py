from django.db import models
import re
# Create your models here.

class DealerManager(models.Manager):
    def dealer_validator(self,postData):
        errors={}
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not postData['fname']:
            errors["missing_field_first_name"]="please fill in First name."
        else:
            if len(postData['fname']) < 2:
                errors["first_name_length"]="First name should be at least 2 charchters"

        if not postData['lname']:
            errors["missing_field_last_name"]="please fill in Last name."
        else:
            if len(postData['lname']) < 2:
                errors["last_name_length"]="Last name should be at least 2 charchters"

        if not postData['email']:
            errors["missing_field_email"]="please fill in Email."
        else:
            if not EMAIL_REGEX.match(postData['email']):
                errors["email"]="invalid Email address!"

        if not postData['password'] or not postData['c_pw']:
            errors["missing_field_password"]="Please enter password & confirm password"
        else:
            if len(postData['password']) <8:
                errors["password_length"]="password should be at least 8 charachters"

            else:
                if postData['password']!=postData['c_pw']:
                    errors["password_confirm"]="password not match!"

        users = Dealer.objects.filter(email = postData['email'])
        if users:
            errors['Email']="The email is alredy exist !"


        return errors
        
    def login_validator(self,postData):
        errors={}
        if not postData['email']:
            errors["confirm"]="Invalid Email or Password"

        return errors



class CarManager(models.Manager):  
    def car_validator(self,postData):
        errors2= []
        if not postData['price']:
            errors2.append("please fill in Price.")
        else:
            if len(postData['price']) <=0:
                errors2.append("Price should be greater than 0")
        if not postData['year']:
            errors2.append("please fill in year.")
        else:
            if len(postData['year']) <=0 :
                errors2.append("year should be greater than zero")
        if len(postData['desc']) <10:
                errors2.append("description should be at least 10 charachters")

        



class Dealer(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DealerManager()


class Car(models.Model):
    price=models.IntegerField()
    model=models.CharField(max_length=250)
    make=models.CharField(max_length=250)
    year=models.IntegerField()
    desc=models.CharField(max_length=250)
    status=models.CharField(max_length=200,default="For Sale")
    dealer_id=models.ForeignKey(Dealer,related_name='pub_cars',on_delete=models.CASCADE)
    seller_con=models.CharField(max_length=40,default="0598921999")
    objects=CarManager()