# Generated by Django 5.0.6 on 2024-06-05 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absence', '0004_alter_etudiant_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='photos'),
        ),
    ]
