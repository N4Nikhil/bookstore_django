
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]
