# Generated by Django 4.0.1 on 2022-02-14 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('Whatsappmobile', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('State', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=50, null=True)),
                ('GST_NUM', models.CharField(blank=True, max_length=15, null=True)),
                ('lead_status', models.CharField(choices=[('Client', 'Client'), ('Lead', 'Lead'), ('Free', 'Free')], default='Lead', max_length=10)),
                ('lead_ref', models.CharField(choices=[('Website', 'Website'), ('Social Media', 'Social Media'), ('Marketing', 'Marketing'), ('Other', 'Other')], default='Social Media', max_length=15)),
                ('Demat_account', models.CharField(blank=True, max_length=40, null=True)),
                ('lead_ref_extra', models.CharField(blank=True, max_length=50, null=True)),
                ('Agent_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_name', to='administrator.agent')),
            ],
        ),
        migrations.CreateModel(
            name='Services_taken_request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], default='Pending', max_length=15)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_name_request', to='Agent.customer')),
                ('Service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Service_name_request', to='administrator.services')),
            ],
        ),
        migrations.CreateModel(
            name='Services_taken',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Start_date', models.DateField(blank=True, null=True)),
                ('End_date', models.DateField(blank=True, null=True)),
                ('GST', models.IntegerField(blank=True, null=True)),
                ('days_left', models.DurationField(blank=True, null=True)),
                ('Tot_payement', models.IntegerField(blank=True, null=True)),
                ('payment_reference_number', models.CharField(max_length=125)),
                ('payment_mode', models.CharField(choices=[('Gpay', 'Gpay'), ('Bank Transfer', 'Bank Transfer'), ('Paytm', 'Paytm'), ('Online Transfer', ' Online Transfer'), ('Cash', 'Cash'), ('Other', 'Other')], default='Other', max_length=50)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_name', to='Agent.customer')),
                ('Service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Service_name', to='administrator.services')),
            ],
        ),
    ]
