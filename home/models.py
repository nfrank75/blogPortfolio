from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Blog(models.Model):
    title = models.CharField(max_length=200)
    meta = models.CharField(max_length=300)
    content = models.TextField()
    blog_img = models.ImageField(null=True, blank=True, upload_to="images/")
    blog_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255, default="uncategorized")
    slug = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    contact_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = PhoneNumberField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.contact_name