from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Group(BaseModel):
    group_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='groups')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.group_name)

        super(Group, self).save(*args, **kwargs)

    def __str__(self):
        return self.group_name


class Product(BaseModel):
    class RatingChoices(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    product_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.ZERO.value, null=True, blank=True)
    discount = models.IntegerField(default=0)
    slug = models.SlugField(null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='products')
    users_like = models.ManyToManyField(User, related_name='users_like',blank=True,db_table='User_Like')
    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)

        return self.price

    @property
    def pay_monthly(self):
        return self.price / 12

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_images', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_images', null=True, blank=True)

    is_primary = models.BooleanField(default=False)
    class Meta:
        db_table = 'Image'

class Comment(BaseModel):

    class Reting(models.IntegerChoices):
        bir = 1
        ikki = 2
        uch = 3
        tort = 4
        besh = 5
    reting = models.IntegerField(choices=Reting.choices, default=0,null=True, blank=True)
    message = models.TextField(null=True,blank=True)
    file = models.FileField(upload_to='communts/',null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Attribute(models.Model):
    attribute_name = models.CharField(max_length=200)
    def __str__(self):
        return self.attribute_name
class AttributeValue(models.Model):
    attribute_value = models.CharField(max_length=200)
    def __str__(self):
        return self.attribute_value
class PraductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='atribut')
    key = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='key')
    value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE, related_name='value')