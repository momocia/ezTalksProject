# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class TActivityFree(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.CharField(max_length=10, blank=True, null=True)
    end_date = models.CharField(max_length=10, blank=True, null=True)
    tariffpkg_id = models.IntegerField(blank=True, null=True)
    ext_tariffpkg_id = models.IntegerField(blank=True, null=True)
    free_time = models.IntegerField(blank=True, null=True)
    free_type = models.IntegerField(blank=True, null=True)
    ext_free_time = models.IntegerField(blank=True, null=True)
    ext_free_type = models.IntegerField(blank=True, null=True)
    free_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_activity_free'


class TAdmin(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    role = models.SmallIntegerField(db_column='ROLE', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    last_login_time = models.DateTimeField(db_column='LAST_LOGIN_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_admin'


class TAdminGroup(models.Model):
    group_name = models.CharField(max_length=30, blank=True, null=True)
    acl = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_admin_group'


class TAdminUser(models.Model):
    admin_user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=64)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_admin_user = models.CharField(max_length=128, blank=True, null=True)
    update_admin_user = models.CharField(max_length=128, blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_admin_user'


class TAffiliate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    client_type = models.CharField(db_column='CLIENT_TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    affiliate = models.CharField(db_column='AFFILIATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    end_date = models.CharField(db_column='END_DATE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_affiliate'


class TAgent(models.Model):
    agent_name = models.CharField(max_length=128)
    timezonecode = models.CharField(db_column='timeZoneCode', max_length=10)  # Field name made lowercase.
    country_area_code = models.CharField(max_length=20)
    contact_name = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    agent_password = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    website = models.CharField(db_column='webSite', max_length=300, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=10)
    create_time = models.DateTimeField()
    create_oper_id = models.IntegerField()
    p_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_agent'


class TAgentProportion(models.Model):
    agent_proportion_id = models.AutoField(primary_key=True)
    agent_id = models.IntegerField(unique=True)
    pull_new_proportion = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    meetings_proportion = models.DecimalField(db_column='meetings__proportion', max_digits=10, decimal_places=5, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    rooms_proportion = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    audio_proportion = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    webinar_proportion = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    file_proportion = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    one_extend_proportion = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    two_extend_proportion = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    three_extend_proportion = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_agent_proportion'


class TApiservice(models.Model):
    apiid = models.AutoField(db_column='ApiID', primary_key=True)  # Field name made lowercase.
    apiname = models.CharField(db_column='ApiName', max_length=64)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID')  # Field name made lowercase.
    types = models.CharField(db_column='Types', max_length=1)  # Field name made lowercase.
    subtype = models.CharField(db_column='Subtype', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    producttype = models.CharField(db_column='ProductType', max_length=1)  # Field name made lowercase.
    servicestypeid = models.IntegerField(db_column='ServicesTypeID', blank=True, null=True)  # Field name made lowercase.
    tariffmoduleid = models.IntegerField(db_column='TariffModuleID', blank=True, null=True)  # Field name made lowercase.
    tariffname = models.CharField(db_column='TariffName', max_length=64)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    totalprice = models.FloatField(db_column='TotalPrice')  # Field name made lowercase.
    point = models.IntegerField(db_column='Point', blank=True, null=True)  # Field name made lowercase.
    bar = models.IntegerField(db_column='Bar', blank=True, null=True)  # Field name made lowercase.
    basiclength = models.FloatField(db_column='BasicLength', blank=True, null=True)  # Field name made lowercase.
    timelength = models.FloatField(db_column='TimeLength', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    surplustimelength = models.FloatField(db_column='SurplusTimeLength', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    bbusinessid = models.IntegerField(db_column='BBusinessID', blank=True, null=True)  # Field name made lowercase.
    bstatus = models.CharField(db_column='BStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    extservice_id = models.IntegerField(blank=True, null=True)
    tariffpkg_id = models.IntegerField(blank=True, null=True)
    ext_tariffpkg_id = models.IntegerField(blank=True, null=True)
    host = models.IntegerField(blank=True, null=True)
    orderid = models.CharField(db_column='OrderID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    webinar_order_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_apiservice'


class TApiserviceCopy(models.Model):
    apiid = models.AutoField(db_column='ApiID', primary_key=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    apiname = models.CharField(db_column='ApiName', max_length=64)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID')  # Field name made lowercase.
    types = models.CharField(db_column='Types', max_length=1)  # Field name made lowercase.
    subtype = models.CharField(db_column='Subtype', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    producttype = models.CharField(db_column='ProductType', max_length=1)  # Field name made lowercase.
    servicestypeid = models.IntegerField(db_column='ServicesTypeID', blank=True, null=True)  # Field name made lowercase.
    tariffmoduleid = models.IntegerField(db_column='TariffModuleID', blank=True, null=True)  # Field name made lowercase.
    tariffname = models.CharField(db_column='TariffName', max_length=64)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    totalprice = models.FloatField(db_column='TotalPrice')  # Field name made lowercase.
    point = models.IntegerField(db_column='Point', blank=True, null=True)  # Field name made lowercase.
    bar = models.IntegerField(db_column='Bar', blank=True, null=True)  # Field name made lowercase.
    basiclength = models.FloatField(db_column='BasicLength', blank=True, null=True)  # Field name made lowercase.
    timelength = models.FloatField(db_column='TimeLength', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    surplustimelength = models.FloatField(db_column='SurplusTimeLength', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    bbusinessid = models.IntegerField(db_column='BBusinessID', blank=True, null=True)  # Field name made lowercase.
    bstatus = models.CharField(db_column='BStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    extservice_id = models.IntegerField(blank=True, null=True)
    tariffpkg_id = models.IntegerField(blank=True, null=True)
    ext_tariffpkg_id = models.IntegerField(blank=True, null=True)
    host = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_apiservice_copy'


class TApiserviceCopy1(models.Model):
    apiid = models.AutoField(db_column='ApiID', primary_key=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    apiname = models.CharField(db_column='ApiName', max_length=64)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID')  # Field name made lowercase.
    types = models.CharField(db_column='Types', max_length=1)  # Field name made lowercase.
    subtype = models.CharField(db_column='Subtype', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    producttype = models.CharField(db_column='ProductType', max_length=1)  # Field name made lowercase.
    servicestypeid = models.IntegerField(db_column='ServicesTypeID', blank=True, null=True)  # Field name made lowercase.
    tariffmoduleid = models.IntegerField(db_column='TariffModuleID', blank=True, null=True)  # Field name made lowercase.
    tariffname = models.CharField(db_column='TariffName', max_length=64)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    totalprice = models.FloatField(db_column='TotalPrice')  # Field name made lowercase.
    point = models.IntegerField(db_column='Point', blank=True, null=True)  # Field name made lowercase.
    bar = models.IntegerField(db_column='Bar', blank=True, null=True)  # Field name made lowercase.
    basiclength = models.FloatField(db_column='BasicLength', blank=True, null=True)  # Field name made lowercase.
    timelength = models.FloatField(db_column='TimeLength', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    surplustimelength = models.FloatField(db_column='SurplusTimeLength', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    bbusinessid = models.IntegerField(db_column='BBusinessID', blank=True, null=True)  # Field name made lowercase.
    bstatus = models.CharField(db_column='BStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    extservice_id = models.IntegerField(blank=True, null=True)
    tariffpkg_id = models.IntegerField(blank=True, null=True)
    ext_tariffpkg_id = models.IntegerField(blank=True, null=True)
    host = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_apiservice_copy1'


class TAppeditinfo(models.Model):
    appeditid = models.AutoField(db_column='AppEditID', primary_key=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    apiid = models.IntegerField(db_column='ApiID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    apiname = models.CharField(db_column='ApiName', max_length=64)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID')  # Field name made lowercase.
    accsort = models.CharField(max_length=1)
    types = models.CharField(db_column='Types', max_length=1)  # Field name made lowercase.
    subtype = models.CharField(db_column='Subtype', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    servicestypeid = models.IntegerField(db_column='ServicesTypeID', blank=True, null=True)  # Field name made lowercase.
    tariffmoduleid = models.IntegerField(db_column='TariffModuleID')  # Field name made lowercase.
    tariffname = models.CharField(db_column='TariffName', max_length=64)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    totalprice = models.FloatField(db_column='TotalPrice')  # Field name made lowercase.
    point = models.IntegerField(db_column='Point', blank=True, null=True)  # Field name made lowercase.
    bar = models.IntegerField(db_column='Bar', blank=True, null=True)  # Field name made lowercase.
    basiclength = models.FloatField(db_column='BasicLength', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    surplustimelength = models.FloatField(db_column='SurplusTimeLength', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_appeditinfo'


class TApplypricelog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID')  # Field name made lowercase.
    orderno = models.IntegerField(db_column='OrderNO')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID')  # Field name made lowercase.
    processstate = models.CharField(db_column='processState', max_length=1, blank=True, null=True)  # Field name made lowercase.
    payprice = models.FloatField(db_column='payPrice', blank=True, null=True)  # Field name made lowercase.
    totalmoney = models.FloatField(db_column='TotalMoney')  # Field name made lowercase.
    disprice = models.FloatField(db_column='disPrice', blank=True, null=True)  # Field name made lowercase.
    gooddistotal = models.FloatField(db_column='GoodDisTotal', blank=True, null=True)  # Field name made lowercase.
    goodpayprice = models.FloatField(db_column='GoodPayPrice', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    upoperatorid = models.IntegerField(db_column='UpOperatorID', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_applypricelog'


class TArticle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cateid = models.IntegerField(db_column='CATEID', blank=True, null=True)  # Field name made lowercase.
    editor = models.IntegerField(db_column='EDITOR', blank=True, null=True)  # Field name made lowercase.
    is_top = models.IntegerField(db_column='IS_TOP', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    seo_title = models.CharField(db_column='SEO_TITLE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    is_recommen_howto = models.IntegerField(db_column='IS_RECOMMEN_HOWTO', blank=True, null=True)  # Field name made lowercase.
    publish_method = models.IntegerField(db_column='PUBLISH_METHOD', blank=True, null=True)  # Field name made lowercase.
    publish_date = models.CharField(db_column='PUBLISH_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    set_publish_date = models.CharField(db_column='SET_PUBLISH_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_time = models.CharField(db_column='CREATE_TIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    update_time = models.CharField(db_column='UPDATE_TIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_deleted = models.IntegerField(db_column='IS_DELETED', blank=True, null=True)  # Field name made lowercase.
    view_count = models.IntegerField(db_column='VIEW_COUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_article'


class TAudioAuth(models.Model):
    primary_user_id = models.BigIntegerField(primary_key=True)
    child_user_id = models.BigIntegerField()
    subscription_id = models.BigIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_audio_auth'
        unique_together = (('primary_user_id', 'child_user_id', 'subscription_id'),)


class TBulletin(models.Model):
    bulletinid = models.AutoField(db_column='BulletinID', primary_key=True)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    content = models.TextField(db_column='Content')  # Field name made lowercase.
    isshow = models.CharField(db_column='Isshow', max_length=1)  # Field name made lowercase.
    picurl = models.CharField(db_column='Picurl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    types = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bulletin'


class TBusinessinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    depid = models.IntegerField(db_column='DepID')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    discbalance = models.FloatField(db_column='DiscBalance', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    timelength = models.IntegerField(db_column='TimeLength', blank=True, null=True)  # Field name made lowercase.
    bar = models.IntegerField(db_column='Bar', blank=True, null=True)  # Field name made lowercase.
    logo = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(db_column='Content', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=64)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=64, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=128)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=128, blank=True, null=True)  # Field name made lowercase.
    surplustimelength = models.FloatField(db_column='SurplusTimeLength', blank=True, null=True)  # Field name made lowercase.
    qq = models.CharField(max_length=25, blank=True, null=True)
    domainkey = models.CharField(db_column='DomainKey', max_length=50)  # Field name made lowercase.
    siteurl = models.CharField(max_length=100, blank=True, null=True)
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=1, blank=True, null=True)
    devid = models.CharField(db_column='DevID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    isshowsysbull = models.CharField(db_column='isShowSysBull', max_length=1, blank=True, null=True)  # Field name made lowercase.
    testnumber = models.IntegerField(db_column='TestNumber', blank=True, null=True)  # Field name made lowercase.
    companysize = models.CharField(db_column='CompanySize', max_length=25, blank=True, null=True)  # Field name made lowercase.
    indcode = models.IntegerField(db_column='indCode', blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_businessinfo'


class TBusinessinfoGroup(models.Model):
    group_name = models.CharField(unique=True, max_length=128)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_businessinfo_group'


class TCategory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    cate_title = models.CharField(db_column='CATE_TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cate_description = models.TextField(db_column='CATE_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='PATH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(db_column='LEVEL', blank=True, null=True)  # Field name made lowercase.
    is_delete = models.IntegerField(db_column='IS_DELETE', blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    update_date = models.CharField(db_column='UPDATE_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_category'


class TChangereq(models.Model):
    reqid = models.AutoField(db_column='ReqID', primary_key=True)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    operatorid1 = models.IntegerField(db_column='OperatorID1', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    changename = models.CharField(db_column='ChangeName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    apiserviceid = models.IntegerField(db_column='ApiServiceID', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    point = models.FloatField(db_column='Point', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    oldprice = models.FloatField(db_column='OldPrice')  # Field name made lowercase.
    oldpoint = models.FloatField(db_column='OldPoint', blank=True, null=True)  # Field name made lowercase.
    oldstarttime = models.DateTimeField(db_column='OldStartTime', blank=True, null=True)  # Field name made lowercase.
    oldendtime = models.DateTimeField(db_column='OldEndTime', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    agreedate = models.DateTimeField(db_column='AgreeDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_changereq'


class TClientVersion(models.Model):
    client_type = models.CharField(max_length=10)
    version_name = models.CharField(max_length=64)
    version_num = models.CharField(max_length=64)
    version_build_num = models.IntegerField(blank=True, null=True)
    version_size = models.FloatField()
    upgrade = models.CharField(max_length=10)
    adress = models.CharField(max_length=256)
    explains = models.TextField()
    version_code = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=10)
    create_time = models.DateTimeField()
    create_oper_id = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)
    update_oper_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_client_version'


class TContact(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    message_to = models.IntegerField(db_column='MESSAGE_TO', blank=True, null=True)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    country = models.IntegerField(db_column='COUNTRY', blank=True, null=True)  # Field name made lowercase.
    request_type = models.IntegerField(db_column='REQUEST_TYPE', blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='EMAIL_ADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    question = models.CharField(db_column='QUESTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    anwser = models.TextField(db_column='ANWSER', blank=True, null=True)  # Field name made lowercase.
    message = models.TextField(db_column='MESSAGE', blank=True, null=True)  # Field name made lowercase.
    create_time = models.CharField(db_column='CREATE_TIME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_contact'


class TCountry(models.Model):
    name = models.CharField(max_length=60)
    zh_name = models.CharField(max_length=60, blank=True, null=True)
    area_code = models.CharField(max_length=20, blank=True, null=True)
    code1 = models.CharField(max_length=10, blank=True, null=True)
    code2 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_country'


class TCountryBak(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 't_country_bak'


class TCoupon(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    coupon_name = models.CharField(db_column='COUPON_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coupon_code = models.CharField(db_column='COUPON_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='DISCOUNT', blank=True, null=True)  # Field name made lowercase.
    product_ids = models.CharField(db_column='PRODUCT_IDS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    begin_time = models.CharField(db_column='BEGIN_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    end_time = models.CharField(db_column='END_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    update_time = models.CharField(db_column='UPDATE_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    create_time = models.CharField(db_column='CREATE_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    discount_munber = models.IntegerField(db_column='DISCOUNT_MUNBER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_coupon'


class TCurrency(models.Model):
    card_type = models.IntegerField(primary_key=True)
    currency_code = models.CharField(max_length=10)
    order_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_currency'
        unique_together = (('card_type', 'currency_code'),)


class TDatelist(models.Model):
    datestr = models.DateField(db_column='dateStr', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_datelist'


class TDbSession(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    expire = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_db_session'


class TDepartment(models.Model):
    depid = models.AutoField(db_column='DepID', primary_key=True)  # Field name made lowercase.
    parentdepid = models.IntegerField(db_column='ParentDepID', blank=True, null=True)  # Field name made lowercase.
    depname = models.CharField(db_column='DepName', max_length=64)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    devid = models.CharField(db_column='DevID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    muserid = models.IntegerField(db_column='Muserid', blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_department'


class TDesc(models.Model):
    id = models.IntegerField(db_column='ID', blank=True,primary_key=True)  # Field name made lowercase.
    desc = models.CharField(db_column='DESC', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_desc'


class TDevice(models.Model):
    device_id = models.BigAutoField(primary_key=True)
    device_name = models.CharField(max_length=100)
    attr1 = models.CharField(max_length=100, blank=True, null=True)
    attr2 = models.CharField(max_length=100, blank=True, null=True)
    attr3 = models.CharField(max_length=100, blank=True, null=True)
    attr4 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_device'


class TDevinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    devid = models.CharField(db_column='devID', max_length=64)  # Field name made lowercase.
    parentdevid = models.IntegerField(db_column='ParentDevID', blank=True, null=True)  # Field name made lowercase.
    devcode = models.CharField(db_column='DevCode', max_length=64)  # Field name made lowercase.
    devname = models.CharField(db_column='DevName', max_length=64)  # Field name made lowercase.
    devtype = models.CharField(db_column='DevType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    devip = models.CharField(db_column='DevIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    devstatus = models.CharField(db_column='DevStatus', max_length=1)  # Field name made lowercase.
    online = models.CharField(db_column='Online', max_length=1, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    verifycode = models.CharField(db_column='VerifyCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    allocpriority = models.IntegerField(db_column='AllocPriority', blank=True, null=True)  # Field name made lowercase.
    backdevid = models.CharField(db_column='BackDevID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    maxonline = models.IntegerField(db_column='MaxOnline', blank=True, null=True)  # Field name made lowercase.
    curonline = models.IntegerField(db_column='CurOnline', blank=True, null=True)  # Field name made lowercase.
    roommaxusercount = models.IntegerField(db_column='RoomMaxUserCount', blank=True, null=True)  # Field name made lowercase.
    maxbandwidth = models.IntegerField(db_column='MaxBandwidth', blank=True, null=True)  # Field name made lowercase.
    curbandwidth = models.IntegerField(db_column='CurBandwidth', blank=True, null=True)  # Field name made lowercase.
    curroomcount = models.IntegerField(db_column='CurRoomCount', blank=True, null=True)  # Field name made lowercase.
    cpuload = models.IntegerField(db_column='CPULoad', blank=True, null=True)  # Field name made lowercase.
    suportmobile = models.CharField(db_column='SuportMobile', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_devinfo'


class TDiscount(models.Model):
    discount_id = models.AutoField(primary_key=True)
    discount_code = models.CharField(unique=True, max_length=64)
    discount_name = models.CharField(max_length=100)
    discount_type = models.IntegerField(blank=True, null=True)
    discount_scale = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    support_cycle = models.IntegerField(blank=True, null=True)
    user_use_count_limit = models.IntegerField(blank=True, null=True)
    total_count_limit = models.IntegerField(blank=True, null=True)
    order_amout_limit = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_admin_user = models.CharField(max_length=128, blank=True, null=True)
    update_admin_user = models.CharField(max_length=128, blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)
    use_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_discount'


class TDiscountService(models.Model):
    discount_id = models.IntegerField(primary_key=True)
    service_id = models.IntegerField()
    service_category_id = models.IntegerField()
    discount_code = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 't_discount_service'
        unique_together = (('discount_id', 'service_id'),)


class TElemtomodule(models.Model):
    tariffelemid = models.IntegerField(db_column='TariffelemID', primary_key=True)  # Field name made lowercase.
    tariffmoduleid = models.IntegerField(db_column='TariffModuleID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_elemtomodule'
        unique_together = (('tariffelemid', 'tariffmoduleid'),)


class TEmailLog(models.Model):
    from_user_id = models.IntegerField()
    to_user_id = models.IntegerField()
    email_type = models.IntegerField()
    email_subject = models.CharField(max_length=1000, blank=True, null=True)
    email_content = models.TextField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_email_log'


class TEmailLogEvent(models.Model):
    email_log_id = models.IntegerField()
    event_name = models.CharField(max_length=32)
    create_time = models.DateTimeField()
    city_name = models.CharField(max_length=60, blank=True, null=True)
    country_code = models.CharField(max_length=20, blank=True, null=True)
    click_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_email_log_event'


class TEmailProject(models.Model):
    pro_id = models.CharField(max_length=50)
    pro_name = models.CharField(max_length=50)
    pro_subject = models.CharField(max_length=100, blank=True, null=True)
    pro_desc = models.CharField(max_length=100, blank=True, null=True)
    database_id = models.IntegerField(blank=True, null=True)
    temp_id = models.IntegerField(blank=True, null=True)
    domain = models.CharField(max_length=50, blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_email_project'


class TEmailProjectUser(models.Model):
    user_id = models.IntegerField()
    pro_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_email_project_user'


class TEmailProjectUserEvent(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    pro_id = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    event_name = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    city_name = models.CharField(max_length=60, blank=True, null=True)
    country_code = models.CharField(max_length=20, blank=True, null=True)
    click_url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_email_project_user_event'


class TEmailTemp(models.Model):
    temp_name = models.CharField(max_length=50)
    temp_desc = models.CharField(max_length=100, blank=True, null=True)
    temp_content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_email_temp'


class TEmailUser(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    register_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    check_status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 't_email_user'


class TEmailUserType(models.Model):
    id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=50)
    type_desc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_email_user_type'


class TEmotion(models.Model):
    groupname = models.CharField(max_length=64, blank=True, null=True)
    sort = models.CharField(max_length=64, blank=True, null=True)
    qrc_path = models.CharField(max_length=256, blank=True, null=True)
    tooltip = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_emotion'


class TErpapproval(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    depid = models.IntegerField(db_column='DepID')  # Field name made lowercase.
    buylicensecount = models.IntegerField(db_column='BuyLicenseCount', blank=True, null=True)  # Field name made lowercase.
    tariffproitemid = models.IntegerField(db_column='TariffProItemID', blank=True, null=True)  # Field name made lowercase.
    contractstarttime = models.DateTimeField(db_column='ContractStartTime')  # Field name made lowercase.
    contractendtime = models.DateTimeField(db_column='ContractEndTime')  # Field name made lowercase.
    money = models.FloatField(db_column='Money', blank=True, null=True)  # Field name made lowercase.
    paystarttime = models.DateTimeField(db_column='PayStartTime', blank=True, null=True)  # Field name made lowercase.
    payendtime = models.DateTimeField(db_column='PayEndTime', blank=True, null=True)  # Field name made lowercase.
    approvaltype = models.CharField(db_column='ApprovalType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    approvalstate = models.CharField(db_column='ApprovalState', max_length=1, blank=True, null=True)  # Field name made lowercase.
    requserid = models.IntegerField(db_column='ReqUserID', blank=True, null=True)  # Field name made lowercase.
    reqtime = models.DateTimeField(db_column='ReqTime', blank=True, null=True)  # Field name made lowercase.
    financeuserid = models.IntegerField(db_column='FinanceUserID', blank=True, null=True)  # Field name made lowercase.
    financetime = models.DateTimeField(db_column='FinanceTime', blank=True, null=True)  # Field name made lowercase.
    operationuserid = models.IntegerField(db_column='OperationUserID', blank=True, null=True)  # Field name made lowercase.
    operationtime = models.DateTimeField(db_column='OperationTime', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=512, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_erpapproval'


class TFaqs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    classification = models.CharField(db_column='CLASSIFICATION', max_length=50)  # Field name made lowercase.
    questions = models.CharField(db_column='QUESTIONS', max_length=200)  # Field name made lowercase.
    answer = models.TextField(db_column='ANSWER')  # Field name made lowercase.
    fqtime = models.CharField(db_column='FQTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='SORT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_faqs'


class TFeedback(models.Model):
    type = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    product_id = models.CharField(max_length=16, blank=True, null=True)
    client_version = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    device_type = models.CharField(max_length=50, blank=True, null=True)
    os_version = models.CharField(max_length=50, blank=True, null=True)
    timezone_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_feedback'


class TFeedbackMoment(models.Model):
    moment_id = models.AutoField(primary_key=True)
    moment_type = models.IntegerField()
    moment_number = models.IntegerField()
    moment_content = models.CharField(max_length=500)
    create_time = models.DateTimeField(blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_feedback_moment'


class TFinancelog(models.Model):
    financelogid = models.AutoField(db_column='FinanceLogID', primary_key=True)  # Field name made lowercase.
    stuts = models.CharField(db_column='Stuts', max_length=1)  # Field name made lowercase.
    tradetype = models.CharField(db_column='TradeType', max_length=1)  # Field name made lowercase.
    trademoney = models.FloatField(db_column='TradeMoney')  # Field name made lowercase.
    glidenumber = models.IntegerField(db_column='GlideNumber')  # Field name made lowercase.
    paymode = models.CharField(db_column='PayMode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    roomid = models.IntegerField(db_column='RoomID', blank=True, null=True)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='Createdate', blank=True, null=True)  # Field name made lowercase.
    billingdate = models.DateTimeField(db_column='BillingDate', blank=True, null=True)  # Field name made lowercase.
    ifline = models.CharField(db_column='ifLine', max_length=1)  # Field name made lowercase.
    cardno = models.CharField(db_column='cardNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    accttype = models.CharField(db_column='AcctType', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_financelog'
        unique_together = (('financelogid', 'glidenumber'),)


class TForgotpwd(models.Model):
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    active = models.CharField(max_length=100)
    username = models.CharField(db_column='UserName', max_length=30)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_forgotpwd'


class THardware(models.Model):
    hardware_id = models.IntegerField()
    hardware_type = models.IntegerField()
    token = models.CharField(max_length=32, blank=True, null=True)
    hardware_name = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=10)
    username = models.CharField(db_column='userName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    explains = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()
    create_oper_id = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)
    update_oper_id = models.IntegerField(blank=True, null=True)
    system_id = models.IntegerField(unique=True, blank=True, null=True)
    device_id = models.CharField(unique=True, max_length=64, blank=True, null=True)
    is_user_binding = models.IntegerField(blank=True, null=True)
    admin_binding_time = models.DateTimeField(blank=True, null=True)
    admin_user_id = models.IntegerField(blank=True, null=True)
    authorization_code = models.CharField(max_length=10, blank=True, null=True)
    room_plan = models.IntegerField(blank=True, null=True)
    free_meeting_time = models.IntegerField(blank=True, null=True)
    used_free_meeting_time = models.IntegerField(blank=True, null=True)
    bind_room_plan_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_hardware'


class THardwareAuth(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    hardware_id = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_hardware_auth'
        unique_together = (('user_id', 'hardware_id'),)


class THolidays(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    setdate = models.DateTimeField(db_column='SetDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_holidays'


class THostAuth(models.Model):
    primary_user_id = models.BigIntegerField(primary_key=True)
    child_user_id = models.BigIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_host_auth'
        unique_together = (('primary_user_id', 'child_user_id'),)


class TImGroup(models.Model):
    group_name = models.TextField()
    group_type = models.IntegerField()
    creator_id = models.IntegerField()
    members = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_group'


class TImGroupmember(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    group_id = models.IntegerField(primary_key=True)
    member_id = models.IntegerField()
    group_type = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_groupmember'
        unique_together = (('group_id', 'member_id'),)


class TImGroupmessage0(models.Model):
    from_id = models.IntegerField()
    to_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    meeting_id = models.IntegerField(blank=True, null=True)
    msg_id = models.BigIntegerField()
    msg_type = models.IntegerField()
    content = models.TextField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_groupmessage0'


class TImGroupnotify0(models.Model):
    from_id = models.IntegerField(blank=True, null=True)
    to_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    meeting_id = models.IntegerField(blank=True, null=True)
    msg_id = models.BigIntegerField()
    msg_type = models.IntegerField()
    content = models.TextField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_groupnotify0'


class TImGroupnotifyshield(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(primary_key=True)
    msg_index = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_groupnotifyshield'
        unique_together = (('user_id', 'msg_index'),)


class TImMeeting(models.Model):
    meeting_id = models.IntegerField(blank=True, null=True)
    meeting_type = models.IntegerField()
    creator_id = models.IntegerField()
    members = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_meeting'


class TImMeetingmember(models.Model):
    id = models.AutoField(primary_key=True)
    meeting_id = models.IntegerField(primary_key=True)
    meeting_index = models.IntegerField()
    member_id = models.IntegerField()
    meeting_type = models.IntegerField()
    role = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_meetingmember'
        unique_together = (('meeting_id', 'meeting_index', 'member_id'),)


class TImMeetingmessage0(models.Model):
    from_id = models.IntegerField(blank=True, null=True)
    to_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    meeting_id = models.IntegerField(blank=True, null=True)
    msg_id = models.BigIntegerField()
    msg_type = models.IntegerField()
    content = models.TextField()
    meeting_index = models.IntegerField(blank=True, null=True)
    state = models.IntegerField()
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_meetingmessage0'


class TImMeetingnotify0(models.Model):
    from_id = models.IntegerField(blank=True, null=True)
    to_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    meeting_id = models.IntegerField(blank=True, null=True)
    msg_id = models.BigIntegerField()
    msg_type = models.IntegerField()
    content = models.TextField()
    meeting_index = models.IntegerField(blank=True, null=True)
    state = models.IntegerField()
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_meetingnotify0'


class TImMeetingnotifyshield(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(primary_key=True)
    msg_index = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_meetingnotifyshield'
        unique_together = (('user_id', 'msg_index'),)


class TImMessage0(models.Model):
    from_id = models.IntegerField(blank=True, null=True)
    to_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    meeting_id = models.IntegerField(blank=True, null=True)
    msg_id = models.BigIntegerField()
    msg_type = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_message0'


class TImNotify0(models.Model):
    from_id = models.IntegerField(blank=True, null=True)
    to_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    meeting_id = models.IntegerField(blank=True, null=True)
    msg_id = models.BigIntegerField()
    msg_type = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_notify0'


class TImNotifyshield(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(primary_key=True)
    msg_index = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_notifyshield'
        unique_together = (('user_id', 'msg_index'),)


class TImRelation(models.Model):
    id = models.AutoField(primary_key=True)
    from_id = models.IntegerField(primary_key=True)
    to_id = models.IntegerField()
    remark_name = models.CharField(max_length=64, blank=True, null=True)
    mobilephone = models.CharField(max_length=32, blank=True, null=True)
    workphone = models.CharField(max_length=32, blank=True, null=True)
    homephone = models.CharField(max_length=32, blank=True, null=True)
    mainphone = models.CharField(max_length=32, blank=True, null=True)
    company = models.CharField(max_length=256, blank=True, null=True)
    duties = models.CharField(max_length=128, blank=True, null=True)
    birthday = models.CharField(max_length=64, blank=True, null=True)
    state = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    lup_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_im_relation'
        unique_together = (('from_id', 'to_id'),)


class TImRelationgroup(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.TextField(blank=True, null=True)
    group_type = models.IntegerField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    members = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_relationgroup'


class TImRelationgroupmember(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.IntegerField(primary_key=True)
    member_id = models.IntegerField()
    group_type = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    lup_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_im_relationgroupmember'
        unique_together = (('group_id', 'member_id'),)


class TIndustry(models.Model):
    ind_code = models.IntegerField(blank=True, null=True)
    ind_groups = models.CharField(max_length=50, blank=True, null=True)
    descriptions = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_industry'


class TIp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    client_type = models.CharField(db_column='CLIENT_TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cid = models.CharField(db_column='CID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tid = models.CharField(db_column='TID', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ip'


class TIspBrand(models.Model):
    isp_brand_id = models.AutoField(primary_key=True)
    isp_brand_name = models.CharField(max_length=60, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_isp_brand'


class TIspPhone(models.Model):
    isp_phone_id = models.AutoField(primary_key=True)
    isp_phone_num = models.CharField(max_length=64)
    country_code = models.CharField(max_length=20)
    country_name = models.CharField(max_length=60)
    isp_brand_id = models.IntegerField(blank=True, null=True)
    isp_brand_name = models.CharField(max_length=60, blank=True, null=True)
    isp_phone_type_id = models.IntegerField(blank=True, null=True)
    isp_phone_type_name = models.CharField(max_length=60, blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_isp_phone'


class TIspPhoneLog(models.Model):
    isp_phone_log_id = models.BigAutoField(primary_key=True)
    room_id = models.BigIntegerField(blank=True, null=True)
    meeting_id = models.IntegerField(blank=True, null=True)
    calling_phone_num = models.CharField(max_length=64, blank=True, null=True)
    called_phone_num = models.CharField(max_length=64, blank=True, null=True)
    calling_line_time = models.DateTimeField(blank=True, null=True)
    callout_line_time = models.DateTimeField(blank=True, null=True)
    calling_room_time = models.DateTimeField(blank=True, null=True)
    callout_room_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    host_user_id = models.BigIntegerField(blank=True, null=True)
    host_email = models.CharField(max_length=128, blank=True, null=True)
    parent_user_id = models.BigIntegerField(blank=True, null=True)
    parent_email = models.CharField(max_length=128, blank=True, null=True)
    isp_phone_type_name = models.CharField(max_length=60, blank=True, null=True)
    isp_phone_tariff_id = models.IntegerField(blank=True, null=True)
    isp_phone_tariff_name = models.CharField(max_length=60, blank=True, null=True)
    cast_total_amount = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_isp_phone_log'
        unique_together = (('calling_line_time', 'calling_phone_num'),)


class TIspPhoneTariff(models.Model):
    isp_phone_tariff_id = models.AutoField(primary_key=True)
    isp_phone_num = models.CharField(max_length=64, blank=True, null=True)
    isp_phone_tariff_type_id = models.IntegerField(blank=True, null=True)
    isp_phone_tariff_name = models.CharField(max_length=60, blank=True, null=True)
    isp_brand_id = models.IntegerField(blank=True, null=True)
    isp_brand_name = models.CharField(max_length=60, blank=True, null=True)
    isp_phone_type_id = models.IntegerField(blank=True, null=True)
    isp_phone_type_name = models.CharField(max_length=60, blank=True, null=True)
    country_code = models.CharField(max_length=20, blank=True, null=True)
    country_name = models.CharField(max_length=60, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_isp_phone_tariff'


class TIspPhoneTariffType(models.Model):
    isp_phone_tariff_type_id = models.AutoField(primary_key=True)
    isp_phone_tariff_type_name = models.CharField(max_length=200)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_isp_phone_tariff_type'


class TIspPhoneType(models.Model):
    isp_phone_type_id = models.AutoField(primary_key=True)
    isp_phone_type_name = models.CharField(max_length=60)
    isp_brand_id = models.IntegerField(blank=True, null=True)
    isp_brand_name = models.CharField(max_length=60, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_isp_phone_type'


class TLicenseinfo(models.Model):
    productserialid = models.CharField(db_column='ProductSerialID', primary_key=True, max_length=64)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    productlicensestatue = models.IntegerField(db_column='ProductLicenseStatue', blank=True, null=True)  # Field name made lowercase.
    productactorlicense = models.IntegerField(db_column='ProductActorLicense', blank=True, null=True)  # Field name made lowercase.
    productguestlicense = models.IntegerField(db_column='ProductGuestLicense', blank=True, null=True)  # Field name made lowercase.
    productlist = models.CharField(db_column='ProductList', max_length=128, blank=True, null=True)  # Field name made lowercase.
    limitedendtime = models.DateTimeField(db_column='LimitedEndTime', blank=True, null=True)  # Field name made lowercase.
    limitedstarttime = models.DateTimeField(db_column='LimitedStartTime', blank=True, null=True)  # Field name made lowercase.
    maxvideowidth = models.IntegerField(db_column='MaxVideoWidth', blank=True, null=True)  # Field name made lowercase.
    maxvideoheight = models.IntegerField(db_column='MaxVideoHeight', blank=True, null=True)  # Field name made lowercase.
    supportmultivideo = models.IntegerField(db_column='SupportMultiVideo', blank=True, null=True)  # Field name made lowercase.
    supportdualdisp = models.IntegerField(db_column='SupportDualDisp', blank=True, null=True)  # Field name made lowercase.
    supportmobile = models.IntegerField(db_column='SupportMobile', blank=True, null=True)  # Field name made lowercase.
    supporthard = models.IntegerField(db_column='SupportHard', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.BigIntegerField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_licenseinfo'


class TLogin(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mid = models.IntegerField(db_column='MID', blank=True, null=True)  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_ADDRESS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    last_login_time = models.DateTimeField(db_column='LAST_LOGIN_TIME', blank=True, null=True)  # Field name made lowercase.
    broswer = models.CharField(db_column='BROSWER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    operation_system = models.CharField(db_column='OPERATION_SYSTEM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    login_time = models.DateTimeField(db_column='LOGIN_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_login'


class TLogs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_ip = models.CharField(db_column='USER_IP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    client_name = models.CharField(db_column='CLIENT_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    visite_date = models.DateTimeField(db_column='VISITE_DATE', blank=True, null=True)  # Field name made lowercase.
    login_entrace = models.IntegerField(db_column='LOGIN_ENTRACE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_logs'


class TMailset(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', unique=True)  # Field name made lowercase.
    smtp = models.CharField(max_length=128, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    mailusername = models.CharField(db_column='mailUsername', max_length=64, blank=True, null=True)  # Field name made lowercase.
    mailpwd = models.CharField(max_length=64, blank=True, null=True)
    createdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mailset'
        unique_together = (('id', 'userid'),)


class TMeetingrecord(models.Model):
    roomid = models.IntegerField(db_column='roomId')  # Field name made lowercase.
    attendusercount = models.IntegerField(db_column='attendUserCount', blank=True, null=True)  # Field name made lowercase.
    realstarttime = models.DateTimeField(db_column='realStartTime', blank=True, null=True)  # Field name made lowercase.
    realendtime = models.DateTimeField(db_column='realEndTime', blank=True, null=True)  # Field name made lowercase.
    mark = models.IntegerField()
    room_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_meetingrecord'


class TMember(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='PHONE_NUMBER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='COMPANY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    is_actived = models.IntegerField(db_column='IS_ACTIVED', blank=True, null=True)  # Field name made lowercase.
    user_type = models.IntegerField(db_column='USER_TYPE', blank=True, null=True)  # Field name made lowercase.
    register_time = models.CharField(db_column='REGISTER_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    time_zone = models.IntegerField(db_column='TIME_ZONE', blank=True, null=True)  # Field name made lowercase.
    active_code = models.CharField(db_column='ACTIVE_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    last_login_time = models.CharField(db_column='LAST_LOGIN_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    expiry_time = models.CharField(db_column='EXPIRY_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    activation_time = models.CharField(db_column='ACTIVATION_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pid = models.IntegerField(db_column='PID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_member'


class TMessage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=512)  # Field name made lowercase.
    ifview = models.CharField(db_column='ifView', max_length=1)  # Field name made lowercase.
    usertype = models.CharField(db_column='userType', max_length=1)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    operid = models.IntegerField(db_column='OperId', blank=True, null=True)  # Field name made lowercase.
    pathtitle = models.CharField(db_column='pathTitle', max_length=64, blank=True, null=True)  # Field name made lowercase.
    pathurl = models.CharField(db_column='pathUrl', max_length=128, blank=True, null=True)  # Field name made lowercase.
    ifbroadcast = models.CharField(db_column='ifBroadcast', max_length=1, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_message'


class TNews(models.Model):
    cate_id = models.IntegerField()
    title = models.CharField(max_length=256)
    tag = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_news'


class TNodeinfo(models.Model):
    nodeid = models.AutoField(db_column='NodeID', primary_key=True)  # Field name made lowercase.
    nodename = models.CharField(db_column='NodeName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    checkcode = models.CharField(db_column='CheckCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    nodedesc = models.CharField(db_column='NodeDesc', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodemanaddr = models.CharField(db_column='NodeManAddr', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nodemanurl = models.CharField(db_column='NodeManUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nodestatus = models.CharField(db_column='NodeStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    statusreasons = models.IntegerField(db_column='StatusReasons', blank=True, null=True)  # Field name made lowercase.
    parentnodeid = models.CharField(db_column='ParentNodeID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    parentdepartid = models.IntegerField(db_column='ParentDepartID', blank=True, null=True)  # Field name made lowercase.
    islocal = models.IntegerField(db_column='IsLocal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_nodeinfo'


class TOauthGoogle(models.Model):
    openid = models.CharField(primary_key=True, max_length=100)
    access_token = models.CharField(max_length=100, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_oauth_google'


class TOperator(models.Model):
    operatorid = models.AutoField(db_column='OperatorID', primary_key=True)  # Field name made lowercase.
    parentoperatorid = models.IntegerField(db_column='ParentOperatorID', blank=True, null=True)  # Field name made lowercase.
    operatornumber = models.CharField(db_column='OperatorNumber', max_length=64)  # Field name made lowercase.
    userlevel = models.CharField(db_column='UserLevel', max_length=1)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=64)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleID')  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=64, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    depositbalance = models.FloatField(db_column='depositBalance', blank=True, null=True)  # Field name made lowercase.
    lastlogindate = models.DateTimeField(db_column='LastLoginDate', blank=True, null=True)  # Field name made lowercase.
    zhekou = models.FloatField(db_column='Zhekou')  # Field name made lowercase.
    testnumber = models.IntegerField(db_column='TestNumber', blank=True, null=True)  # Field name made lowercase.
    devid = models.CharField(db_column='DEVID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    longesttime = models.IntegerField(db_column='longestTime', blank=True, null=True)  # Field name made lowercase.
    logins = models.IntegerField(db_column='Logins', blank=True, null=True)  # Field name made lowercase.
    pwderrorlogins = models.IntegerField(db_column='PwdErrorLogins', blank=True, null=True)  # Field name made lowercase.
    pwderrordate = models.DateTimeField(db_column='PwdErrorDate', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=64, blank=True, null=True)  # Field name made lowercase.
    agent_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_operator'
        unique_together = (('operatorid', 'operatornumber'),)


class TOperatorlog(models.Model):
    operatorlogid = models.AutoField(db_column='OperatorLogID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    userip = models.CharField(db_column='UserIP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    operation = models.CharField(db_column='Operation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    logtime = models.DateTimeField(db_column='LogTime')  # Field name made lowercase.
    preoperation = models.CharField(db_column='PreOperation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    objectname = models.CharField(db_column='ObjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    result = models.IntegerField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    errorinfo = models.CharField(db_column='ErrorInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    operationdesc = models.CharField(db_column='OperationDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_operatorlog'


class TOrder(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNO', max_length=20)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    orderoperatorid = models.IntegerField(db_column='OrderOperatorID', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=1)  # Field name made lowercase.
    ifline = models.CharField(db_column='ifLine', max_length=1)  # Field name made lowercase.
    processstate = models.CharField(db_column='processState', max_length=1, blank=True, null=True)  # Field name made lowercase.
    payprice = models.FloatField(db_column='payPrice', blank=True, null=True)  # Field name made lowercase.
    totalmoney = models.FloatField(db_column='TotalMoney')  # Field name made lowercase.
    disprice = models.FloatField(db_column='disPrice', blank=True, null=True)  # Field name made lowercase.
    gooddistotal = models.FloatField(db_column='GoodDisTotal', blank=True, null=True)  # Field name made lowercase.
    goodpayprice = models.FloatField(db_column='GoodPayPrice', blank=True, null=True)  # Field name made lowercase.
    pscore = models.CharField(db_column='Pscore', max_length=1, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=25, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=128, blank=True, null=True)  # Field name made lowercase.
    confirmdate = models.DateTimeField(db_column='ConfirmDate')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    upoperatorid = models.IntegerField(db_column='UpOperatorID', blank=True, null=True)  # Field name made lowercase.
    frombank = models.CharField(db_column='FromBank', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tobank = models.CharField(db_column='ToBank', max_length=256, blank=True, null=True)  # Field name made lowercase.
    billselectr = models.CharField(db_column='BillsElectr', max_length=128, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50, blank=True, null=True)  # Field name made lowercase.
    producttype = models.CharField(db_column='ProductType', max_length=1)  # Field name made lowercase.
    testorderstate = models.CharField(db_column='testOrderState', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prompt = models.CharField(db_column='Prompt', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cwremark = models.CharField(db_column='cwRemark', max_length=128, blank=True, null=True)  # Field name made lowercase.
    ordertype = models.IntegerField(db_column='orderType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_order'


class TOrderDetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    refno = models.IntegerField(db_column='REFNO', blank=True, null=True)  # Field name made lowercase.
    order_type = models.IntegerField(db_column='ORDER_TYPE', blank=True, null=True)  # Field name made lowercase.
    payment_date = models.DateTimeField(db_column='PAYMENT_DATE', blank=True, null=True)  # Field name made lowercase.
    due_to_pay_date = models.DateTimeField(db_column='DUE_TO_PAY_DATE', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    order_status = models.CharField(db_column='ORDER_STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_order_details'


class TOrderRepare(models.Model):
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    order_no = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 't_order_repare'


class TOrderitem(models.Model):
    orderitemid = models.AutoField(db_column='OrderItemID', primary_key=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    apiname = models.CharField(db_column='ApiName', max_length=64)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID')  # Field name made lowercase.
    types = models.CharField(db_column='Types', max_length=1)  # Field name made lowercase.
    subtype = models.CharField(db_column='Subtype', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    producttype = models.CharField(db_column='ProductType', max_length=1)  # Field name made lowercase.
    servicestypeid = models.IntegerField(db_column='ServicesTypeID', blank=True, null=True)  # Field name made lowercase.
    tariffmoduleid = models.IntegerField(db_column='TariffModuleID')  # Field name made lowercase.
    tariffname = models.CharField(db_column='TariffName', max_length=64)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    totalprice = models.FloatField(db_column='TotalPrice')  # Field name made lowercase.
    point = models.IntegerField(db_column='Point', blank=True, null=True)  # Field name made lowercase.
    bar = models.IntegerField(db_column='Bar', blank=True, null=True)  # Field name made lowercase.
    basiclength = models.FloatField(db_column='BasicLength', blank=True, null=True)  # Field name made lowercase.
    timelength = models.FloatField(db_column='TimeLength', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    surplustimelength = models.FloatField(db_column='SurplusTimeLength', blank=True, null=True)  # Field name made lowercase.
    ifexpireremind = models.CharField(db_column='ifExpireRemind', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remiddate = models.IntegerField(db_column='RemidDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_orderitem'


class TPaybankinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='bankName', max_length=64)  # Field name made lowercase.
    bankcardno = models.CharField(db_column='bankCardNo', max_length=64)  # Field name made lowercase.
    bankaccountname = models.CharField(db_column='bankAccountName', max_length=64)  # Field name made lowercase.
    ifclose = models.CharField(db_column='ifClose', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_paybankinfo'


class TPopUrl(models.Model):
    pop_url_id = models.AutoField(primary_key=True)
    pop_no = models.CharField(unique=True, max_length=128)
    pop_name = models.CharField(max_length=128)
    pop_url = models.CharField(max_length=256)
    pop_type = models.IntegerField(blank=True, null=True)
    stauts = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pop_url'


class TPopUserAuth(models.Model):
    pop_user_auth_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    pop_no = models.CharField(max_length=128)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pop_user_auth'
        unique_together = (('user_id', 'pop_no'),)


class TPopUserLog(models.Model):
    pop_user_log_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    pop_no = models.CharField(max_length=128)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_pop_user_log'
        unique_together = (('user_id', 'pop_no'),)


class TProduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    prods = models.IntegerField(db_column='PRODS', blank=True, null=True)  # Field name made lowercase.
    pname = models.CharField(db_column='PNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pcate = models.IntegerField(db_column='PCATE', blank=True, null=True)  # Field name made lowercase.
    ponline = models.SmallIntegerField(db_column='PONLINE', blank=True, null=True)  # Field name made lowercase.
    charge_type = models.IntegerField(db_column='CHARGE_TYPE', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    avangate_checkout_url = models.TextField(db_column='AVANGATE_CHECKOUT_URL', blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    update_date = models.CharField(db_column='UPDATE_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_product'


class TProservices(models.Model):
    proservicesid = models.AutoField(db_column='ProServicesID', primary_key=True)  # Field name made lowercase.
    prodservicesname = models.CharField(db_column='ProdServicesName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    prodservicesdesc = models.CharField(db_column='ProdServicesDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enabledata = models.CharField(db_column='EnableData', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enableaudio = models.CharField(db_column='EnableAudio', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enablevideo = models.CharField(db_column='EnableVideo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enablemobile = models.CharField(db_column='EnableMobile', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enablemultivideo = models.CharField(db_column='EnableMultiVideo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enabledualdisp = models.CharField(db_column='EnableDualDisp', max_length=1, blank=True, null=True)  # Field name made lowercase.
    wndmode = models.CharField(db_column='WndMode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    audiobrdcount = models.IntegerField(db_column='AudioBrdCount', blank=True, null=True)  # Field name made lowercase.
    videobrdcount = models.IntegerField(db_column='VideoBrdCount', blank=True, null=True)  # Field name made lowercase.
    videorcvcountchair = models.IntegerField(db_column='VideoRcvCountChair', blank=True, null=True)  # Field name made lowercase.
    videorcvcountattender = models.IntegerField(db_column='VideoRcvCountAttender', blank=True, null=True)  # Field name made lowercase.
    videowidth = models.IntegerField(db_column='VideoWidth', blank=True, null=True)  # Field name made lowercase.
    videoheight = models.IntegerField(db_column='VideoHeight', blank=True, null=True)  # Field name made lowercase.
    videoframerate = models.IntegerField(db_column='VideoFrameRate', blank=True, null=True)  # Field name made lowercase.
    videobitrate = models.IntegerField(db_column='VideoBitrate', blank=True, null=True)  # Field name made lowercase.
    i18n = models.CharField(db_column='I18N', max_length=10, blank=True, null=True)  # Field name made lowercase.
    videid = models.IntegerField(db_column='videID', blank=True, null=True)  # Field name made lowercase.
    meeting_max_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_proservices'


class TProservicesCopy(models.Model):
    proservicesid = models.AutoField(db_column='ProServicesID', primary_key=True)  # Field name made lowercase.
    prodservicesname = models.CharField(db_column='ProdServicesName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    prodservicesdesc = models.CharField(db_column='ProdServicesDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enabledata = models.CharField(db_column='EnableData', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enableaudio = models.CharField(db_column='EnableAudio', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enablevideo = models.CharField(db_column='EnableVideo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enablemobile = models.CharField(db_column='EnableMobile', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enablemultivideo = models.CharField(db_column='EnableMultiVideo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enabledualdisp = models.CharField(db_column='EnableDualDisp', max_length=1, blank=True, null=True)  # Field name made lowercase.
    wndmode = models.CharField(db_column='WndMode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    audiobrdcount = models.IntegerField(db_column='AudioBrdCount', blank=True, null=True)  # Field name made lowercase.
    videobrdcount = models.IntegerField(db_column='VideoBrdCount', blank=True, null=True)  # Field name made lowercase.
    videorcvcountchair = models.IntegerField(db_column='VideoRcvCountChair', blank=True, null=True)  # Field name made lowercase.
    videorcvcountattender = models.IntegerField(db_column='VideoRcvCountAttender', blank=True, null=True)  # Field name made lowercase.
    videowidth = models.IntegerField(db_column='VideoWidth', blank=True, null=True)  # Field name made lowercase.
    videoheight = models.IntegerField(db_column='VideoHeight', blank=True, null=True)  # Field name made lowercase.
    videoframerate = models.IntegerField(db_column='VideoFrameRate', blank=True, null=True)  # Field name made lowercase.
    videobitrate = models.IntegerField(db_column='VideoBitrate', blank=True, null=True)  # Field name made lowercase.
    i18n = models.CharField(db_column='I18N', max_length=10, blank=True, null=True)  # Field name made lowercase.
    videid = models.IntegerField(db_column='videID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_proservices_copy'


class TReportOrderHour(models.Model):
    id = models.BigAutoField(primary_key=True)
    begindatetime = models.DateTimeField(db_column='beginDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='endDateTime')  # Field name made lowercase.
    new_order_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_order_hour'


class TReportRoominfoHour(models.Model):
    id = models.BigAutoField(primary_key=True)
    begindatetime = models.DateTimeField(db_column='beginDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='endDateTime', blank=True, null=True)  # Field name made lowercase.
    scheduled_num = models.IntegerField(blank=True, null=True)
    started_num = models.IntegerField(blank=True, null=True)
    meeting_total_time = models.FloatField(blank=True, null=True)
    meeting_avg_time = models.FloatField(blank=True, null=True)
    and_num = models.IntegerField(blank=True, null=True)
    iph_num = models.IntegerField(blank=True, null=True)
    ipa_num = models.IntegerField(blank=True, null=True)
    mac_num = models.IntegerField(blank=True, null=True)
    web_num = models.IntegerField(blank=True, null=True)
    win_num = models.IntegerField(blank=True, null=True)
    user_meeting_total_time = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_roominfo_hour'


class TReportUserDay(models.Model):
    meeting_day = models.DateField(unique=True)
    start_meeting_num = models.IntegerField()
    renewal_succ_order_num = models.IntegerField()
    renewal_wait_order_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_report_user_day'


class TReportUserHour(models.Model):
    id = models.BigAutoField(primary_key=True)
    begindatetime = models.DateTimeField(db_column='beginDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='endDateTime', blank=True, null=True)  # Field name made lowercase.
    register_num = models.IntegerField(blank=True, null=True)
    activated_num = models.IntegerField(blank=True, null=True)
    activated_rate = models.FloatField(blank=True, null=True)
    contanct_num = models.IntegerField(blank=True, null=True)
    contanct_activated_num = models.IntegerField(blank=True, null=True)
    contanct_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_user_hour'


class TReview(models.Model):
    cate_id = models.IntegerField()
    title = models.CharField(max_length=256)
    review_url = models.CharField(max_length=256, blank=True, null=True)
    review_content = models.TextField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    pic_url = models.CharField(max_length=256, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_review'


class TRole(models.Model):
    roleid = models.AutoField(db_column='RoleID', primary_key=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=32)  # Field name made lowercase.
    roletype = models.IntegerField(db_column='RoleType')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zhekou = models.FloatField(db_column='Zhekou')  # Field name made lowercase.
    testnumber = models.IntegerField(db_column='TestNumber', blank=True, null=True)  # Field name made lowercase.
    longesttime = models.IntegerField(db_column='longestTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_role'


class TRoleright(models.Model):
    rolerightid = models.AutoField(db_column='RolerightID', primary_key=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleID')  # Field name made lowercase.
    funnumber = models.CharField(max_length=20)
    selectr = models.IntegerField(db_column='Selectr', blank=True, null=True)  # Field name made lowercase.
    insertr = models.IntegerField(db_column='Insertr', blank=True, null=True)  # Field name made lowercase.
    updater = models.IntegerField(db_column='Updater', blank=True, null=True)  # Field name made lowercase.
    delr = models.IntegerField(db_column='Delr', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_roleright'
        unique_together = (('rolerightid', 'roleid', 'funnumber'),)


class TRoomAuth(models.Model):
    primary_user_id = models.BigIntegerField(primary_key=True)
    child_user_id = models.BigIntegerField()
    room_id = models.BigIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_room_auth'
        unique_together = (('primary_user_id', 'child_user_id', 'room_id'),)


class TRoomchatmsg(models.Model):
    roomid = models.IntegerField(db_column='RoomID', blank=True, null=True)  # Field name made lowercase.
    srcuserid = models.IntegerField(db_column='SrcUserID', blank=True, null=True)  # Field name made lowercase.
    userrole = models.CharField(db_column='UserRole', max_length=1, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=128, blank=True, null=True)  # Field name made lowercase.
    srcusername = models.CharField(db_column='SrcUserName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_roomchatmsg'


class TRoomdocslist(models.Model):
    docid = models.CharField(db_column='DocID', primary_key=True, max_length=64)  # Field name made lowercase.
    roomid = models.IntegerField(db_column='RoomID', blank=True, null=True)  # Field name made lowercase.
    parentid = models.CharField(db_column='ParentID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    docname = models.CharField(db_column='DocName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    doctype = models.IntegerField(db_column='DocType', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    fileext = models.CharField(db_column='FileExt', max_length=16, blank=True, null=True)  # Field name made lowercase.
    filesize = models.IntegerField(db_column='FileSize', blank=True, null=True)  # Field name made lowercase.
    checkcode = models.IntegerField(db_column='CheckCode', blank=True, null=True)  # Field name made lowercase.
    creatorid = models.IntegerField(db_column='CreatorID', blank=True, null=True)  # Field name made lowercase.
    otheruserright = models.CharField(db_column='OtherUserRight', max_length=1, blank=True, null=True)  # Field name made lowercase.
    filewidth = models.IntegerField(db_column='FileWidth', blank=True, null=True)  # Field name made lowercase.
    fileheight = models.IntegerField(db_column='FileHeight', blank=True, null=True)  # Field name made lowercase.
    subfilecount = models.IntegerField(db_column='SubFileCount', blank=True, null=True)  # Field name made lowercase.
    fileurl = models.CharField(db_column='FileUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fileserviceid = models.IntegerField(db_column='FileServiceID', blank=True, null=True)  # Field name made lowercase.
    filecreatetime = models.DateTimeField(db_column='FileCreateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_roomdocslist'


class TRoominfo(models.Model):
    roomid = models.AutoField(db_column='RoomID', primary_key=True)  # Field name made lowercase.
    depid = models.IntegerField(db_column='DepID')  # Field name made lowercase.
    roomappid = models.IntegerField(db_column='RoomAppID', blank=True, null=True)  # Field name made lowercase.
    proservicesid = models.IntegerField(db_column='ProServicesID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=256)  # Field name made lowercase.
    roomdesc = models.CharField(db_column='RoomDesc', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45, blank=True, null=True)  # Field name made lowercase.
    verifymode = models.CharField(db_column='VerifyMode', max_length=1)  # Field name made lowercase.
    maxusercount = models.IntegerField(db_column='MaxUserCount')  # Field name made lowercase.
    curusercount = models.IntegerField(db_column='CurUserCount', blank=True, null=True)  # Field name made lowercase.
    roomtype = models.CharField(db_column='RoomType', max_length=1)  # Field name made lowercase.
    hopestarttime = models.DateTimeField(db_column='HopeStartTime', blank=True, null=True)  # Field name made lowercase.
    hopeendtime = models.DateTimeField(db_column='HopeEndTime', blank=True, null=True)  # Field name made lowercase.
    realstarttime = models.DateTimeField(db_column='realStartTime', blank=True, null=True)  # Field name made lowercase.
    realendtime = models.DateTimeField(db_column='realEndTime', blank=True, null=True)  # Field name made lowercase.
    cycleflag = models.CharField(db_column='CycleFlag', max_length=1, blank=True, null=True)  # Field name made lowercase.
    weeks = models.CharField(db_column='Weeks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dateeveymonth = models.CharField(db_column='DateEveyMonth', max_length=2, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    defaultmode = models.CharField(db_column='DefaultMode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    currentserviceid = models.IntegerField(db_column='CurrentServiceID', blank=True, null=True)  # Field name made lowercase.
    ifchairpwd = models.CharField(db_column='IfChairPwd', max_length=1)  # Field name made lowercase.
    chairpassword = models.CharField(db_column='ChairPassword', max_length=40, blank=True, null=True)  # Field name made lowercase.
    usedefaultflag = models.IntegerField(db_column='UseDefaultFlag')  # Field name made lowercase.
    defaultvideocodec = models.CharField(db_column='DefaultVideoCodec', max_length=1, blank=True, null=True)  # Field name made lowercase.
    defaultvideowind = models.CharField(db_column='DefaultVideoWind', max_length=1, blank=True, null=True)  # Field name made lowercase.
    defaultvideoqos = models.CharField(db_column='DefaultVideoQOS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    defaultvideobitrate = models.IntegerField(db_column='DefaultVideoBitrate', blank=True, null=True)  # Field name made lowercase.
    defaultvideoquality = models.IntegerField(db_column='DefaultVideoQuality', blank=True, null=True)  # Field name made lowercase.
    devid = models.CharField(db_column='DevID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    enabledynamicdev = models.CharField(db_column='EnableDynamicDev', max_length=1, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    videid = models.IntegerField(db_column='videID', blank=True, null=True)  # Field name made lowercase.
    loginroomno = models.IntegerField(db_column='loginRoomNo')  # Field name made lowercase.
    mark = models.CharField(max_length=1, blank=True, null=True)
    attend_url = models.CharField(max_length=100, blank=True, null=True)
    time_zone_code = models.CharField(max_length=20, blank=True, null=True)
    attend_user_count = models.IntegerField()
    system_id = models.IntegerField(blank=True, null=True)
    message_preset_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_roominfo'


class TRoominfoAction(models.Model):
    id = models.BigAutoField(primary_key=True)
    room_id = models.BigIntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    refused = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_roominfo_action'


class TRoominfoJob(models.Model):
    room_job_id = models.BigAutoField(primary_key=True)
    room_id = models.BigIntegerField()
    type = models.IntegerField(blank=True, null=True)
    meeting_id = models.IntegerField()
    work_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_roominfo_job'
        unique_together = (('room_id', 'type'),)


class TRoominfoWebinar(models.Model):
    roominfo_webinar_id = models.BigAutoField(primary_key=True)
    room_id = models.BigIntegerField(unique=True)
    meeting_id = models.BigIntegerField()
    webinar_room_type = models.IntegerField(blank=True, null=True)
    access_type = models.IntegerField(blank=True, null=True)
    auto_recoding_status = models.IntegerField(blank=True, null=True)
    backgroup_pic_url = models.CharField(max_length=300, blank=True, null=True)
    logo_pic_url = models.CharField(max_length=300, blank=True, null=True)
    webinar_room_status = models.IntegerField(blank=True, null=True)
    agenda_content = models.TextField(blank=True, null=True)
    registration_field = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    register_num = models.IntegerField(blank=True, null=True)
    participants_num = models.IntegerField(blank=True, null=True)
    invite_num = models.IntegerField(blank=True, null=True)
    registration_required = models.IntegerField(blank=True, null=True)
    approval_required = models.IntegerField(blank=True, null=True)
    thanks_content = models.TextField(blank=True, null=True)
    webinar_is = models.IntegerField(blank=True, null=True)
    payment_platform = models.IntegerField(blank=True, null=True)
    accept_account = models.CharField(max_length=128, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    video_storage_id = models.BigIntegerField(blank=True, null=True)
    webinar_type = models.IntegerField(blank=True, null=True)
    live_streaming = models.CharField(max_length=2000, blank=True, null=True)
    auto_live_streaming = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_roominfo_webinar'


class TRoominfoWebinarInvoice(models.Model):
    webinar_invoice_id = models.BigAutoField(primary_key=True)
    webinar_register_id = models.BigIntegerField(blank=True, null=True)
    payment_platform = models.IntegerField(blank=True, null=True)
    accept_account = models.CharField(max_length=128, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    payment_id = models.CharField(max_length=128, blank=True, null=True)
    pay_account = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_roominfo_webinar_invoice'


class TRoominfoWebinarRegisters(models.Model):
    webinar_register_id = models.BigAutoField(primary_key=True)
    room_id = models.BigIntegerField()
    roominfo_webinar_id = models.BigIntegerField()
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    company_name = models.CharField(max_length=128, blank=True, null=True)
    phone_num = models.CharField(max_length=128, blank=True, null=True)
    office_number = models.CharField(max_length=128, blank=True, null=True)
    department = models.CharField(max_length=128, blank=True, null=True)
    industry = models.CharField(max_length=128, blank=True, null=True)
    linkedin = models.CharField(max_length=128, blank=True, null=True)
    facebook = models.CharField(max_length=128, blank=True, null=True)
    twitter = models.CharField(max_length=128, blank=True, null=True)
    invitation_code = models.IntegerField(blank=True, null=True)
    country_code = models.CharField(max_length=50, blank=True, null=True)
    country_name = models.CharField(max_length=50, blank=True, null=True)
    join_status = models.IntegerField(blank=True, null=True)
    invite_status = models.IntegerField(blank=True, null=True)
    register_status = models.IntegerField(blank=True, null=True)
    register_time = models.DateTimeField(blank=True, null=True)
    invite_time = models.DateTimeField(blank=True, null=True)
    last_join_time = models.DateTimeField(blank=True, null=True)
    user_ip = models.CharField(max_length=50, blank=True, null=True)
    browser = models.CharField(max_length=50, blank=True, null=True)
    os_platform = models.CharField(max_length=50, blank=True, null=True)
    device_name = models.CharField(max_length=50, blank=True, null=True)
    presenter_status = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)
    approval_status = models.IntegerField(blank=True, null=True)
    is_paid = models.IntegerField(blank=True, null=True)
    webinar_invoice_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_roominfo_webinar_registers'
        unique_together = (('room_id', 'invitation_code'),)


class TRoominfoWebinarTime(models.Model):
    webinar_time_id = models.BigAutoField(primary_key=True)
    room_id = models.BigIntegerField(blank=True, null=True)
    meeting_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_roominfo_webinar_time'


class TRoomlog(models.Model):
    roomlogid = models.AutoField(db_column='RoomLogID', primary_key=True)  # Field name made lowercase.
    serviceid = models.IntegerField(db_column='ServiceID', blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    roomid = models.IntegerField(db_column='RoomID')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    userip = models.CharField(db_column='UserIP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    entertime = models.DateTimeField(db_column='EnterTime', blank=True, null=True)  # Field name made lowercase.
    leavetime = models.DateTimeField(db_column='LeaveTime', blank=True, null=True)  # Field name made lowercase.
    eventcode = models.IntegerField(db_column='EventCode', blank=True, null=True)  # Field name made lowercase.
    eventdesc = models.CharField(db_column='EventDesc', max_length=255)  # Field name made lowercase.
    logtime = models.DateTimeField(db_column='LogTime', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(blank=True, null=True)
    client_version = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    user_type = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    product_id = models.CharField(max_length=16, blank=True, null=True)
    dev_id = models.CharField(max_length=64, blank=True, null=True)
    area_code = models.CharField(max_length=20, blank=True, null=True)
    browser = models.CharField(max_length=50, blank=True, null=True)
    os_platform = models.CharField(max_length=50, blank=True, null=True)
    device_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_roomlog'


class TRoomlogCopy(models.Model):
    roomlogid = models.AutoField(db_column='RoomLogID', primary_key=True)  # Field name made lowercase.
    serviceid = models.IntegerField(db_column='ServiceID', blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    roomid = models.IntegerField(db_column='RoomID')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    userip = models.CharField(db_column='UserIP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    entertime = models.DateTimeField(db_column='EnterTime', blank=True, null=True)  # Field name made lowercase.
    leavetime = models.DateTimeField(db_column='LeaveTime', blank=True, null=True)  # Field name made lowercase.
    eventcode = models.IntegerField(db_column='EventCode', blank=True, null=True)  # Field name made lowercase.
    eventdesc = models.CharField(db_column='EventDesc', max_length=255)  # Field name made lowercase.
    logtime = models.DateTimeField(db_column='LogTime', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(blank=True, null=True)
    client_version = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    user_type = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    product_id = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_roomlog_copy'


class TRoomrouteinfo(models.Model):
    roomsrvnodeid = models.CharField(db_column='RoomSrvNodeID', primary_key=True, max_length=128)  # Field name made lowercase.
    roomid = models.IntegerField(db_column='RoomID')  # Field name made lowercase.
    srvnodeid = models.CharField(db_column='SrvNodeID', max_length=128)  # Field name made lowercase.
    srvauthcode = models.CharField(db_column='SrvAuthCode', max_length=128)  # Field name made lowercase.
    srvappid = models.IntegerField(db_column='SrvAppID')  # Field name made lowercase.
    roomnodeid = models.CharField(db_column='RoomNodeID', max_length=64)  # Field name made lowercase.
    parentsrvnodeid = models.CharField(db_column='ParentSrvNodeID', max_length=128)  # Field name made lowercase.
    parentsrvaddr = models.CharField(db_column='ParentSrvAddr', max_length=512)  # Field name made lowercase.
    parentsrvappid = models.IntegerField(db_column='ParentSrvAppID')  # Field name made lowercase.
    parentauthcode = models.CharField(db_column='ParentAuthCode', max_length=128)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_roomrouteinfo'
        unique_together = (('roomsrvnodeid', 'roomid', 'srvnodeid', 'srvappid'),)


class TRoomruninfo(models.Model):
    nodeid = models.CharField(db_column='NodeID', primary_key=True, max_length=64)  # Field name made lowercase.
    roomid = models.IntegerField(db_column='RoomID')  # Field name made lowercase.
    roomappid = models.IntegerField(db_column='RoomAppID')  # Field name made lowercase.
    maxusercount = models.IntegerField(db_column='MaxUserCount')  # Field name made lowercase.
    devid = models.CharField(db_column='DevID', max_length=64)  # Field name made lowercase.
    devreqtime = models.DateTimeField(db_column='DevReqTime')  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_roomruninfo'
        unique_together = (('nodeid', 'roomid'),)


class TRoomusers(models.Model):
    userrightid = models.AutoField(db_column='UserRightID', primary_key=True)  # Field name made lowercase.
    roomid = models.IntegerField(db_column='RoomID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    userright = models.CharField(db_column='UserRight', max_length=1)  # Field name made lowercase.
    online = models.CharField(db_column='Online', max_length=1, blank=True, null=True)  # Field name made lowercase.
    seatlist = models.IntegerField(db_column='SeatList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_roomusers'


class TSendinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sendtime = models.DateTimeField(db_column='SendTime')  # Field name made lowercase.
    timingtype = models.IntegerField(db_column='TimingType', blank=True, null=True)  # Field name made lowercase.
    sendobj = models.TextField(db_column='SendObj', blank=True, null=True)  # Field name made lowercase.
    edittype = models.IntegerField(db_column='EditType')  # Field name made lowercase.
    content = models.TextField(db_column='Content')  # Field name made lowercase.
    sendtype = models.IntegerField(db_column='SendType', blank=True, null=True)  # Field name made lowercase.
    roomid = models.IntegerField(db_column='RoomID', blank=True, null=True)  # Field name made lowercase.
    resultsuccess = models.TextField(db_column='ResultSuccess')  # Field name made lowercase.
    resultfail = models.TextField(db_column='ResultFail', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    timingflag = models.CharField(db_column='TimingFlag', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fromdisplayname = models.CharField(db_column='FromDisplayName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fromtelphone = models.CharField(db_column='FromTelphone', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sendinfo'


class TService(models.Model):
    service_id = models.BigAutoField(primary_key=True)
    service_category_id = models.BigIntegerField()
    service_name = models.CharField(max_length=100)
    service_desc = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=125, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    month_amount = models.DecimalField(max_digits=12, decimal_places=2)
    yearly_amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_month_buy = models.IntegerField()
    is_yearly_buy = models.IntegerField()
    has_hardware = models.IntegerField()
    sort_order = models.IntegerField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_service'


class TServiceCategory(models.Model):
    service_category_id = models.BigIntegerField(primary_key=True)
    service_category_name = models.CharField(unique=True, max_length=100)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_service_category'


class TServiceDevice(models.Model):
    service_id = models.BigIntegerField(primary_key=True)
    device_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 't_service_device'
        unique_together = (('service_id', 'device_id'),)


class TServiceOrder(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    order_code = models.CharField(max_length=20)
    user_id = models.BigIntegerField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    actual_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.IntegerField()
    create_time = models.DateTimeField()
    pay_time = models.DateTimeField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    consignee = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    country_id = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=1200, blank=True, null=True)
    address_line_one = models.CharField(max_length=255, blank=True, null=True)
    address_line_two = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=70, blank=True, null=True)
    state = models.CharField(max_length=70, blank=True, null=True)
    country_name = models.CharField(max_length=70, blank=True, null=True)
    frist_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_service_order'


class TServiceOrderDetail(models.Model):
    order_detail_id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField()
    order_code = models.CharField(max_length=20)
    service_category_id = models.BigIntegerField()
    service_id = models.BigIntegerField()
    service_name = models.CharField(max_length=50)
    user_id = models.BigIntegerField()
    discount_code = models.CharField(max_length=50, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    billing_cycle = models.IntegerField()
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    actual_amount = models.DecimalField(max_digits=12, decimal_places=2)
    shipping_status = models.IntegerField()
    type = models.IntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)
    choice_num = models.IntegerField(blank=True, null=True)
    billing_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_service_order_detail'


class TServiceinfo(models.Model):
    serviceid = models.AutoField(db_column='ServiceID', primary_key=True)  # Field name made lowercase.
    serviceappid = models.IntegerField(db_column='ServiceAppID')  # Field name made lowercase.
    servicename = models.CharField(db_column='ServiceName', max_length=64)  # Field name made lowercase.
    serviceaddrs = models.CharField(db_column='ServiceAddrs', max_length=512)  # Field name made lowercase.
    servicestatus = models.CharField(db_column='ServiceStatus', max_length=1)  # Field name made lowercase.
    devid = models.CharField(db_column='DevID', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_serviceinfo'


class TServicestype(models.Model):
    servicestypeid = models.AutoField(db_column='ServicesTypeID', primary_key=True)  # Field name made lowercase.
    servicestypename = models.CharField(db_column='ServicesTypeName', max_length=64)  # Field name made lowercase.
    typeid = models.CharField(max_length=1)
    servicesid = models.IntegerField(db_column='ServicesID', blank=True, null=True)  # Field name made lowercase.
    i18n = models.CharField(db_column='I18N', max_length=10, blank=True, null=True)  # Field name made lowercase.
    service_desc = models.TextField(blank=True, null=True)
    agents_id = models.IntegerField()
    expire_day = models.IntegerField(blank=True, null=True)
    is_free = models.CharField(max_length=1, blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_servicestype'


class TServicestypeCopy(models.Model):
    servicestypeid = models.AutoField(db_column='ServicesTypeID', primary_key=True)  # Field name made lowercase.
    servicestypename = models.CharField(db_column='ServicesTypeName', max_length=64)  # Field name made lowercase.
    typeid = models.CharField(max_length=1)
    servicesid = models.IntegerField(db_column='ServicesID', blank=True, null=True)  # Field name made lowercase.
    i18n = models.CharField(db_column='I18N', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_servicestype_copy'


class TServicestypeExt(models.Model):
    name = models.CharField(max_length=64)
    typeid = models.CharField(max_length=1)
    service_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_servicestype_ext'


class TServicestypeExtMiddle(models.Model):
    service_id = models.IntegerField(primary_key=True)
    ext_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_servicestype_ext_middle'
        unique_together = (('service_id', 'ext_id'),)


class TServicestypeExtWebinar(models.Model):
    ext_id = models.IntegerField(primary_key=True)
    point = models.IntegerField()
    service_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_servicestype_ext_webinar'


class TSiteUrl(models.Model):
    url = models.CharField(max_length=200)
    p_url = models.CharField(max_length=200, blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_url'


class TSjcrm(models.Model):
    cnumber = models.CharField(max_length=20, blank=True, null=True)
    companyname = models.CharField(db_column='CompanyName', max_length=216)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=64, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=64, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=64, blank=True, null=True)  # Field name made lowercase.
    qq = models.CharField(db_column='QQ', max_length=32, blank=True, null=True)  # Field name made lowercase.
    progress = models.TextField(db_column='Progress', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sjcrm'


class TSjgroupoper(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    lastgetdate = models.DateTimeField(db_column='LastGetDate')  # Field name made lowercase.
    logindate = models.DateTimeField(db_column='LoginDate', blank=True, null=True)  # Field name made lowercase.
    assigndate = models.DateTimeField(db_column='AssignDate')  # Field name made lowercase.
    pageonlinedate = models.DateTimeField(db_column='PageOnlineDate', blank=True, null=True)  # Field name made lowercase.
    logoutdate = models.DateTimeField(db_column='LogoutDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sjgroupoper'


class TSjgroupregion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID')  # Field name made lowercase.
    regionid = models.IntegerField(db_column='RegionID')  # Field name made lowercase.
    grouptype = models.CharField(db_column='GroupType', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sjgroupregion'


class TSjgroups(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=128)  # Field name made lowercase.
    groupdesc = models.TextField(db_column='GroupDesc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sjgroups'


class TSjopportunities(models.Model):
    opportid = models.AutoField(db_column='opportID', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=128)  # Field name made lowercase.
    regionid = models.IntegerField(db_column='RegionID')  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=100)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=64, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=64, blank=True, null=True)  # Field name made lowercase.
    qq = models.CharField(db_column='QQ', max_length=32, blank=True, null=True)  # Field name made lowercase.
    clientsource = models.CharField(db_column='ClientSource', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sourcekeyword = models.CharField(db_column='SourceKeyword', max_length=128, blank=True, null=True)  # Field name made lowercase.
    mainpurpose = models.TextField(db_column='MainPurpose')  # Field name made lowercase.
    needpoint = models.IntegerField(db_column='NeedPoint', blank=True, null=True)  # Field name made lowercase.
    hztype = models.CharField(db_column='Hztype', max_length=1)  # Field name made lowercase.
    remark = models.TextField(blank=True, null=True)
    groupid = models.IntegerField(db_column='GroupID')  # Field name made lowercase.
    createid = models.IntegerField(db_column='CreateID')  # Field name made lowercase.
    assignid = models.IntegerField(db_column='AssignID', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    assigndate = models.DateTimeField(db_column='AssignDate', blank=True, null=True)  # Field name made lowercase.
    getdate = models.DateTimeField(db_column='GetDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sjopportunities'


class TSjregion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    regionname = models.CharField(db_column='RegionName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    regiontype = models.IntegerField(db_column='RegionType', blank=True, null=True)  # Field name made lowercase.
    regionparent = models.IntegerField(db_column='RegionParent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sjregion'


class TSn(models.Model):
    snid = models.AutoField(db_column='SnID', primary_key=True)  # Field name made lowercase.
    orderno = models.IntegerField(db_column='OrderNO')  # Field name made lowercase.
    types = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 't_sn'


class TSpecialPage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cate_id = models.CharField(db_column='CATE_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    create_time = models.CharField(db_column='CREATE_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    update_time = models.CharField(db_column='UPDATE_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='SORT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_special_page'


class TSpfinancelog(models.Model):
    spfinancelogid = models.AutoField(db_column='SpFinanceLogID', primary_key=True)  # Field name made lowercase.
    stuts = models.IntegerField(db_column='Stuts')  # Field name made lowercase.
    tradetype = models.IntegerField(db_column='TradeType')  # Field name made lowercase.
    trademoney = models.FloatField(db_column='TradeMoney')  # Field name made lowercase.
    paymode = models.CharField(db_column='PayMode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    glidenumber = models.IntegerField(db_column='GlideNumber', blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    upoperatorid = models.IntegerField(db_column='UpOperatorID', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='Createdate', blank=True, null=True)  # Field name made lowercase.
    accttype = models.CharField(db_column='AcctType', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_spfinancelog'


class TStripePayment(models.Model):
    stripe_id = models.CharField(max_length=50, blank=True, null=True)
    stripe_email = models.CharField(max_length=50, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stripe_payment'


class TSysresource(models.Model):
    funnumber = models.IntegerField(primary_key=True)
    fathernumber = models.IntegerField(blank=True, null=True)
    funname = models.CharField(max_length=64, blank=True, null=True)
    funpath = models.CharField(max_length=128, blank=True, null=True)
    ismenu = models.FloatField()
    dolog = models.FloatField(blank=True, null=True)
    funlevel = models.FloatField(blank=True, null=True)
    orderno = models.FloatField(blank=True, null=True)
    i18ncode = models.CharField(max_length=50, blank=True, null=True)
    icon = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sysresource'


class TSystemConfig(models.Model):
    prm_opid = models.IntegerField(blank=True, null=True)
    prm_name = models.CharField(unique=True, max_length=60)
    prm_value = models.CharField(max_length=200)
    prm_remark = models.CharField(max_length=200, blank=True, null=True)
    prm_createtime = models.DateTimeField(db_column='prm_createTime', blank=True, null=True)  # Field name made lowercase.
    prm_status = models.IntegerField()
    prm_clienttype = models.IntegerField(blank=True, null=True)
    prm_configtype = models.IntegerField(blank=True, null=True)
    prm_updatetime = models.DateTimeField(blank=True, null=True)
    prm_updateopid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_system_config'


class TTariffPkg(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    service_type = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    max_host = models.IntegerField(blank=True, null=True)
    min_host = models.IntegerField(blank=True, null=True)
    charge_type = models.IntegerField(blank=True, null=True)
    meeting_max_time = models.IntegerField(blank=True, null=True)
    meeting_total = models.IntegerField(blank=True, null=True)
    meeting_is_cycle = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=9, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    attendees_level = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 't_tariff_pkg'


class TTariffPkgExt(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    extservice_type = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    charge_type = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_tariff_pkg_ext'


class TTariffelem(models.Model):
    tariffelemid = models.AutoField(db_column='TariffelemID', primary_key=True)  # Field name made lowercase.
    elemname = models.CharField(db_column='ElemName', max_length=20)  # Field name made lowercase.
    elemunit = models.CharField(db_column='ElemUnit', max_length=20)  # Field name made lowercase.
    timelength = models.IntegerField(db_column='TimeLength')  # Field name made lowercase.
    elemtype = models.CharField(db_column='ElemType', max_length=1)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True, null=True)
    i18n = models.CharField(db_column='I18N', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_tariffelem'


class TTariffmodule(models.Model):
    tariffmoduleid = models.AutoField(db_column='TariffModuleID', primary_key=True)  # Field name made lowercase.
    servicestypeid = models.IntegerField(db_column='ServicesTypeID')  # Field name made lowercase.
    tariffmodulename = models.CharField(db_column='TariffModuleName', max_length=64)  # Field name made lowercase.
    i18n = models.CharField(db_column='I18N', max_length=10, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    addpoint = models.FloatField(db_column='AddPoint', blank=True, null=True)  # Field name made lowercase.
    addbar = models.IntegerField(db_column='AddBar', blank=True, null=True)  # Field name made lowercase.
    addtimerule = models.FloatField(db_column='AddTimeRule', blank=True, null=True)  # Field name made lowercase.
    cheapstarttime = models.DateTimeField(db_column='CheapStartTime', blank=True, null=True)  # Field name made lowercase.
    cheapendtime = models.DateTimeField(db_column='CheapEndTime', blank=True, null=True)  # Field name made lowercase.
    cheaprule = models.FloatField(db_column='CheapRule', blank=True, null=True)  # Field name made lowercase.
    runformat = models.CharField(db_column='RunFormat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    types = models.CharField(max_length=1)
    producttype = models.CharField(db_column='productType', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    freetype = models.CharField(db_column='FreeType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    elemtype = models.CharField(db_column='ElemType', max_length=1)  # Field name made lowercase.
    point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_tariffmodule'


class TTariffproitem(models.Model):
    tariffproitemid = models.AutoField(db_column='TariffProItemID', primary_key=True)  # Field name made lowercase.
    parenttariffproid = models.IntegerField(db_column='ParentTariffProID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    tariffmoduleid = models.IntegerField(db_column='TariffModuleID', blank=True, null=True)  # Field name made lowercase.
    tariffproname = models.CharField(db_column='TariffProName', max_length=50)  # Field name made lowercase.
    bar = models.IntegerField(db_column='Bar', blank=True, null=True)  # Field name made lowercase.
    videopoints = models.IntegerField(db_column='VideoPoints', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    addtime = models.IntegerField(db_column='AddTime', blank=True, null=True)  # Field name made lowercase.
    tariffprotype = models.CharField(db_column='TariffProType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    totalprice = models.FloatField(db_column='TotalPrice', blank=True, null=True)  # Field name made lowercase.
    oritotalprice = models.FloatField(db_column='OriTotalPrice', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_tariffproitem'


class TTariffrule(models.Model):
    ruleid = models.AutoField(db_column='RuleID', primary_key=True)  # Field name made lowercase.
    rulename = models.CharField(db_column='RuleName', max_length=50)  # Field name made lowercase.
    rulestartvalue = models.IntegerField(db_column='RuleStartValue')  # Field name made lowercase.
    ruleendvalue = models.IntegerField(db_column='RuleEndValue')  # Field name made lowercase.
    rulevalue = models.FloatField(db_column='RuleValue')  # Field name made lowercase.
    ruletype = models.CharField(db_column='RuleType', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_tariffrule'


class TTimeZone(models.Model):
    time_zone_code = models.CharField(max_length=50, blank=True, null=True)
    time_zone_name = models.CharField(max_length=128, blank=True, null=True)
    time_zone_desc = models.CharField(max_length=128, blank=True, null=True)
    time_zone_gmt = models.CharField(max_length=128, blank=True, null=True)
    time_zone_id = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_time_zone'


class TTimetotimelog(models.Model):
    logid = models.AutoField(db_column='LogID', primary_key=True)  # Field name made lowercase.
    stuts = models.CharField(db_column='Stuts', max_length=1)  # Field name made lowercase.
    tradetype = models.CharField(db_column='TradeType', max_length=1)  # Field name made lowercase.
    trademoney = models.FloatField(db_column='TradeMoney')  # Field name made lowercase.
    tradetimelength = models.IntegerField(db_column='TradeTimeLength', blank=True, null=True)  # Field name made lowercase.
    smsbar = models.IntegerField(db_column='SmsBar', blank=True, null=True)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='Createdate')  # Field name made lowercase.
    billingdate = models.DateTimeField(db_column='BillingDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_timetotimelog'


class TTips(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cateid = models.IntegerField(db_column='CATEID', blank=True, null=True)  # Field name made lowercase.
    editor = models.IntegerField(db_column='EDITOR', blank=True, null=True)  # Field name made lowercase.
    is_top = models.IntegerField(db_column='IS_TOP', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    seo_title = models.CharField(db_column='SEO_TITLE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    is_recommen_howto = models.IntegerField(db_column='IS_RECOMMEN_HOWTO', blank=True, null=True)  # Field name made lowercase.
    publish_method = models.CharField(db_column='PUBLISH_METHOD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    publish_date = models.CharField(db_column='PUBLISH_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    set_publish_date = models.CharField(db_column='SET_PUBLISH_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_time = models.CharField(db_column='CREATE_TIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    update_time = models.CharField(db_column='UPDATE_TIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_deleted = models.IntegerField(db_column='IS_DELETED', blank=True, null=True)  # Field name made lowercase.
    view_count = models.IntegerField(db_column='VIEW_COUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_tips'


class TTokeninfo(models.Model):
    tokenid = models.CharField(db_column='TokenID', primary_key=True, max_length=64)  # Field name made lowercase.
    nodeid = models.CharField(db_column='NodeID', max_length=64)  # Field name made lowercase.
    departid = models.IntegerField(db_column='DepartID')  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    roomid = models.IntegerField(db_column='RoomID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    termianltype = models.IntegerField(db_column='TermianlType')  # Field name made lowercase.
    userright = models.IntegerField(db_column='UserRight')  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=64)  # Field name made lowercase.
    userrole = models.IntegerField(db_column='UserRole')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    activetime = models.DateTimeField(db_column='ActiveTime')  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID')  # Field name made lowercase.
    activeid = models.IntegerField(db_column='ActiveID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_tokeninfo'


class TUrl(models.Model):
    url_key = models.CharField(max_length=10, blank=True, null=True)
    source = models.CharField(max_length=120, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    target_name = models.CharField(max_length=120, blank=True, null=True)
    dsc = models.CharField(max_length=300, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_url'


class TUserActivityFree(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    free_id = models.IntegerField()
    service_expire = models.CharField(max_length=10, blank=True, null=True)
    ext_service_expire = models.CharField(max_length=10, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_activity_free'


class TUserBaseServiceOrder(models.Model):
    order_code = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    service_type = models.IntegerField(blank=True, null=True)
    tariffpkg_id = models.IntegerField(blank=True, null=True)
    host = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    coupon_code = models.CharField(max_length=30, blank=True, null=True)
    amout = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    order_type = models.CharField(max_length=3, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    cycle_amout = models.FloatField(blank=True, null=True)
    amount_org = models.FloatField(blank=True, null=True)
    amount_coupon = models.FloatField(blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField()
    give_source_order_code = models.CharField(max_length=20, blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    choice_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_base_service_order'


class TUserBindCardOrder(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    order_code = models.CharField(max_length=20, blank=True, null=True)
    amout = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_bind_card_order'


class TUserInvoice(models.Model):
    type = models.CharField(max_length=1, blank=True, null=True)
    order_code = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    service_category_name = models.CharField(max_length=100, blank=True, null=True)
    service_name = models.CharField(max_length=1000, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    pay_platform = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    card_no = models.CharField(max_length=128, blank=True, null=True)
    card_brand = models.CharField(max_length=36, blank=True, null=True)
    mode = models.CharField(max_length=1, blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    country_id = models.BigIntegerField(blank=True, null=True)
    country_name = models.CharField(max_length=70, blank=True, null=True)
    address_line_one = models.CharField(max_length=255, blank=True, null=True)
    address_line_two = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=70, blank=True, null=True)
    state = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_invoice'


class TUserOrderItem(models.Model):
    order_code = models.CharField(max_length=20, blank=True, null=True)
    worldpay_code = models.CharField(max_length=20, blank=True, null=True)
    cutpayment_time = models.DateTimeField(blank=True, null=True)
    card_number = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=3, blank=True, null=True)
    user_id = models.IntegerField()
    card_brand = models.CharField(max_length=36, blank=True, null=True)
    subscription_id = models.BigIntegerField(blank=True, null=True)
    subscription_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_order_item'


class TUserOrderPlan(models.Model):
    type = models.CharField(max_length=1, blank=True, null=True)
    service_name = models.CharField(max_length=64, blank=True, null=True)
    order_code = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    next_billing_date = models.DateTimeField(blank=True, null=True)
    cut_payment_num = models.IntegerField(blank=True, null=True)
    amout = models.FloatField(blank=True, null=True)
    explain = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_order_plan'


class TUserPayToken(models.Model):
    user_id = models.IntegerField()
    agent_id = models.IntegerField()
    card_no = models.CharField(max_length=36, blank=True, null=True)
    token_id = models.CharField(primary_key=True, max_length=40)
    create_time = models.DateTimeField(blank=True, null=True)
    card_brand = models.CharField(max_length=36, blank=True, null=True)
    is_default = models.CharField(max_length=1, blank=True, null=True)
    cus_id = models.CharField(max_length=50, blank=True, null=True)
    exp_month = models.IntegerField(blank=True, null=True)
    exp_year = models.IntegerField(blank=True, null=True)
    card_holder_name = models.CharField(max_length=64, blank=True, null=True)
    card_type = models.IntegerField(blank=True, null=True)
    shipping_id = models.IntegerField(blank=True, null=True)
    card_source = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_pay_token'
        unique_together = (('token_id', 'user_id', 'agent_id'),)


class TUserShippingAddress(models.Model):
    user_shipping_address_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    frist_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_name = models.CharField(max_length=30, blank=True, null=True)
    address_line_one = models.CharField(max_length=255, blank=True, null=True)
    address_line_two = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=70, blank=True, null=True)
    state = models.CharField(max_length=70, blank=True, null=True)
    zip = models.CharField(max_length=30, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_shipping_address'


class TUserStorage(models.Model):
    user_storage_id = models.BigAutoField(primary_key=True)
    mine_type = models.CharField(max_length=64, blank=True, null=True)
    file_source = models.IntegerField(blank=True, null=True)
    vir_name = models.CharField(max_length=128, blank=True, null=True)
    real_name = models.CharField(max_length=128, blank=True, null=True)
    bucket_name = models.CharField(max_length=128, blank=True, null=True)
    region_name = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    file_size = models.BigIntegerField(blank=True, null=True)
    room_id = models.BigIntegerField(blank=True, null=True)
    meeting_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    room_type = models.IntegerField(blank=True, null=True)
    file_status = models.IntegerField(blank=True, null=True)
    download_url = models.CharField(max_length=300, blank=True, null=True)
    expiration_time = models.DateTimeField(blank=True, null=True)
    join_trash_time = models.DateTimeField(blank=True, null=True)
    upload_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_storage'


class TUserStorageSize(models.Model):
    user_storage_size_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True)
    free_size = models.BigIntegerField()
    meeting_size = models.BigIntegerField(blank=True, null=True)
    webinar_size = models.BigIntegerField(blank=True, null=True)
    buy_size = models.BigIntegerField(blank=True, null=True)
    real_size = models.BigIntegerField(blank=True, null=True)
    used_size = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_storage_size'


class TUserSubscription(models.Model):
    subscription_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    order_code = models.CharField(max_length=20)
    service_category_id = models.BigIntegerField()
    service_id = models.BigIntegerField()
    service_name = models.CharField(max_length=100)
    count = models.IntegerField()
    type = models.CharField(max_length=125, blank=True, null=True)
    type_two = models.CharField(max_length=125, blank=True, null=True)
    type_three = models.CharField(max_length=125, blank=True, null=True)
    type_four = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    type_five = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    billing_cycle = models.IntegerField()
    billing_time = models.DateField()
    billing_status = models.IntegerField()
    status = models.IntegerField()
    max_auth_num = models.IntegerField()
    available_auth_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_user_subscription'


class TUserSubscriptionChangeLog(models.Model):
    user_subscription_change_log_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    order_code = models.CharField(max_length=20)
    change_time = models.DateTimeField()
    moment_number = models.IntegerField(blank=True, null=True)
    moment_content = models.CharField(max_length=500, blank=True, null=True)
    comments_content = models.CharField(max_length=2000, blank=True, null=True)
    user_ip = models.CharField(max_length=25, blank=True, null=True)
    order_type = models.IntegerField(blank=True, null=True)
    cycle_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_subscription_change_log'


class TUserTemp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', unique=True, max_length=128)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='PHONE_NUMBER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='COMPANY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    is_actived = models.IntegerField(db_column='IS_ACTIVED', blank=True, null=True)  # Field name made lowercase.
    register_time = models.CharField(db_column='REGISTER_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    time_zone = models.IntegerField(db_column='TIME_ZONE', blank=True, null=True)  # Field name made lowercase.
    active_code = models.CharField(db_column='ACTIVE_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    last_login_time = models.CharField(db_column='LAST_LOGIN_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    expiry_time = models.CharField(db_column='EXPIRY_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    activation_time = models.CharField(db_column='ACTIVATION_TIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pid = models.IntegerField(db_column='PID', blank=True, null=True)  # Field name made lowercase.
    auto_mail_flag = models.IntegerField(db_column='AUTO_MAIL_FLAG', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE')  # Field name made lowercase.
    source = models.IntegerField(db_column='SOURCE', blank=True, null=True)  # Field name made lowercase.
    pid_old = models.IntegerField(db_column='PID_OLD', blank=True, null=True)  # Field name made lowercase.
    reg_state = models.IntegerField(blank=True, null=True)
    reg_country = models.CharField(max_length=20, blank=True, null=True)
    agents_id = models.IntegerField()
    is_invite = models.IntegerField(blank=True, null=True)
    invite_count = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_temp'


class TUserWebinarService(models.Model):
    user_webinar_service_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True)
    free_meeting_time = models.IntegerField(blank=True, null=True)
    used_free_meeting_time = models.IntegerField(blank=True, null=True)
    free_meeting_point = models.IntegerField(blank=True, null=True)
    free_meeting_presenter = models.IntegerField(blank=True, null=True)
    is_buy = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_webinar_service'


class TUserWebinarServiceOrder(models.Model):
    order_code = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    extservice_id = models.IntegerField(blank=True, null=True)
    ext_tariffpkg_id = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    coupon_code = models.CharField(max_length=30, blank=True, null=True)
    amout = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    order_type = models.CharField(max_length=3, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    cycle_amout = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_webinar_service_order'


class TUserinfo(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', unique=True, max_length=128)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=42)  # Field name made lowercase.
    depid = models.IntegerField(db_column='DepID')  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=64, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=128, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=128, blank=True, null=True)  # Field name made lowercase.
    userlevel = models.CharField(db_column='UserLevel', max_length=1)  # Field name made lowercase.
    adminrole = models.CharField(db_column='AdminRole', max_length=1)  # Field name made lowercase.
    pwdquestion = models.CharField(db_column='PwdQuestion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pwdanswer = models.CharField(db_column='PwdAnswer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discbalance = models.FloatField(db_column='DiscBalance', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    logins = models.IntegerField(db_column='Logins', blank=True, null=True)  # Field name made lowercase.
    pwderrorlogins = models.IntegerField(db_column='PwdErrorLogins', blank=True, null=True)  # Field name made lowercase.
    pwderrordate = models.DateTimeField(db_column='PwdErrorDate', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    lastlogindate = models.DateTimeField(db_column='LastLoginDate', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version')  # Field name made lowercase.
    flag = models.CharField(max_length=1, blank=True, null=True)
    qq = models.CharField(db_column='QQ', max_length=25, blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=20, blank=True, null=True)
    type = models.IntegerField(db_column='TYPE')  # Field name made lowercase.
    source = models.IntegerField(db_column='SOURCE', blank=True, null=True)  # Field name made lowercase.
    time_zone_code = models.CharField(max_length=20, blank=True, null=True)
    pid_old = models.IntegerField(blank=True, null=True)
    reg_country = models.CharField(max_length=20, blank=True, null=True)
    agents_id = models.IntegerField()
    is_invite = models.IntegerField(blank=True, null=True)
    file_url = models.CharField(max_length=500, blank=True, null=True)
    small_file_url = models.CharField(max_length=500, blank=True, null=True)
    medium_file_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_userinfo'


class TUserlog(models.Model):
    userlogid = models.AutoField(db_column='UserLogID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    userip = models.CharField(db_column='UserIP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    operation = models.CharField(db_column='Operation', max_length=255)  # Field name made lowercase.
    objectname = models.CharField(db_column='ObjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    operationdesc = models.CharField(db_column='OperationDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    result = models.IntegerField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    errorinfo = models.CharField(db_column='ErrorInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    logtime = models.DateTimeField(db_column='LogTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_userlog'


class TUsers(models.Model):
    primary_user_id = models.BigIntegerField(primary_key=True)
    child_user_id = models.BigIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_users'
        unique_together = (('primary_user_id', 'child_user_id'),)


class TValuecard(models.Model):
    valuecardid = models.AutoField(db_column='ValueCardID', primary_key=True)  # Field name made lowercase.
    cardno = models.CharField(db_column='CardNO', max_length=12)  # Field name made lowercase.
    cardpwd = models.CharField(db_column='CardPwd', max_length=8)  # Field name made lowercase.
    conditionvalue = models.FloatField(db_column='ConditionValue', blank=True, null=True)  # Field name made lowercase.
    promotionsvalue = models.FloatField(db_column='PromotionsValue')  # Field name made lowercase.
    proservicesid = models.IntegerField(db_column='ProServicesID')  # Field name made lowercase.
    begindate = models.DateTimeField(db_column='BeginDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    businessid = models.IntegerField(db_column='BusinessID', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_valuecard'
        unique_together = (('valuecardid', 'cardno'),)


class TVideosize(models.Model):
    videsizename = models.CharField(db_column='videSizeName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    videowidth = models.IntegerField(db_column='VideoWidth')  # Field name made lowercase.
    videoheight = models.IntegerField(db_column='VideoHeight')  # Field name made lowercase.
    types = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_videosize'
        unique_together = (('id', 'types'),)


class TVotingOptions(models.Model):
    voting_topic_id = models.BigIntegerField(primary_key=True)
    option_num = models.IntegerField()
    option_content = models.CharField(max_length=500)
    voting_user_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_voting_options'
        unique_together = (('voting_topic_id', 'option_num'),)


class TVotingResult(models.Model):
    voting_result_id = models.BigAutoField(primary_key=True)
    voting_topic_id = models.BigIntegerField()
    option_num = models.IntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    login_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_voting_result'


class TVotingTopic(models.Model):
    voting_topic_id = models.BigAutoField(primary_key=True)
    voting_topic_name = models.CharField(max_length=1000, blank=True, null=True)
    room_id = models.BigIntegerField()
    create_user_id = models.BigIntegerField()
    create_email = models.CharField(max_length=128, blank=True, null=True)
    create_username = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)
    option_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_voting_topic'


class TWebinarsAuth(models.Model):
    primary_user_id = models.BigIntegerField(primary_key=True)
    child_user_id = models.BigIntegerField()
    subscription_id = models.BigIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_webinars_auth'
        unique_together = (('primary_user_id', 'child_user_id', 'subscription_id'),)


class TWwwDepartment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pid = models.IntegerField(db_column='PID', blank=True, null=True)  # Field name made lowercase.
    add_department = models.CharField(db_column='ADD_DEPARTMENT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    add_description = models.TextField(db_column='ADD_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_www_department'


class TWwwOrder(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    refno = models.IntegerField(db_column='REFNO', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    order_type = models.IntegerField(db_column='ORDER_TYPE', blank=True, null=True)  # Field name made lowercase.
    order_status = models.CharField(db_column='ORDER_STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pay_account = models.CharField(db_column='PAY_ACCOUNT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='CURRENCY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bussiness_acount = models.CharField(db_column='BUSSINESS_ACOUNT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pay_type = models.CharField(db_column='PAY_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bill_name = models.CharField(db_column='BILL_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bill_address = models.CharField(db_column='BILL_ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZIPCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    payment_date = models.DateTimeField(db_column='PAYMENT_DATE', blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    due_to_pay_date = models.DateTimeField(db_column='DUE_TO_PAY_DATE', blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='DISCOUNT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    product_munber = models.IntegerField(db_column='PRODUCT_MUNBER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_www_order'


class Testt(models.Model):
    test = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testt'
