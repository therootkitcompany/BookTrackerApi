# Generated by Django 5.0.9 on 2024-10-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='idGoogle',
            field=models.UUIDField(default=None, editable=False),
            preserve_default=False,
        ),
    ]
