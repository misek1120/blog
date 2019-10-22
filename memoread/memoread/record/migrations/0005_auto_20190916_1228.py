# Generated by Django 2.2.4 on 2019-09-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0004_auto_20190901_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='genre',
            field=models.CharField(blank=True, choices=[('1', '文学・評論'), ('2', '人文・思想'), ('3', '社会・政治・法律'), ('4', 'ノンフィクション'), ('5', '歴史・地理'), ('6', 'ビジネス・経済'), ('7', '投資・金融'), ('8', '科学・テクノロジー'), ('9', '医学・薬学'), ('10', 'コンピュータ・IT'), ('11', 'アート・建築・デザイン'), ('12', '趣味・実用'), ('13', 'スポーツ・アウトドア'), ('14', '暮らし・健康・子育て'), ('15', 'その他')], max_length=30, null=True, verbose_name='ジャンル'),
        ),
    ]
