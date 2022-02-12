# Generated by Django 4.0 on 2022-02-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_contactspage_faqpage_linkspage'),
    ]

    operations = [
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
    ]