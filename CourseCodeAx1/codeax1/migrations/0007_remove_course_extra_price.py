# Generated by Django 4.2.1 on 2023-09-20 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeax1', '0006_course_extra_price_alter_learning_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='extra_price',
        ),
    ]
