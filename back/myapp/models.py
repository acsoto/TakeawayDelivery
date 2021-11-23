# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=100, blank=True, null=True)
    food_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'


class FoodEvaluate(models.Model):
    food_evaluate_id = models.AutoField(primary_key=True)
    food_evaluate_text = models.CharField(max_length=100, blank=True, null=True)
    food_evaluate_score = models.IntegerField(blank=True, null=True)
    food = models.ForeignKey(Food, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_evaluate'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_user = models.ForeignKey('User', models.DO_NOTHING)
    delivery_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    order_completed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order'


class OrderFood(models.Model):
    order = models.ForeignKey(Order, models.DO_NOTHING, blank=True, null=True)
    food = models.ForeignKey(Food, models.DO_NOTHING, blank=True, null=True)
    food_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_food'


class Star(models.Model):
    star_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'star'


class StarFood(models.Model):
    star = models.ForeignKey(Star, models.DO_NOTHING, blank=True, null=True)
    food = models.ForeignKey(Food, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'star_food'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=100, blank=True, null=True)
    store_address = models.CharField(max_length=100, blank=True, null=True)
    store_tel = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_nickname = models.CharField(max_length=100, blank=True, null=True)
    user_address = models.CharField(max_length=100)
    user_tel = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'user'


class UserEvaluate(models.Model):
    user_evaluate_id = models.AutoField(primary_key=True)
    user_evaluate_text = models.CharField(max_length=100, blank=True, null=True)
    user_evaluate_score = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_evaluate'
