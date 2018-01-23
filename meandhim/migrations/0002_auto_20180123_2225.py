# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-23 22:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meandhim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='anwser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=200)),
                ('choice2', models.CharField(max_length=200)),
                ('choice3', models.CharField(max_length=200)),
                ('choice4', models.CharField(blank=True, max_length=200)),
                ('choice5', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=10)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meandhim.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meandhim.user')),
            ],
        ),
        migrations.AddField(
            model_name='anwser',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meandhim.response'),
        ),
        migrations.AddField(
            model_name='anwser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meandhim.user'),
        ),
    ]
