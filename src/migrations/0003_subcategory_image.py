# Generated by Django 4.1.4 on 2022-12-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_subcategory_content_alter_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
