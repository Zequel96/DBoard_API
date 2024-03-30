# Generated by Django 3.2.18 on 2024-01-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('banner', models.ImageField(upload_to='stock/banners')),
            ],
        ),
    ]
