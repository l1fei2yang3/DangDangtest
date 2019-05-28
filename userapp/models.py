# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAddress(models.Model):
    id = models.ForeignKey('TOrder', models.DO_NOTHING, db_column='id', primary_key=True)
    recever = models.CharField(max_length=40, blank=True, null=True)
    receve_address = models.CharField(max_length=40, blank=True, null=True)
    zip_code = models.CharField(max_length=6, blank=True, null=True)
    tel = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_address'


class TBook(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=40, blank=True, null=True)
    dangdang_price = models.FloatField(blank=True, null=True)
    market_price = models.FloatField(blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)
    storage = models.BigIntegerField(blank=True, null=True)
    pushish_time = models.DateField(blank=True, null=True)
    editer_commond = models.IntegerField(blank=True, null=True)
    anthor = models.CharField(max_length=40, blank=True, null=True)
    category = models.ForeignKey('TCategory', models.DO_NOTHING, blank=True, null=True)
    pics = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'


class TCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=40, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_category'


class TOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    order_price = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    receive_address = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'

class Confirm_string(models.Model):
    code=models.CharField(max_length=200,null=True,)
    email=models.CharField(max_length=40,null=True,)
    code_time=models.DateTimeField(null=True,auto_now_add=True)
    user_id=models.ForeignKey("TUser",on_delete=models.CASCADE,null=True)
    class Meta:
        db_table="t_confirm_string"

class TOrderitem(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=40, blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_orderitem'


class TUser(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField( blank=True, null=True,default=0)

    class Meta:
        # managed = False
        db_table = 't_user'
