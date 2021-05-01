from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def registration_validator(self, postdata):
        errors = {}
        email_errors = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postdata['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters"
        if len(postdata['first_name']) < 2 or len(postdata['last_name']) < 2:
            errors['name'] = "Your first name and last name must be at least 2 characters"
        if not email_errors.match(postdata['email']):
            errors['email'] = 'Please enter valid email address'
        if postdata['password'] != postdata['confirm_password']:
            errors['password'] = 'Both passwords must match. Please try again.'
        return errors


    def login_validator(self, postData):
        errors = {}
        LoginUser = User.objects.filter(email=postData['login_email'])
        if len(LoginUser) > 0:
            if bcrypt.checkpw(postData['login_password'].encode(), LoginUser[0].password.encode()):
                print("Password Matches")
            else:
                errors['login_password'] = "Password is incorrect. Please try again."
        else:
            errors['login_email'] = "User with that email does not exist"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


class ProductManager(models.Manager):
    def prepreg_validator(self, postData):
        errors = {}
        if len(postData['prepreg_name']) < 1:
            errors['prepreg_name'] = "Please make sure the Prepreg Name/ID field is complete"
        if len(postData['tg']) < 1:
            errors['tg'] = "Please make sure the Tg field is complete"
        if len(postData['cure_temp']) < 1:
            errors['cure_temp'] = "Please make sure Cure/Processing Temperature field is complete"
        if len(postData['prepreg_processing']) < 1:
            errors['prepreg_processing'] = "Please make sure the Processing field is complete"
        if len(postData['omit']) < 1:
            errors['omit'] = "Please make sure the Omit Market Segment field is complete"
        if len(postData['resin_type']) < 1:
            errors['resin_type'] = "Please make sure the Resin Type field is complete if there is no Resin Type then put NA"
        return errors


    def carbon_fiber_validator(self, postData):
        errors = {}
        if len(postData['carbon_fiber_name']) < 1:
            errors['carbon_fiber_name'] = "Please make sure the Carbon Fiber Name/ID field is complete"
        if len(postData['tensile_modulus']) < 1:
            errors['tensile_modulus'] = "Please make sure the Tensile Modulus field is complete"
        if len(postData['tensile_strength']) < 1:
            errors['tensile_strength'] = "Please make sure the Tensile Strength field is complete"
        if len(postData['resin_matrix']) < 1:
            errors['resin_matrix'] = "Please make sure the Resin Matrix field is complete"
        if len(postData['carbon_fiber_processing']) < 1:
            errors['carbon_fiber_processing'] = "Please make sure the Processing field is complete"
        return errors

0
class Prepreg(models.Model):
    prepreg_name = models.CharField(max_length=10)
    tg = models.CharField(max_length=20)
    cure_temp = models.CharField(max_length=10)
    prepreg_processing = models.CharField(max_length=20)
    omit = models.CharField(max_length=20)
    resin_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()


class CarbonFiber(models.Model):
    carbon_fiber_name = models.CharField(max_length=10)
    tensile_modulus = models.CharField(max_length=20)
    tensile_strength = models.CharField(max_length=20)
    resin_matrix = models.CharField(max_length=20)
    carbon_fiber_processing = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()
