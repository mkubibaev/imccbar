from django.db import models
from django.core.validators import validate_image_file_extension, FileExtensionValidator
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class News(models.Model):
    title = models.CharField(max_length=256)
    body = RichTextUploadingField()
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
        return self.title[:50]


class AboutCenterPage(models.Model):
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About center'
        verbose_name_plural = 'About center'

    def __str__(self):
        return 'About center'


class AboutCenterPreview(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About center preview'
        verbose_name_plural = 'About center preview'

    def __str__(self):
        return 'About center preview'


class OrgStructurePage(models.Model):
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Organization structure'
        verbose_name_plural = 'Organization structure'

    def __str__(self):
        return 'Organization structure'


class OrgStructurePreview(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Organization structure preview'
        verbose_name_plural = 'Organization structure preview'

    def __str__(self):
        return 'Organization structure preview'


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
        verbose_name = 'Multimedia photo album'
        verbose_name_plural = 'Multimedia photo albums'

    def get_media_type(self):
        return 'photo'

    def __str__(self):
        return self.title[:30]


class PhotoAlbumImage(models.Model):
    image = models.ImageField(upload_to='uploads/img/gallery/%Y/%m',
                              validators=[validate_image_file_extension],
                              verbose_name='Photo')
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(825, 480)],
                               format='JPEG',
                               options={'quality': 100})
    album = models.ForeignKey('webapp.PhotoAlbum', related_name='images', on_delete=models.CASCADE,
                              verbose_name='Photo album')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Multimedia photo'
        verbose_name_plural = 'Multimedia photos'

    def __str__(self):
        return 'Multimedia photo'


class VideoItem(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='uploads/video/posters/%Y/%m',
                               validators=[validate_image_file_extension])
    thumbnail = ImageSpecField(source='poster',
                               processors=[ResizeToFill(825, 480)],
                               format='JPEG',
                               options={'quality': 100})
    file = models.FileField(
        upload_to='uploads/video/%Y/%m',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mkv'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Multimedia video'
        verbose_name_plural = 'Multimedia videos'

    def get_media_type(self):
        return 'video'

    def __str__(self):
        return self.title


class CooperationPage(models.Model):
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cooperation and exchange'
        verbose_name_plural = 'Cooperation and exchange'

    def __str__(self):
        return 'Cooperation and exchange'


class ServicesPage(models.Model):
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Platform services'
        verbose_name_plural = 'Platform services'

    def __str__(self):
        return 'Platform services'


class FAQPage(models.Model):
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    def __str__(self):
        return 'FAQ'


class ContactsPage(models.Model):
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return 'Contacts'


class LinksPage(models.Model):
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Useful links'
        verbose_name_plural = 'Useful links'

    def __str__(self):
        return 'Useful links'
