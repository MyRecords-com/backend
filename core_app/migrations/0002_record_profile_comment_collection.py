# Generated by Django 4.0.6 on 2022-07-24 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('rec_format', models.CharField(max_length=50)),
                ('released', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
                ('style', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('location', models.CharField(max_length=100)),
                ('usr_type', models.CharField(max_length=50)),
                ('setup', models.TextField()),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(max_length=20)),
                ('comment', models.TextField()),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.record')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('records', models.ManyToManyField(to='core_app.record')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.profile')),
            ],
        ),
    ]
