# Generated by Django 2.1.7 on 2019-03-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='avatar',
            field=models.ImageField(blank=True, default='../static/img/no_avatar.png', upload_to='media/users_avatars'),
        ),
    ]
