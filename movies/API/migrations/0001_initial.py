# Generated by Django 3.1.3 on 2020-11-09 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('year', models.CharField(max_length=128)),
                ('rated', models.CharField(max_length=128)),
                ('relased', models.CharField(max_length=128)),
                ('runtime', models.CharField(max_length=128)),
                ('genre', models.CharField(max_length=128)),
                ('director', models.CharField(max_length=128)),
                ('writer', models.CharField(max_length=512)),
                ('actors', models.CharField(max_length=512)),
                ('plot', models.CharField(max_length=1024)),
                ('language', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('awards', models.CharField(max_length=512)),
                ('poster', models.CharField(max_length=128)),
                ('metascore', models.CharField(max_length=128)),
                ('imdbrating', models.CharField(max_length=128)),
                ('imdbvotes', models.CharField(max_length=128)),
                ('imdbID', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('dvd', models.CharField(max_length=128)),
                ('boxoffice', models.CharField(max_length=128)),
                ('production', models.CharField(max_length=128)),
                ('website', models.CharField(max_length=128)),
                ('response', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=128)),
                ('value', models.CharField(max_length=128)),
                ('movie', models.ForeignKey(db_column='title', on_delete=django.db.models.deletion.CASCADE, to='API.moviedata')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=128)),
                ('movie', models.ForeignKey(db_column='title', on_delete=django.db.models.deletion.CASCADE, to='API.moviedata')),
            ],
        ),
    ]
