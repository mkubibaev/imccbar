# Generated by Django 4.0 on 2022-01-16 09:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCenterPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField()),
                ('body_en', ckeditor.fields.RichTextField(null=True)),
                ('body_ru', ckeditor.fields.RichTextField(null=True)),
                ('body_zh_cn', ckeditor.fields.RichTextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'About center page',
                'verbose_name_plural': 'About center page',
            },
        ),
    ]