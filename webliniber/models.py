from django.db import models


class Animal(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    organismo = models.TextField(db_column='Organismo', blank=True, null=True)
    instalacion = models.TextField(db_column='Instalacion', blank=True, null=True)
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)
    frecuencia = models.TextField(db_column='Frecuencia', blank=True, null=True)
    telefono = models.TextField(db_column='Telefono', blank=True, null=True)
    activo = models.BooleanField(db_column='Activo')
    fecha_nacimiento = models.DateTimeField(db_column='FechaNacimiento', blank=True, null=True)

    class Meta:
        db_table = 'Animal'


class AreasDistribuccion(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    año = models.SmallIntegerField(db_column='Año', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Areas_Distribuccion'


class Posicion(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    latitud = models.DecimalField(db_column='Latitud', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    longitud = models.DecimalField(db_column='Longitud', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    satelite = models.TextField(db_column='Satelite', blank=True, null=True)  # Field name made lowercase.
    actividad = models.IntegerField(db_column='Actividad', blank=True, null=True)  # Field name made lowercase.
    tipo_gps = models.IntegerField(db_column='Tipo_GPS', blank=True, null=True)  # Field name made lowercase.
    bateria = models.DecimalField(db_column='Bateria', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    bateria_respaldo = models.DecimalField(db_column='Bateria_respaldo', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    temperatura = models.DecimalField(db_column='Temperatura', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='Animal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Posicion'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'
