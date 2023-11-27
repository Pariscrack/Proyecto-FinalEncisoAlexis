# Generated by Django 4.2.7 on 2023-11-25 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blob', '0002_blog_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=120)),
                ('comentario', models.CharField(max_length=600)),
                ('fecha', models.DateField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blob.blog')),
            ],
        ),
    ]