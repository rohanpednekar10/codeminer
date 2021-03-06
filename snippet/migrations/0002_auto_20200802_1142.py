# Generated by Django 3.0.8 on 2020-08-02 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='code',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content1',
            field=models.TextField(default='', null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content2',
            field=models.TextField(default='', null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='introduction',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
