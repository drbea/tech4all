from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    This model represents an article, which consists of a title, content, 
    creation and update timestamps, and a category it belongs to.
    """
    # Model fields
    title = models.CharField(max_length=250, verbose_name="Title")
    # content = models.TextField(verbose_name="Content")
    # content = RichTextField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")

    slug = models.SlugField(max_length=250, unique=True, verbose_name="Slug", editable=False, default=None)

    def save(self, *args, **kwargs):
        """
        Override the save method to generate a slug based on the article title.
        """
        if not self.slug:
            self.slug = self.title.lower().replace(" ", "-")
        super().save(*args, **kwargs)


    # Model methods
    def __str__(self):
        """
        Returns a string representation of the article object.
        """
        return self.title
    
    def get_absolute_url(self):
        """
        Returns the absolute URL of the article object.
        """
        return f"/blog/{self.id}"
    
    class Meta: # Meta class for Article model.
        ordering = ['-created_at']  # Orders the articles by creation date in descending order


class Comment(models.Model):
    """
    This model represents a comment on an article, which consists of a content,
    creation and update timestamps, and an article it belongs to.
    """
    # Model fields
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Article")

    # Model methods
    def __str__(self):
        """
        Returns a string representation of the comment object.
        """
        return self.content[:100]
    
    class Meta: # Meta class for Comment model.
        ordering = ['-created_at']  # Orders the comments by creation date in descending order




