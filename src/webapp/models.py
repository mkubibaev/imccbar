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


class AboutCenterPage(models.Model):
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About center page'
        verbose_name_plural = 'About center page'

    def __str__(self):
        return 'About center'


class OrgStructurePage(models.Model):
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Organization structure page'
        verbose_name_plural = 'Organization structure page'

    def __str__(self):
        return 'Organization structure'


class PhotoAlbum(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='uploads/img/gallery/%Y/%m',
                               validators=[validate_image_file_extension])
    thumbnail = ImageSpecField(source='poster',
                               processors=[ResizeToFill(825, 480)],
                               format='JPEG',
                               options={'quality': 100})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Multimedia gallery'
        verbose_name_plural = 'Multimedia galleries'

    def __str__(self):
        return self.title[:30]


class PhotoAlbumImage(models.Model):
    image = models.ImageField(upload_to='uploads/img/gallery/%Y/%m',
                              validators=[validate_image_file_extension])
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(825, 480)],
                               format='JPEG',
                               options={'quality': 100})
    album = models.ForeignKey('webapp.PhotoAlbum', related_name='images', on_delete=models.CASCADE,
                              verbose_name='Multimedia gallery')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Multimedia photo'
        verbose_name_plural = 'Multimedia photos'

    def __str__(self):
        return 'Multimedia photo'
