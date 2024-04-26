# Generated by Django 5.0.4 on 2024-04-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=255)),
                ('course_1', models.CharField(max_length=255)),
                ('course_2', models.CharField(default='course_2', max_length=255)),
                ('course_3', models.CharField(default='course_3', max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('called', models.CharField(choices=[("Bog'lanildi", "Bog'lanildi"), ("Bog'lanilmadi", "Bog'lanilmadi")], default="Bog'lanilmadi", max_length=100)),
            ],
        ),
    ]