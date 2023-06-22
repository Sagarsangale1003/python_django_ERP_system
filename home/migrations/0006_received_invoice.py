# Generated by Django 3.2.3 on 2021-05-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_invoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Received_Invoice',
            fields=[
                ('InvoiceNo', models.TextField(default='0', primary_key=True, serialize=False)),
                ('Supplier', models.CharField(max_length=300)),
                ('Date', models.DateField()),
                ('Delivery_Note', models.TextField(default='-')),
                ('Mode_Terms_Of_Payment', models.TextField(default='-')),
                ('Supplier_Reference', models.TextField(default='-')),
                ('Other_Reference', models.TextField(default='-')),
                ('OrderNo', models.TextField(default='-')),
                ('Delivery_Note_Date', models.DateField()),
                ('Despatched_Document_No', models.TextField(default='-')),
                ('Despatched_Through', models.TextField(default='-')),
                ('Terms_Of_Delivery', models.TextField(default='-')),
                ('Particulars', models.TextField(default='-', max_length=250)),
                ('HSN_SAC', models.FloatField(default='0')),
                ('Quantity', models.FloatField(default='0')),
                ('Rate', models.FloatField(default='0')),
                ('Amount', models.FloatField(default='0')),
                ('GST_1', models.FloatField(default='0')),
                ('HSN_SAC_Amount', models.FloatField(default='0')),
                ('GST_2', models.FloatField(default='0')),
                ('Total', models.FloatField(default='0')),
                ('PaidBy', models.TextField(default='-')),
            ],
        ),
    ]
