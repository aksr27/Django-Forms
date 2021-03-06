# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(db_column='emp_id_books', max_length=150)),
                ('title', models.CharField(db_column='Title', max_length=100)),
                ('edition', models.CharField(db_column='Edition', max_length=500)),
                ('published_date', models.DateField(db_column='Published_Date')),
                ('chapter', models.CharField(db_column='Chapter', max_length=500)),
                ('isbn', models.CharField(db_column='ISBN', max_length=500)),
                ('copyright_status', models.CharField(db_column='Copyright_Status', max_length=100)),
                ('copyright_no', models.CharField(db_column='Copyright_No', max_length=100)),
                ('publisher_name', models.CharField(db_column='Publisher_Name', max_length=100)),
                ('publisher_address', models.CharField(db_column='Publisher_Address', max_length=500)),
                ('publisher_zip_code', models.IntegerField(db_column='Publisher_Zip_Code')),
                ('publisher_contact', models.CharField(db_column='Publisher_Contact', max_length=50)),
                ('publisher_email', models.CharField(db_column='Publisher_Email', max_length=50)),
                ('publisher_website', models.CharField(db_column='Publisher_Website', max_length=100)),
                ('author', models.ForeignKey(db_column='Author', default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='author', to='login.AarDropdown')),
                ('publisher_type', models.ForeignKey(db_column='Publisher_Type', default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='publisher_type', to='login.AarDropdown')),
                ('role', models.ForeignKey(db_column='Role', default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='role', to='login.AarDropdown')),
                ('role_for', models.ForeignKey(db_column='Role_For', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='login.AarDropdown')),
            ],
            options={
                'db_table': 'books',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Researchconference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(db_column='emp_id_conference', max_length=150)),
                ('sponsered', models.CharField(db_column='Sponsored', max_length=1000)),
                ('conference_title', models.CharField(db_column='Conference_Title', max_length=500)),
                ('paper_title', models.CharField(db_column='Paper_Title', max_length=100)),
                ('published_date', models.DateField(db_column='Published_Date')),
                ('organized_by', models.CharField(db_column='Organized_By', max_length=500)),
                ('journal_name', models.CharField(db_column='Journal_Name', max_length=500)),
                ('volume_no', models.TextField(db_column='Volume_No')),
                ('issue_no', models.CharField(db_column='Issue_No', max_length=500)),
                ('isbn', models.CharField(db_column='ISBN', max_length=500)),
                ('page_no', models.CharField(db_column='Page_No', max_length=100)),
                ('conference_from', models.DateField(db_column='Conference_From')),
                ('conference_to', models.DateField(db_column='Conference_To')),
                ('other_description', models.CharField(db_column='Other_Description', max_length=500)),
                ('publisher_name', models.CharField(db_column='Publisher_Name', max_length=100)),
                ('publisher_address', models.CharField(db_column='Publisher_Address', max_length=500)),
                ('publisher_zip_code', models.IntegerField(db_column='Publisher_Zip_Code')),
                ('publisher_contact', models.CharField(db_column='Publisher_Contact', max_length=50)),
                ('publisher_email', models.CharField(db_column='Publisher_Email', max_length=50)),
                ('publisher_website', models.CharField(db_column='Publisher_Website', max_length=100)),
                ('others', models.CharField(blank=True, db_column='other_conference', max_length=100, null=True)),
                ('author', models.ForeignKey(db_column='Author', on_delete=django.db.models.deletion.CASCADE, related_name='Author_Conference', to='login.AarDropdown')),
                ('category', models.ForeignKey(db_column='Category', on_delete=django.db.models.deletion.CASCADE, related_name='Category_Research', to='login.AarDropdown')),
                ('sub_category', models.ForeignKey(db_column='Sub_Category', on_delete=django.db.models.deletion.CASCADE, related_name='Sub_Category_Conference', to='login.AarDropdown')),
                ('type_of_conference', models.ForeignKey(db_column='Type_Of_Conference', on_delete=django.db.models.deletion.CASCADE, related_name='Conference_Type', to='login.AarDropdown')),
            ],
            options={
                'db_table': 'researchconference',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Researchguidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(db_column='emp_id_guid', max_length=150)),
                ('no_of_students', models.IntegerField(blank=True, db_column='No_Of_Students', null=True)),
                ('degree_awarded', models.CharField(blank=True, db_column='degree_awarded', max_length=100, null=True)),
                ('project_title', models.CharField(blank=True, db_column='Project_Title', max_length=500, null=True)),
                ('area_of_spec', models.CharField(blank=True, db_column='Area_Of_Spec', max_length=100, null=True)),
                ('course', models.ForeignKey(blank=True, db_column='Course', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Course_Guidence', to='login.AarDropdown')),
                ('degree', models.ForeignKey(blank=True, db_column='Degree', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Degree', to='login.AarDropdown')),
                ('guidence', models.ForeignKey(db_column='Guidence', on_delete=django.db.models.deletion.CASCADE, related_name='Guidence', to='login.AarDropdown')),
                ('status', models.ForeignKey(blank=True, db_column='Status', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Status', to='login.AarDropdown')),
            ],
            options={
                'db_table': 'researchguidence',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Researchjournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(db_column='emp_id_journal', max_length=150)),
                ('published_date', models.DateField(db_column='Published_Date')),
                ('paper_title', models.CharField(db_column='Paper_Title', max_length=100)),
                ('impact_factor', models.FloatField(blank=True, db_column='Impact_Factor', null=True)),
                ('journal_name', models.CharField(db_column='Journal_Name', max_length=500)),
                ('volume_no', models.TextField(db_column='Volume_No')),
                ('issue_no', models.CharField(db_column='Issue_No', max_length=500)),
                ('isbn', models.CharField(db_column='ISBN', max_length=500)),
                ('page_no', models.CharField(db_column='Page_No', max_length=100)),
                ('publisher_name', models.CharField(db_column='Publisher_Name', max_length=100)),
                ('publisher_address', models.CharField(db_column='Publisher_Address', max_length=500)),
                ('publisher_zip_code', models.IntegerField(db_column='Publisher_Zip_Code')),
                ('publisher_contact', models.CharField(db_column='Publisher_Contact', max_length=15)),
                ('publisher_email', models.CharField(db_column='Publisher_Email', max_length=50)),
                ('publisher_website', models.CharField(db_column='Publisher_Website', max_length=100)),
                ('others', models.CharField(blank=True, db_column='other_journal', max_length=100, null=True)),
                ('author', models.ForeignKey(db_column='Author', on_delete=django.db.models.deletion.CASCADE, related_name='Author_Journal', to='login.AarDropdown')),
                ('category', models.ForeignKey(db_column='Category', on_delete=django.db.models.deletion.CASCADE, related_name='Category_Journal', to='login.AarDropdown')),
                ('sub_category', models.ForeignKey(db_column='Sub_Category', on_delete=django.db.models.deletion.CASCADE, related_name='Sub_Category_Journal', to='login.AarDropdown')),
                ('type_of_journal', models.ForeignKey(db_column='Type_Of_Journal', on_delete=django.db.models.deletion.CASCADE, related_name='Type_Of_Journal', to='login.AarDropdown')),
            ],
            options={
                'db_table': 'researchjournal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sponsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spons_id', models.IntegerField(db_column='spons_id')),
                ('sponser_name', models.CharField(db_column='sponsor_name', max_length=100)),
            ],
            options={
                'db_table': 'Sponsers',
                'managed': True,
            },
        ),
    ]
