# Generated by Django 5.1.6 on 2025-02-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notehub', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
        migrations.AddField(
            model_name='note',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='notehub.category'),
        ),
    ]
