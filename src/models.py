from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="sub")
    name = models.CharField(max_length=200)
    content = RichTextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)

    def __str__(self) -> str:
        return self.name