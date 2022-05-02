from django.db import models
from django.utils.text import slugify



class Creator(models.Model):
    name = models.CharField(max_length=50,default='0')
    image = models.FileField()

    def __str__(self):
        return self.name

class Price_logo(models.Model):
    name = models.CharField(max_length=50,default='0')
    image = models.FileField()

    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50,default='0')
    image = models.FileField()
    cover_image = models.FileField()   
    highest_sale = models.CharField(max_length=50,default='0') 
    floor_price = models.CharField(max_length=50,default='0')
    marketcap = models.CharField(max_length=50,default='0')
    items = models.CharField(max_length=50,default='0')
    owners = models.CharField(max_length=50,default='0')   
    total_volume = models.CharField(max_length=50,default='0')     
    slug = models.SlugField(blank=True)       

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)





class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	subject = models.CharField(max_length=2000)
	message = models.TextField()

	def __str__ (self):
		return self.name

class Nft(models.Model):
    parent = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50,default='0')
    price = models.CharField(max_length=50,default='0')
    image = models.FileField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='nft')
    price_logo = models.ForeignKey(Price_logo,on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Nft, self).save(*args, **kwargs)

class Bid(models.Model):
    name = models.CharField(max_length=50,default='0')
    nft = models.ForeignKey(Nft,on_delete=models.CASCADE)
    price = models.CharField(max_length=50,default='0') 
    qutity = models.CharField(max_length=50,default='0')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Pay_method(models.Model):
    name = models.CharField(max_length=50,default='0')
    wallet = models.CharField(max_length=500,default='0')
    image = models.FileField()
    visible = models.BooleanField(default=True)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Pay_method, self).save(*args, **kwargs)

class Payment(models.Model):
    user = models.CharField(max_length=50,default='0')
    name = models.CharField(max_length=50,default='0')
    price = models.CharField(max_length=50,default='0')
    wallet = models.CharField(max_length=500,default='0')
    image = models.FileField()
    approve = models.BooleanField(default=False)
    def __str__(self):
        return self.name