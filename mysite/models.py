# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

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
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

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


class Forex(models.Model):
    time = models.DateTimeField(primary_key=True)
    p_open = models.FloatField(blank=True, null=True)
    p_high = models.FloatField(blank=True, null=True)
    p_low = models.FloatField(blank=True, null=True)
    p_close = models.FloatField(blank=True, null=True)
    sma_5 = models.FloatField(blank=True, null=True)
    sma_10 = models.FloatField(blank=True, null=True)
    sma_20 = models.FloatField(blank=True, null=True)
    sma_60 = models.FloatField(blank=True, null=True)
    sma_120 = models.FloatField(blank=True, null=True)
    sma_240 = models.FloatField(blank=True, null=True)
    wma_5 = models.FloatField(blank=True, null=True)
    wma_10 = models.FloatField(blank=True, null=True)
    wma_20 = models.FloatField(blank=True, null=True)
    wma_60 = models.FloatField(blank=True, null=True)
    wma_120 = models.FloatField(blank=True, null=True)
    wma_240 = models.FloatField(blank=True, null=True)
    ema_5 = models.FloatField(blank=True, null=True)
    ema_10 = models.FloatField(blank=True, null=True)
    ema_20 = models.FloatField(blank=True, null=True)
    ema_60 = models.FloatField(blank=True, null=True)
    ema_120 = models.FloatField(blank=True, null=True)
    ema_240 = models.FloatField(blank=True, null=True)
    stc_slow_9_3_3 = models.FloatField(blank=True, null=True)
    stc_slow_14_3_3 = models.FloatField(blank=True, null=True)
    stc_slow_18_3_3 = models.FloatField(blank=True, null=True)
    rsi_sma_5 = models.FloatField(blank=True, null=True)
    rsi_sma_9 = models.FloatField(blank=True, null=True)
    rsi_sma_14 = models.FloatField(blank=True, null=True)
    rsi_ema_5 = models.FloatField(blank=True, null=True)
    rsi_ema_9 = models.FloatField(blank=True, null=True)
    rsi_ema_14 = models.FloatField(blank=True, null=True)
    bull_sma = models.FloatField(blank=True, null=True)
    bull_upper = models.FloatField(blank=True, null=True)
    bull_lower = models.FloatField(blank=True, null=True)
    macd_dif = models.FloatField(blank=True, null=True)
    macd = models.FloatField(blank=True, null=True)
    macd_osc = models.FloatField(blank=True, null=True)
    tenkan_sen = models.FloatField(blank=True, null=True)
    kijun_sen = models.FloatField(blank=True, null=True)
    chinkou_span = models.FloatField(blank=True, null=True)
    senkou_spana = models.FloatField(db_column='senkou_spanA', blank=True, null=True)  # Field name made lowercase.
    senkou_spanb = models.FloatField(db_column='senkou_spanB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forex'


class TripsPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'trips_post'
