
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0002_auto_20200524_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
