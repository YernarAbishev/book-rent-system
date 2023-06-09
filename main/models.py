
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Book(models.Model):
    title = models.CharField("Кітап атауы", max_length=255)
    author = models.CharField("Автор", max_length=50)
    description = models.TextField("Сипаттамасы", blank=True, null=True)
    category = models.CharField("Жанр", max_length=255, blank=True, null=True)
    price = models.IntegerField("Бағасы")
    quantity = models.IntegerField("Дана")
    img = models.ImageField("Суреті", upload_to='books', null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Кітап"
        verbose_name_plural = "Кітаптар"


class MyCustomerManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, phone='0', address=None):
        if not email:
            raise ValueError('Пайдаланушының электрондық поштасы болуы керек')
        if not username:
            raise ValueError('Пайдаланушылардың логині болуы керек')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, password):
        user = self.create_user(
            email=str(username + '@gmail.com'),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    phone = models.CharField(max_length=10, default='0')
    deposite = models.IntegerField(blank=True, default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyCustomerManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Тапсырыс беруші"
        verbose_name_plural = "Тапсырыс берушілер"


class Address(models.Model):
    first_name = models.CharField(max_length=30, default=None)
    last_name = models.CharField(max_length=30, default=None)
    add_ln1 = models.CharField(max_length=100)
    add_ln2 = models.CharField(max_length=100, default=None)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    phone = models.CharField(max_length=10, default=None)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.add_ln1}"

    class Meta:
        verbose_name = "Мекен-жай"
        verbose_name_plural = "Мекен-жайлар"
        


class Payment(models.Model):
    amount = models.IntegerField()
    payment_time = models.DateTimeField(auto_now=True, null=True)
    is_succeed = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.amount} - {self.payment_time}"

    class Meta:
        verbose_name = "Төлем"
        verbose_name_plural = "Төлемдер"
        
