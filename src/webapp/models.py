from django.db import models
from django.core.validators import validate_image_file_extension
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class News(models.Model):
    title = models.CharField(max_length=256)
    body = RichTextField()
    image = models.ImageField(upload_to='uploads/img/news/%Y/%m',
                              validators=[validate_image_file_extension])
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(825, 480)],
                               format='JPEG',
                               options={'quality': 100})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title[:30]


