# Generated by Django 2.2.4 on 2019-09-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='agree',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='賛成'),
        ),
        migrations.AlterField(
            model_name='record',
            name='author',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='著者'),
        ),
        migrations.AlterField(
            model_name='record',
            name='difference',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='違い'),
        ),
        migrations.AlterField(
            model_name='record',
            name='example',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='事例'),
        ),
        migrations.AlterField(
            model_name='record',
            name='genre',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='ジャンル'),
        ),
        migrations.AlterField(
            model_name='record',
            name='importance',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='重要な文'),
        ),
        migrations.AlterField(
            model_name='record',
            name='impressions',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='感想'),
        ),
        migrations.AlterField(
            model_name='record',
            name='inspiration',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='感銘'),
        ),
        migrations.AlterField(
            model_name='record',
            name='learn',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='学び'),
        ),
        migrations.AlterField(
            model_name='record',
            name='opposition',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='反対'),
        ),
        migrations.AlterField(
            model_name='record',
            name='story',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='進め方'),
        ),
        migrations.AlterField(
            model_name='record',
            name='summary',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='要約'),
        ),
        migrations.AlterField(
            model_name='record',
            name='unkown',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='不明点'),
        ),
    ]
