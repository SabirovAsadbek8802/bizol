# Generated by Django 5.0.3 on 2024-04-04 08:42

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 4, 8, 42, 17, 834433, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
