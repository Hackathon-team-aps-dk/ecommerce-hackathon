# Generated by Django 3.2.6 on 2021-09-20 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0019_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='productImage',
        ),
    ]