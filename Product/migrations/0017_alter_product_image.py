# Generated by Django 3.2.6 on 2021-09-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0016_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static/default.jpg', upload_to='images'),
        ),
    ]
