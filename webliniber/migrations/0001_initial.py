# Generated by Django 3.2 on 2021-04-24 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('organismo', models.TextField(blank=True, db_column='Organismo', null=True)),
                ('instalacion', models.TextField(blank=True, db_column='Instalacion', null=True)),
                ('nombre', models.TextField(blank=True, db_column='Nombre', null=True)),
                ('frecuencia', models.TextField(blank=True, db_column='Frecuencia', null=True)),
                ('telefono', models.TextField(blank=True, db_column='Telefono', null=True)),
                ('activo', models.BooleanField(db_column='Activo')),
            ],
            options={
                'db_table': 'Animal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AreasDistribuccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', models.TextField(blank=True, null=True)),
                ('nombre', models.TextField(blank=True, db_column='Nombre', null=True)),
                ('año', models.SmallIntegerField(blank=True, db_column='Año', null=True)),
            ],
            options={
                'db_table': 'Areas_Distribuccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
                ('fecha', models.DateTimeField(db_column='Fecha')),
                ('latitud', models.DecimalField(db_column='Latitud', decimal_places=65535, max_digits=65535)),
                ('longitud', models.DecimalField(db_column='Longitud', decimal_places=65535, max_digits=65535)),
                ('satelite', models.TextField(blank=True, db_column='Satelite', null=True)),
                ('actividad', models.IntegerField(blank=True, db_column='Actividad', null=True)),
                ('tipo_gps', models.IntegerField(blank=True, db_column='Tipo_GPS', null=True)),
                ('bateria', models.DecimalField(blank=True, db_column='Bateria', decimal_places=65535, max_digits=65535, null=True)),
                ('bateria_respaldo', models.DecimalField(blank=True, db_column='Bateria_respaldo', decimal_places=65535, max_digits=65535, null=True)),
                ('temperatura', models.DecimalField(blank=True, db_column='Temperatura', decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'Posicion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpatialRefSys',
            fields=[
                ('srid', models.IntegerField(primary_key=True, serialize=False)),
                ('auth_name', models.CharField(blank=True, max_length=256, null=True)),
                ('auth_srid', models.IntegerField(blank=True, null=True)),
                ('srtext', models.CharField(blank=True, max_length=2048, null=True)),
                ('proj4text', models.CharField(blank=True, max_length=2048, null=True)),
            ],
            options={
                'db_table': 'spatial_ref_sys',
                'managed': False,
            },
        ),
    ]
