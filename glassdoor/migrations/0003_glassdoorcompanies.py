# Generated by Django 3.1.6 on 2021-04-02 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glassdoor', '0002_glassdoorreview_companyurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlassdoorCompanies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=30, null=True)),
                ('companyReviewPageUrl', models.TextField(null=True)),
            ],
        ),
    ]
