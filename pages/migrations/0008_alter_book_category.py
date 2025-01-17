# Generated by Django 5.1.1 on 2024-09-11 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank='True', choices=[('fiction', 'fiction'), ('nonfiction', 'nonfiction'), ('science', 'science'), ('mystery', 'mystery'), ('fantasy', 'fantasy'), ('children', 'children'), ('biographies', 'biographies')], max_length=50, null='true'),
        ),
    ]
