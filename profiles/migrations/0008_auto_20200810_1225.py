# Generated by Django 3.0.8 on 2020-08-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200806_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_writer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.CharField(choices=[('1.png', 'profile_pic_1'), ('2.png', 'profile_pic_2'), ('3.png', 'profile_pic_3'), ('4.png', 'profile_pic_4'), ('5.png', 'profile_pic_5'), ('6.png', 'profile_pic_6')], default='missingbook.png', max_length=54),
        ),
    ]
