# Generated by Django 2.2.7 on 2019-12-30 21:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20191229_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]