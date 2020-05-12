# Generated by Django 3.0.5 on 2020-05-12 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upvotes', '0003_auto_20200512_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upvote',
            name='upvoter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
