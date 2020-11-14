# Generated by Django 3.1.3 on 2020-11-14 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0011_auto_20201114_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geral',
            name='catalogo',
            field=models.CharField(blank=True, default='nulo', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='geral',
            name='cobertura',
            field=models.CharField(blank=True, default='nulo', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='geral',
            name='descricao',
            field=models.CharField(blank=True, default='nulo', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='geral',
            name='entrada',
            field=models.CharField(blank=True, default='nulo', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='geral',
            name='estrutura',
            field=models.CharField(blank=True, default='nulo', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='geral',
            name='formato',
            field=models.CharField(blank=True, default='nulo', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='geral',
            name='idioma',
            field=models.CharField(blank=True, default='nulo', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='geral',
            name='nivel_agregacao',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='geral',
            name='palavras_chaves',
            field=models.CharField(blank=True, default='nulo', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='geral',
            name='tamanho',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='geral',
            name='titulo',
            field=models.CharField(blank=True, default='nulo', max_length=255, null=True),
        ),
    ]
