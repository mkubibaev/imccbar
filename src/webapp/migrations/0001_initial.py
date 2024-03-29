# Generated by Django 4.0 on 2022-02-12 19:13

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCenterPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_zh_cn', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'About center',
                'verbose_name_plural': 'About center',
            },
        ),
        migrations.CreateModel(
            name='AboutCenterPreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('body_en', models.TextField(null=True)),
                ('body_ru', models.TextField(null=True)),
                ('body_zh_cn', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'About center preview',
                'verbose_name_plural': 'About center preview',
            },
        ),
        migrations.CreateModel(
            name='ContactsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_zh_cn', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contacts',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='CooperationPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_zh_cn', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cooperation and exchange',
                'verbose_name_plural': 'Cooperation and exchange',
            },
        ),
        migrations.CreateModel(
            name='FAQPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_zh_cn', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
            },
        ),
        migrations.CreateModel(
            name='LinksPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_zh_cn', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Useful links',
                'verbose_name_plural': 'Useful links',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('title_en', models.CharField(max_length=256, null=True)),
                ('title_ru', models.CharField(max_length=256, null=True)),
                ('title_zh_cn', models.CharField(max_length=256, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_zh_cn', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('image', models.ImageField(upload_to='uploads/img/news/%Y/%m', validators=[django.core.validators.validate_image_file_extension])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='OrgStructurePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_zh_cn', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Organization structure',
                'verbose_name_plural': 'Organization structure',
            },
        ),
        migrations.CreateModel(
            name='OrgStructurePreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('body_en', models.TextField(null=True)),
                ('body_ru', models.TextField(null=True)),
                ('body_zh_cn', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Organization structure preview',
                'verbose_name_plural': 'Organization structure preview',
            },
        ),
        migrations.CreateModel(
            name='PhotoAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_zh_cn', models.CharField(max_length=255, null=True)),
                ('poster', models.ImageField(upload_to='uploads/img/gallery/%Y/%m', validators=[django.core.validators.validate_image_file_extension])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Multimedia photo album',
                'verbose_name_plural': 'Multimedia photo albums',
            },
        ),
        migrations.CreateModel(
            name='ServicesPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_zh_cn', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Platform services',
                'verbose_name_plural': 'Platform services',
            },
        ),
        migrations.CreateModel(
            name='VideoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_zh_cn', models.CharField(max_length=255, null=True)),
                ('poster', models.ImageField(upload_to='uploads/video/posters/%Y/%m', validators=[django.core.validators.validate_image_file_extension])),
                ('file', models.FileField(upload_to='uploads/video/%Y/%m', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mkv'])])),
                ('file_en', models.FileField(null=True, upload_to='uploads/video/%Y/%m', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mkv'])])),
                ('file_ru', models.FileField(null=True, upload_to='uploads/video/%Y/%m', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mkv'])])),
                ('file_zh_cn', models.FileField(null=True, upload_to='uploads/video/%Y/%m', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mkv'])])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Multimedia video',
                'verbose_name_plural': 'Multimedia videos',
            },
        ),
        migrations.CreateModel(
            name='PhotoAlbumImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/img/gallery/%Y/%m', validators=[django.core.validators.validate_image_file_extension])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='webapp.photoalbum', verbose_name='Multimedia gallery')),
            ],
            options={
                'verbose_name': 'Multimedia photo',
                'verbose_name_plural': 'Multimedia photos',
            },
        ),
    ]
