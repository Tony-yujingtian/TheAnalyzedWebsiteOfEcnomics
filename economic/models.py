# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FaD(models.Model):
    data = models.CharField(max_length=100, blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fa����d'





class GjtjDataJi(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_ji'


class GjtjDataMonth(models.Model):

    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month'


class GjtjDataMonthA01(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a01'


class GjtjDataMonthA02(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a02'


class GjtjDataMonthA022(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a02_2'


class GjtjDataMonthA023(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a02_3'


class GjtjDataMonthA03(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a03'


class GjtjDataMonthA04(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a04'


class GjtjDataMonthA05(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a05'


class GjtjDataMonthA06(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a06'


class GjtjDataMonthA07(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a07'


class GjtjDataMonthA08(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a08'


class GjtjDataMonthA09(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a09'


class GjtjDataMonthA10(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a10'


class GjtjDataMonthA11(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a11'


class GjtjDataMonthA12(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a12'


class GjtjDataMonthA13(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a13'


class GjtjDataMonthA14(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_month_a14'


class GjtjDataYear(models.Model):
    data = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_data_year'


class GjtjNameJi(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    number = models.CharField(max_length=255, blank=True, null=True)
    if_gen = models.CharField(max_length=20, blank=True, null=True)
    pre_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_name_ji'


class GjtjNameMonth(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(primary_key=True, max_length=20)
    if_gen = models.CharField(max_length=20, blank=True, null=True)
    pre_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_name_month'


class GjtjNameYear(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    number = models.CharField(max_length=255, blank=True, null=True)
    if_gen = models.CharField(max_length=20, blank=True, null=True)
    pre_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_name_year'


class KaggleA01(models.Model):
    date = models.CharField(db_column='Date', max_length=100, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=100, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100, blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    flight_field = models.CharField(db_column='Flight #', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    route = models.CharField(db_column='Route', max_length=100, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    registration = models.CharField(db_column='Registration', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cn_in = models.CharField(db_column='cn/In', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aboard = models.CharField(db_column='Aboard', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fatalities = models.CharField(db_column='Fatalities', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ground = models.CharField(db_column='Ground', max_length=100, blank=True, null=True)  # Field name made lowercase.
    summary = models.CharField(db_column='Summary', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kaggle_a01'





class Test(models.Model):
    data = models.CharField(max_length=100, blank=True, null=True)
    month = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    concrete_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'
class GjtjConnameMonth(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(primary_key=True, max_length=20)
    con_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_conname_month'


class GjtjConnameJi(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(primary_key=True, max_length=20)
    con_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_conname_ji'
class GjtjConnameYear(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(primary_key=True, max_length=20)
    con_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gjtj_conname_year'