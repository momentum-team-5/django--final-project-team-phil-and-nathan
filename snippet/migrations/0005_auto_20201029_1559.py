# Generated by Django 3.1.2 on 2020-10-29 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippet', '0004_auto_20201028_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]
