# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone


class TAdministrators(models.Model):
    id = models.BigIntegerField(primary_key=True)
    number = models.CharField(max_length=200, blank=True, null=True)
    pwd = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_administrators'


class TAlbum(models.Model):
    id = models.BigIntegerField(primary_key=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    score = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    announcer = models.CharField(max_length=200, blank=True, null=True)
    num = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_album'


class TArticle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True,default=timezone.now())
    content = models.TextField(blank=True, null=True)
    t_url = models.CharField(max_length=500, blank=True, null=True)
    t_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_article'


class TChapter(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    size = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    t_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_chapter'


class TCount(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    coun = models.CharField(max_length=200, blank=True, null=True)
    t_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_count'


class TLessons(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    grade = models.CharField(max_length=20, blank=True, null=True)
    t_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lessons'


class TPhoto(models.Model):
    id = models.BigIntegerField(primary_key=True)
    url = models.ImageField(upload_to="img")
    describe_1 = models.CharField(max_length=200, blank=True, null=True)
    show_1 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_photo'


class TTeacher(models.Model):
    id = models.BigIntegerField(primary_key=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_teacher'


class TUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    pwd = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to="img")
    autograph = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    spare = models.DateTimeField(blank=True, null=True,default=timezone.now())

    class Meta:
        managed = False
        db_table = 't_user'
