from django.contrib.gis.db import models


class AreaDistribucion(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    geom = models.GeometryField()
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)
    anio = models.SmallIntegerField(db_column='Anio', blank=True, null=True)
    f2002 = models.IntegerField(db_column='F2002', blank=True, null=True)
    f2003 = models.IntegerField(db_column='F2003', blank=True, null=True)
    f2004 = models.IntegerField(db_column='F2004', blank=True, null=True)
    f2005 = models.IntegerField(db_column='F2005', blank=True, null=True)
    f2006 = models.IntegerField(db_column='F2006', blank=True, null=True)
    f2007 = models.IntegerField(db_column='F2007', blank=True, null=True)
    f2008 = models.IntegerField(db_column='F2008', blank=True, null=True)
    f2009 = models.IntegerField(db_column='F2009', blank=True, null=True)
    f2010 = models.IntegerField(db_column='F2010', blank=True, null=True)
    f2011 = models.IntegerField(db_column='F2011', blank=True, null=True)
    f2012 = models.IntegerField(db_column='F2012', blank=True, null=True)
    f2013 = models.IntegerField(db_column='F2013', blank=True, null=True)
    f2014 = models.IntegerField(db_column='F2014', blank=True, null=True)
    f2015 = models.IntegerField(db_column='F2015', blank=True, null=True)
    f2018 = models.IntegerField(db_column='F2016', blank=True, null=True)
    f2016 = models.IntegerField(db_column='F2017', blank=True, null=True)
    f2017 = models.IntegerField(db_column='F2018', blank=True, null=True)
    shape_area = models.DecimalField(db_column='Shape_Area', blank=True, null=True, max_digits=65535, decimal_places=65535)
    shape_length = models.DecimalField(db_column='Shape_Length', blank=True, null=True, max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'Area_Distribucion'


class Animal(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    organismo = models.TextField(db_column='Organismo', blank=True, null=True)
    instalacion = models.TextField(db_column='Instalacion', blank=True, null=True)
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)
    frecuencia = models.TextField(db_column='Frecuencia', blank=True, null=True)
    telefono = models.TextField(db_column='Telefono', blank=True, null=True)
    activo = models.BooleanField(db_column='Activo')
    fecha_nacimiento = models.DateTimeField(db_column='Fecha_Nacimiento', blank=True, null=True)
    area = models.ForeignKey(AreaDistribucion, models.DO_NOTHING, db_column='Area')

    class Meta:
        db_table = 'Animal'


class Posicion(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    estado = models.TextField(db_column='Estado', blank=True, null=True)
    fecha = models.DateTimeField(db_column='Fecha')
    latitud = models.DecimalField(db_column='Latitud', max_digits=65535, decimal_places=65535)
    longitud = models.DecimalField(db_column='Longitud', max_digits=65535, decimal_places=65535)
    satelite = models.TextField(db_column='Satelite', blank=True, null=True)
    actividad = models.IntegerField(db_column='Actividad', blank=True, null=True)
    tipo_gps = models.IntegerField(db_column='Tipo_GPS', blank=True, null=True)
    bateria = models.DecimalField(db_column='Bateria', max_digits=65535, decimal_places=65535, blank=True, null=True)
    bateria_respaldo = models.DecimalField(db_column='Bateria_respaldo', max_digits=65535, decimal_places=65535, blank=True, null=True)
    temperatura = models.DecimalField(db_column='Temperatura', max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.PointField()
    animal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='Animal')

    class Meta:
        managed = False
        db_table = 'Posicion'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'
