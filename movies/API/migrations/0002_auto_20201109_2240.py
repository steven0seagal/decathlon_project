# Generated by Django 3.1.3 on 2020-11-09 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.moviedata'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.moviedata'),
        ),
    ]
