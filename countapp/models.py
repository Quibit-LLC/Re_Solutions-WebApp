from django.db import models
from django.contrib.auth.models import User  # Assuming you are using the built-in User model
from django.core.validators import MinValueValidator, MaxValueValidator

class Resolutions(models.Model):
    STATUS_CHOICES = [
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Abandoned', 'Abandoned'),
    ]

    PRIORITY_HELP_TEXT = "Enter a value between 1 and 10."

    title = models.CharField(max_length=100, help_text="Enter the title of the resolution.")
    description = models.TextField(max_length=1000, help_text="Enter a detailed description of the resolution.")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='In Progress', help_text="Select the status of the resolution. Default is in progress.")
    due_date = models.DateField(null=True, blank=True, help_text="Enter the due date of the resolution.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Automatically set to the creation date and time.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Automatically set to the last update date and time.")
    categories = models.CharField(max_length=100, blank=True, help_text="Enter categories related to the resolution.")
    priority = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1, message="Priority must be at least 1."), MaxValueValidator(10, message="Priority must be at most 10.")],
        help_text=PRIORITY_HELP_TEXT,
    )
    notes = models.TextField(max_length=1000, blank=True, help_text="Enter any additional notes for the resolution.")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Select the user who created the resolution.")

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "Resolutions"

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    phone_number = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_date=models.DateTimeField(auto_now_add=True)
    countdown_date = models.DateField(null=True, blank=True)
    location_description = models.TextField(null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_by=models.ForeignKey(User, related_name="Contacts", on_delete=models.CASCADE, null=True)

    class Meta:  #metadata description for the class name in plural
        ordering = ("email",) #order them by their names
        verbose_name_plural="Contacts"

    def __str__(self): #object name to be displayed
        return self.email
    

class NewsArticle(models.Model):
    title = models.CharField(max_length=100, help_text="Enter the title of the news or article.")
    content = models.TextField(help_text="Enter the content of the news or article.")
    image = models.ImageField(upload_to='news_images/', null=True, blank=True, help_text="Upload an image for the news or article.")
    url_link = models.URLField(max_length=200, blank=True, help_text="Enter the URL link related to the news or article.")
    categories = models.CharField(max_length=100, blank=True, help_text="Enter categories related to the news or article.")
    tags = models.CharField(max_length=100, blank=True, help_text="Enter tags related to the news or article.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Automatically set to the creation date and time.")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Select the user who created the news or article.")

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "News and Articles"

    def __str__(self):
        return self.title
