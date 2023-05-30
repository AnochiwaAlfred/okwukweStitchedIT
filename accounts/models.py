from django.db import models
from orders.models import Order
from products.models import Product
from orderitems.models import OrderItem
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Group

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
        username=username,
        email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
        email=email,
        username=username,
        password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user




class MyUser(AbstractBaseUser):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name='Email Address', max_length=255, unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER, blank=False)
    password = models.CharField(max_length=100, blank=False)
    profile_pics = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    cart = models.ManyToManyField(OrderItem, blank=True, related_name='cart')
    wishList = models.ManyToManyField(Product, blank=True, related_name='wishList')
    newsLetterSub = models.BooleanField(verbose_name='Subscription Status',default=False, blank=True, null=False)
    newsLetterEmail = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    
    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, pings):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    class Meta:
        verbose_name = 'User'
