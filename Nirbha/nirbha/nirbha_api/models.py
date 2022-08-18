# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DeviceVersion(models.Model):
    imei = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    port = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'device_version'


class Deviceconfig(models.Model):
    imei = models.TextField(blank=True, null=True)
    eventcode = models.IntegerField(blank=True, null=True)
    eventname = models.TextField(blank=True, null=True)
    parameter = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    iswrite = models.IntegerField(blank=True, null=True)
    response_type = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    tcp_port = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'deviceconfig'


class IoclActivitylog(models.Model):
    activity = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    actionid = models.IntegerField(blank=True, null=True)
    device = models.TextField()
    deviceid = models.IntegerField(blank=True, null=True)
    ipaddress = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_activitylog'


class IoclAlertMonitor(models.Model):
    imeino = models.TextField(blank=True, null=True)
    alert_type = models.IntegerField(blank=True, null=True)
    in_out_flag = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    trackdatetime = models.DateTimeField(blank=True, null=True)
    alertsendflag = models.IntegerField(blank=True, null=True)
    currentdatetime = models.DateTimeField(blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    tripid = models.IntegerField()
    vehicleid = models.IntegerField(blank=True, null=True)
    nightdriveduration = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_alert_monitor'


class IoclAlertMonitorOld(models.Model):
    alertmoniter_id = models.IntegerField(blank=True, null=True)
    imeino = models.TextField(blank=True, null=True)
    alert_type = models.IntegerField(blank=True, null=True)
    in_out_flag = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    trackdatetime = models.DateTimeField(blank=True, null=True)
    alertsendflag = models.IntegerField(blank=True, null=True)
    currentdatetime = models.DateTimeField(blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    tripid = models.IntegerField(blank=True, null=True)
    vehicleid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_alert_monitor_old'


class IoclAlertMonitorOld2(models.Model):
    alertmoniter_id = models.IntegerField(blank=True, null=True)
    imeino = models.TextField(blank=True, null=True)
    alert_type = models.IntegerField(blank=True, null=True)
    in_out_flag = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    trackdatetime = models.DateTimeField(blank=True, null=True)
    alertsendflag = models.IntegerField(blank=True, null=True)
    currentdatetime = models.DateTimeField(blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    tripid = models.IntegerField(blank=True, null=True)
    vehicleid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_alert_monitor_old2'


class IoclAlertSendReport(models.Model):
    alert_monitor_id = models.IntegerField()
    tripid = models.IntegerField()
    vehicleid = models.IntegerField()
    mobilenumber = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    alert_send_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'iocl_alert_send_report'


class IoclAlertSettings(models.Model):
    alert_type_id = models.IntegerField()
    action_type = models.IntegerField()
    access_roles = models.TextField()
    created_date = models.DateTimeField()
    created_by = models.IntegerField()
    modified_date = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    isdeleted = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_alert_settings'


class IoclAlertdetails(models.Model):
    vehicleid = models.IntegerField(blank=True, null=True)
    transportername = models.TextField(blank=True, null=True)
    companyid = models.IntegerField(blank=True, null=True)
    track_date = models.TextField(blank=True, null=True)
    ovscount = models.IntegerField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    nightdriveduration = models.TextField(blank=True, null=True)
    nightdrivecount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_alertdetails'


class IoclApproveMaster(models.Model):
    rtdid = models.IntegerField(blank=True, null=True)
    plant_manager_id = models.IntegerField(blank=True, null=True)
    plant_manager_date = models.DateTimeField(blank=True, null=True)
    plant_manager_process_id = models.IntegerField(blank=True, null=True)
    state_level_sales_id = models.IntegerField(blank=True, null=True)
    state_level_sales_date = models.DateTimeField(blank=True, null=True)
    state_level_sales_process_id = models.IntegerField(blank=True, null=True)
    state_level_ops_id = models.IntegerField(blank=True, null=True)
    state_level_ops_date = models.DateTimeField(blank=True, null=True)
    state_level_ops_process_id = models.IntegerField(blank=True, null=True)
    state_level_fin_id = models.IntegerField(blank=True, null=True)
    state_level_fin_date = models.DateTimeField(blank=True, null=True)
    state_level_fin_process_id = models.IntegerField(blank=True, null=True)
    state_level_lpg_head_id = models.IntegerField(blank=True, null=True)
    state_level_lpg_head_date = models.DateTimeField(blank=True, null=True)
    state_level_lpg_head_process_id = models.IntegerField(blank=True, null=True)
    plant_manager_select_route_reason = models.TextField(blank=True, null=True)
    plant_manager_route_change_reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_approve_master'


class IoclApproved(models.Model):
    rtdid = models.IntegerField()
    field_officer_id = models.IntegerField(blank=True, null=True)
    field_officer_date = models.DateTimeField(blank=True, null=True)
    field_officer_is_approved = models.IntegerField(blank=True, null=True)
    state_level_sales_id = models.IntegerField(blank=True, null=True)
    state_level_sales_date = models.DateTimeField(blank=True, null=True)
    state_level_sales_is_approved = models.IntegerField(blank=True, null=True)
    state_level_lpg_head_id = models.IntegerField(blank=True, null=True)
    state_level_lpg_head_date = models.DateTimeField(blank=True, null=True)
    state_level_lpg_head_is_approved = models.IntegerField(blank=True, null=True)
    state_level_fin_id = models.IntegerField(blank=True, null=True)
    state_level_fin_date = models.DateTimeField(blank=True, null=True)
    state_level_fin_is_approved = models.IntegerField(blank=True, null=True)
    state_level_ops_id = models.IntegerField(blank=True, null=True)
    state_level_ops_date = models.DateTimeField(blank=True, null=True)
    state_level_ops_is_approved = models.IntegerField(blank=True, null=True)
    field_officer_remark = models.TextField(blank=True, null=True)
    state_level_sales_remark = models.TextField(blank=True, null=True)
    state_level_ops_remark = models.TextField(blank=True, null=True)
    state_level_fin_remark = models.TextField(blank=True, null=True)
    state_level_lpg_head_remark = models.TextField(blank=True, null=True)
    field_officer_select_route_reason = models.TextField(blank=True, null=True)
    field_office_route_change_reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_approved'


class IoclCheckdata(models.Model):
    datetime = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    vech_imei = models.CharField(max_length=15, blank=True, null=True)
    latitude = models.CharField(max_length=40, blank=True, null=True)
    longitude = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_checkdata'


class IoclCity(models.Model):
    stateid = models.IntegerField(blank=True, null=True)
    cityname = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createdate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_city'


class IoclCompany(models.Model):
    uniquecode = models.TextField()
    companyname = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    stateid = models.IntegerField()
    cityid = models.IntegerField()
    pincode = models.TextField(blank=True, null=True)
    phoneno = models.TextField(blank=True, null=True)
    mobileno = models.TextField(blank=True, null=True)
    personname = models.TextField(blank=True, null=True)
    person_mobileno = models.TextField(blank=True, null=True)
    person_email = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    isdistributor = models.IntegerField()
    groupid = models.IntegerField()
    drc_code = models.TextField(blank=True, null=True)
    loadinglocation = models.TextField()
    unloadinglocation = models.TextField()
    isloadinglocation = models.IntegerField()
    isprivateplant = models.IntegerField()
    associatedplant = models.TextField()
    engineer_email = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_company'


class IoclConstants(models.Model):
    speed_vehicle_hr = models.IntegerField()
    idle_vehicle_hr = models.IntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_constants'


class IoclDealerMaster(models.Model):
    name = models.TextField(blank=True, null=True)
    contact_person = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    alt_number = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    uniquecode = models.UUIDField()
    vltmanufacturerid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_dealer_master'


class IoclDevice(models.Model):
    uniquecode = models.TextField()
    deviceimeino = models.TextField()
    simcardproviderid = models.IntegerField()
    simno = models.TextField(blank=True, null=True)
    devicedetails = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    deviceidno = models.TextField()

    class Meta:
        managed = True
        db_table = 'iocl_device'


class IoclDeviceSetzone(models.Model):
    uniquecode = models.TextField()
    imei = models.TextField(blank=True, null=True)
    zoneid = models.IntegerField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    radius = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_device_setzone'


class IoclDeviceaudiolog(models.Model):
    imei = models.TextField(blank=True, null=True)
    zoneid = models.IntegerField(blank=True, null=True)
    latitude = models.TextField()
    longitude = models.TextField()
    rawdata = models.TextField(blank=True, null=True)
    audioplayedtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_deviceaudiolog'


class IoclDevicechangeLogs(models.Model):
    vehicleid = models.IntegerField()
    old_imeino = models.TextField()
    new_imeino = models.TextField()
    changereason = models.TextField()
    devicechange_date = models.DateTimeField()
    devicechange_by = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_devicechange_logs'


class IoclDistanceMovementReport(models.Model):
    uniquecode = models.TextField(blank=True, null=True)
    vehicleid = models.IntegerField()
    track_date = models.DateTimeField()
    distance = models.FloatField()
    travel_period = models.TextField()
    stoppage_period = models.TextField()
    average = models.FloatField()
    max_speed = models.FloatField()
    exceptions = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    isdeleted = models.IntegerField()
    transporterid = models.IntegerField()
    tripid = models.IntegerField()
    vehicleno = models.CharField(max_length=30, blank=True, null=True)
    actual_distance = models.FloatField()

    class Meta:
        managed = True
        db_table = 'iocl_distance_movement_report'


class IoclDriver(models.Model):
    uniquecode = models.TextField()
    companyid = models.IntegerField()
    drivername = models.TextField()
    mobileno = models.TextField(blank=True, null=True)
    licenceno = models.TextField(blank=True, null=True)
    licencetype = models.TextField(blank=True, null=True)
    licenceexpirydate = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_driver'


class IoclGeofencingzone(models.Model):
    uniquecode = models.TextField()
    geofencingzone = models.TextField(blank=True, null=True)
    routeid = models.IntegerField()
    bounds = models.TextField(blank=True, null=True)
    zonetypeid = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_geofencingzone'


class IoclGroup(models.Model):
    groupid = models.AutoField(primary_key=True)
    group_name = models.TextField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    isdeleted = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_group'


class IoclLastTrackingLog(models.Model):
    uniquecode = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    vehicleid = models.IntegerField()
    tripid = models.IntegerField()
    trackdatetime = models.DateTimeField()
    speed = models.FloatField(blank=True, null=True)
    locationid = models.IntegerField()
    isonac = models.IntegerField()
    isonignition = models.IntegerField()
    mainpower = models.IntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    istemperatingmachine = models.IntegerField()
    statusindicator = models.CharField(max_length=50, blank=True, null=True)
    odometer = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    internalbattery = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_last_tracking_log'


class IoclLastTrip(models.Model):
    uniquecode = models.TextField()
    tripname = models.TextField(blank=True, null=True)
    routeid = models.IntegerField()
    vehicleid = models.IntegerField()
    driverid = models.IntegerField()
    expectedleavedatetime = models.DateTimeField(blank=True, null=True)
    leavedatetime = models.DateTimeField(blank=True, null=True)
    reachdatetime = models.DateTimeField(blank=True, null=True)
    totaltakendistance = models.FloatField()
    totaltakentime = models.TextField()
    createddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    ordernumber = models.TextField()
    nocommstatus = models.IntegerField(blank=True, null=True)
    poweroffstatus = models.IntegerField(blank=True, null=True)
    reachtimefound = models.IntegerField(blank=True, null=True)
    tripinfo_id = models.IntegerField(blank=True, null=True)
    tripstatus = models.TextField(blank=True, null=True)
    fromplantid = models.IntegerField(blank=True, null=True)
    toplantid = models.IntegerField(blank=True, null=True)
    leavetimefound = models.IntegerField(blank=True, null=True)
    tripdeviation = models.TextField(blank=True, null=True)
    routedeviation = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_last_trip'


class IoclLocation(models.Model):
    locationname = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    key = models.BigIntegerField(blank=True, null=True)
    deviceid = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_location'


class IoclLocationUnknown(models.Model):
    locationname = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    key = models.BigIntegerField(blank=True, null=True)
    deviceid = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_location_unknown'


class IoclMaillog(models.Model):
    mailsubject = models.TextField(blank=True, null=True)
    mailto = models.TextField(blank=True, null=True)
    mailcc = models.TextField(blank=True, null=True)
    mailbcc = models.TextField(blank=True, null=True)
    mailattachment = models.TextField(blank=True, null=True)
    mailstatus = models.IntegerField()
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_maillog'


class IoclMailsend(models.Model):
    imei = models.TextField(blank=True, null=True)
    mail_sendtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_mailsend'


class IoclPlantzone(models.Model):
    zonename = models.TextField(blank=True, null=True)
    zone_radious = models.FloatField(blank=True, null=True)
    vehicle_capacity = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField()
    createdate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    plantid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_plantzone'


class IoclReportTable(models.Model):
    tiripid = models.IntegerField()
    vehicleid = models.IntegerField()
    driverid = models.IntegerField()
    trackdatetime = models.DateTimeField()
    latitude = models.TextField()
    longitude = models.TextField()
    ispanicswitch = models.IntegerField(blank=True, null=True)
    speed = models.FloatField()
    stoppagealert = models.IntegerField()
    isonignition = models.IntegerField()
    fueltank = models.FloatField()
    mainpower = models.IntegerField(blank=True, null=True)
    waypointid = models.IntegerField(blank=True, null=True)
    odometer = models.CharField(max_length=20, blank=True, null=True)
    statusindicator = models.CharField(max_length=5, blank=True, null=True)
    latdirection = models.CharField(max_length=1, blank=True, null=True)
    longdirection = models.CharField(max_length=1, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    harshaccelation = models.IntegerField(blank=True, null=True)
    harshbreak = models.IntegerField(blank=True, null=True)
    harshmaneuvering = models.IntegerField(blank=True, null=True)
    heading = models.FloatField(blank=True, null=True)
    gsmsignalstregth = models.FloatField(blank=True, null=True)
    lowinternalbattery = models.CharField(max_length=30, blank=True, null=True)
    externalbatteryvoltage = models.FloatField(blank=True, null=True)
    internalbatteryvoltage = models.FloatField(blank=True, null=True)
    locationid = models.IntegerField(blank=True, null=True)
    placeid = models.IntegerField(blank=True, null=True)
    zoneid = models.IntegerField(blank=True, null=True)
    isinaccidentzone = models.IntegerField(blank=True, null=True)
    istemperatingmachine = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    overspeed = models.IntegerField()
    geofencingzoneids = models.TextField(blank=True, null=True)
    reserved = models.IntegerField(blank=True, null=True)
    nightdrive = models.IntegerField(blank=True, null=True)
    continuesdriving = models.IntegerField(blank=True, null=True)
    devicedetail = models.CharField(max_length=20, blank=True, null=True)
    rawdata = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_report_table'


class IoclRole(models.Model):
    uniquecode = models.TextField()
    rolename = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_role'


class IoclRolemapping(models.Model):
    roleid = models.IntegerField()
    module = models.TextField(blank=True, null=True)
    permission = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_rolemapping'


class IoclRoute(models.Model):
    uniquecode = models.TextField()
    routename = models.TextField()
    routeno = models.TextField(blank=True, null=True)
    senderwaypointid = models.IntegerField()
    receiverwaypointid = models.IntegerField()
    senderremarks = models.TextField(blank=True, null=True)
    receiverremarks = models.TextField(blank=True, null=True)
    speedlimit = models.IntegerField(blank=True, null=True)
    totaldistance = models.IntegerField(blank=True, null=True)
    pointslist = models.TextField(blank=True, null=True)
    geofencing = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    distance = models.FloatField(blank=True, null=True)
    companyid = models.IntegerField()
    mapimage = models.TextField(blank=True, null=True)
    physicaldistance = models.FloatField(blank=True, null=True)
    senderplantid = models.IntegerField()
    receiverplantid = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_route'


class IoclRouteWaypoint(models.Model):
    uniquecode = models.TextField()
    routeid = models.IntegerField()
    waypointid = models.IntegerField()
    sequence = models.IntegerField()
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    distance = models.FloatField(blank=True, null=True)
    isstartend = models.IntegerField()
    physicaldistance = models.FloatField(blank=True, null=True)
    isplant = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_route_waypoint'


class IoclRtd(models.Model):
    uniquecode = models.TextField()
    name_address = models.TextField(blank=True, null=True)
    drc_code = models.TextField(blank=True, null=True)
    old_total_rtd = models.FloatField()
    old_verification_date = models.DateField(blank=True, null=True)
    old_truck_charge = models.IntegerField()
    old_multi_axle_charge = models.IntegerField()
    new_plain_in_km = models.FloatField()
    new_hill_in_km = models.FloatField()
    new_high_hill_in_km = models.FloatField()
    new_total_rtd = models.FloatField()
    new_verification_date = models.DateField(blank=True, null=True)
    new_truck_charge = models.IntegerField()
    new_multi_axle_charge = models.IntegerField()
    reason_for_new_rtd = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    routeid = models.IntegerField()
    effective_date = models.DateField(blank=True, null=True)
    isverified = models.IntegerField(blank=True, null=True)
    verifiedby = models.IntegerField(blank=True, null=True)
    verifieddate = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    rtdcode = models.TextField(blank=True, null=True)
    rtdfrom = models.TextField(blank=True, null=True)
    rtdto = models.TextField(blank=True, null=True)
    rtdrequestid = models.IntegerField()
    approv_status = models.IntegerField(blank=True, null=True)
    pdffilename = models.TextField(blank=True, null=True)
    sap_uploaded_date = models.DateTimeField(blank=True, null=True)
    reference_no = models.TextField(blank=True, null=True)
    locationcode = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    fromplantid = models.IntegerField(blank=True, null=True)
    toplantid = models.IntegerField(blank=True, null=True)
    iscompleted = models.IntegerField()
    senderplantid = models.IntegerField()
    receiverplantid = models.IntegerField()
    ishold = models.IntegerField()
    reverserouteid = models.IntegerField(blank=True, null=True)
    reply_by_admin = models.TextField(blank=True, null=True)
    routetotaltime = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_rtd'


class IoclRtdProcess(models.Model):
    rtdid = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    is_approved = models.IntegerField(blank=True, null=True)
    action_date = models.DateTimeField(blank=True, null=True)
    select_route_reason = models.TextField(blank=True, null=True)
    route_change_reason = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    isdeleted = models.IntegerField()
    isreapprove = models.IntegerField()
    reply_by_admin = models.TextField(blank=True, null=True)
    reply_admin_pending = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_rtd_process'


class IoclRtdTollplaza(models.Model):
    rtdid = models.IntegerField(blank=True, null=True)
    tollplazaid = models.IntegerField(blank=True, null=True)
    double_exel_oneway = models.FloatField(blank=True, null=True)
    double_exel_twoway = models.FloatField(blank=True, null=True)
    multi_axle_oneway = models.FloatField(blank=True, null=True)
    multi_axle_twoway = models.FloatField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    roadtype = models.TextField(blank=True, null=True)
    kmcover = models.FloatField(blank=True, null=True)
    fromplace = models.TextField(blank=True, null=True)
    toplace = models.TextField(blank=True, null=True)
    sequence = models.IntegerField()
    rate_revisiondoc = models.TextField(blank=True, null=True)
    route_id = models.IntegerField(blank=True, null=True)
    reverse_routeid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_rtd_tollplaza'


class IoclRtdconnect(models.Model):
    r1_rtdid = models.IntegerField(blank=True, null=True)
    rtdid = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_rtdconnect'


class IoclRtddoc(models.Model):
    uniquecode = models.TextField()
    rtdid = models.IntegerField()
    filename = models.TextField(blank=True, null=True)
    filetype = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_rtddoc'


class IoclRtdrequest(models.Model):
    uniquecode = models.TextField()
    fromwaypointid = models.IntegerField(blank=True, null=True)
    towaypointid = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    rtdstatus = models.IntegerField()
    rtdclosedby = models.IntegerField(blank=True, null=True)
    rtdcloseeddate = models.DateTimeField(blank=True, null=True)
    fromplantid = models.IntegerField()
    toplantid = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_rtdrequest'


class IoclRtdtime(models.Model):
    rtdtimeid = models.BigIntegerField(blank=True, null=True)
    uniquecode = models.TextField()
    isdeleted = models.IntegerField()
    routeid = models.IntegerField()
    routetotaltime = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_rtdtime'


class IoclSimcardProvider(models.Model):
    uniquecode = models.TextField()
    simcardprovider = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_simcard_provider'


class IoclSpeedmonitorReport(models.Model):
    uniquecode = models.TextField()
    vehicleid = models.IntegerField()
    track_date = models.DateTimeField()
    max_speed = models.FloatField(blank=True, null=True)
    average_speed = models.FloatField(blank=True, null=True)
    total_exceed_speed = models.FloatField()
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    isdeleted = models.IntegerField()
    transporterid = models.IntegerField()
    tripid = models.IntegerField()
    vehicleno = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_speedmonitor_report'


class IoclState(models.Model):
    statename = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_state'


class IoclStoppageReport(models.Model):
    uniquecode = models.TextField()
    vehicleid = models.IntegerField()
    track_date = models.DateTimeField()
    max_stoppage = models.TextField()
    min_stoppage = models.TextField()
    average_stoppage = models.TextField()
    stop_period = models.TextField()
    stoppage_details = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    isdeleted = models.IntegerField()
    transporterid = models.IntegerField()
    tripid = models.IntegerField()
    vehicleno = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_stoppage_report'


class IoclTollPlaza(models.Model):
    uniquecode = models.TextField()
    rtdid = models.IntegerField(blank=True, null=True)
    tollplazaname = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    notification_file = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    referencelink = models.TextField(blank=True, null=True)
    rate_revision = models.TextField(blank=True, null=True)
    tollplazadetails = models.TextField(blank=True, null=True)
    roadtype = models.TextField(blank=True, null=True)
    kmcover = models.FloatField(blank=True, null=True)
    fromplace = models.TextField(blank=True, null=True)
    toplace = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_toll_plaza'


class IoclTollplaza2(models.Model):
    rtdid = models.IntegerField(blank=True, null=True)
    tollplaza = models.TextField(blank=True, null=True)
    double_exel_oneway = models.FloatField(blank=True, null=True)
    double_exel_twoway = models.FloatField(blank=True, null=True)
    multi_axle_oneway = models.FloatField(blank=True, null=True)
    multi_axle_twoway = models.FloatField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_tollplaza'


class IoclTrackinglog(models.Model):
    tiripid = models.IntegerField()
    vehicleid = models.IntegerField()
    driverid = models.IntegerField()
    trackdatetime = models.DateTimeField()
    latitude = models.TextField()
    longitude = models.TextField()
    ispanicswitch = models.IntegerField(blank=True, null=True)
    speed = models.FloatField()
    stoppagealert = models.IntegerField()
    isonignition = models.IntegerField()
    fueltank = models.FloatField()
    mainpower = models.IntegerField(blank=True, null=True)
    waypointid = models.IntegerField(blank=True, null=True)
    odometer = models.CharField(max_length=20, blank=True, null=True)
    statusindicator = models.CharField(max_length=5, blank=True, null=True)
    latdirection = models.CharField(max_length=1, blank=True, null=True)
    longdirection = models.CharField(max_length=1, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    harshaccelation = models.IntegerField(blank=True, null=True)
    harshbreak = models.IntegerField(blank=True, null=True)
    harshmaneuvering = models.IntegerField(blank=True, null=True)
    heading = models.FloatField(blank=True, null=True)
    gsmsignalstregth = models.FloatField(blank=True, null=True)
    lowinternalbattery = models.CharField(max_length=30, blank=True, null=True)
    externalbatteryvoltage = models.FloatField(blank=True, null=True)
    internalbatteryvoltage = models.FloatField(blank=True, null=True)
    locationid = models.IntegerField(blank=True, null=True)
    placeid = models.IntegerField(blank=True, null=True)
    zoneid = models.IntegerField(blank=True, null=True)
    isinaccidentzone = models.IntegerField(blank=True, null=True)
    istemperatingmachine = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    overspeed = models.IntegerField()
    geofencingzoneids = models.TextField(blank=True, null=True)
    reserved = models.IntegerField(blank=True, null=True)
    nightdrive = models.IntegerField(blank=True, null=True)
    continuesdriving = models.IntegerField(blank=True, null=True)
    devicedetail = models.CharField(max_length=20, blank=True, null=True)
    rawdata = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_trackinglog'


class IoclTrackinglogDuplicate(models.Model):
    tiripid = models.IntegerField()
    vehicleid = models.IntegerField()
    driverid = models.IntegerField()
    trackdatetime = models.DateTimeField()
    latitude = models.TextField()
    longitude = models.TextField()
    ispanicswitch = models.IntegerField(blank=True, null=True)
    speed = models.FloatField()
    stoppagealert = models.IntegerField()
    isonignition = models.IntegerField()
    fueltank = models.FloatField()
    mainpower = models.IntegerField(blank=True, null=True)
    waypointid = models.IntegerField(blank=True, null=True)
    odometer = models.CharField(max_length=20, blank=True, null=True)
    statusindicator = models.CharField(max_length=5, blank=True, null=True)
    latdirection = models.CharField(max_length=1, blank=True, null=True)
    longdirection = models.CharField(max_length=1, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    harshaccelation = models.IntegerField(blank=True, null=True)
    harshbreak = models.IntegerField(blank=True, null=True)
    harshmaneuvering = models.IntegerField(blank=True, null=True)
    heading = models.FloatField(blank=True, null=True)
    gsmsignalstregth = models.FloatField(blank=True, null=True)
    lowinternalbattery = models.CharField(max_length=30, blank=True, null=True)
    externalbatteryvoltage = models.FloatField(blank=True, null=True)
    internalbatteryvoltage = models.FloatField(blank=True, null=True)
    locationid = models.IntegerField(blank=True, null=True)
    placeid = models.IntegerField(blank=True, null=True)
    zoneid = models.IntegerField(blank=True, null=True)
    isinaccidentzone = models.IntegerField(blank=True, null=True)
    istemperatingmachine = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    overspeed = models.IntegerField()
    geofencingzoneids = models.TextField(blank=True, null=True)
    reserved = models.IntegerField(blank=True, null=True)
    nightdrive = models.IntegerField(blank=True, null=True)
    continuesdriving = models.IntegerField(blank=True, null=True)
    devicedetail = models.CharField(max_length=20, blank=True, null=True)
    rawdata = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_trackinglog_duplicate'


class IoclTransporterMapping(models.Model):
    uniquecode = models.TextField()
    userid = models.IntegerField()
    connected_userid = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_transporter_mapping'


class IoclTransporterVehicleMapping(models.Model):
    uniquecode = models.TextField()
    transporterid = models.IntegerField(blank=True, null=True)
    vehicleid = models.IntegerField(blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_transporter_vehicle_mapping'


class IoclTravelhistoryReport(models.Model):
    uniquecode = models.TextField()
    vehicleid = models.IntegerField()
    track_date = models.DateTimeField(blank=True, null=True)
    traveldetails = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    isdeleted = models.IntegerField()
    transporterid = models.IntegerField()
    tripid = models.IntegerField()
    vehicleno = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'iocl_travelhistory_report'


class IoclTrip(models.Model):
    uniquecode = models.TextField()
    tripname = models.TextField(blank=True, null=True)
    routeid = models.IntegerField()
    vehicleid = models.IntegerField()
    driverid = models.IntegerField()
    expectedleavedatetime = models.DateTimeField(blank=True, null=True)
    expectedreachdatetime = models.DateTimeField(blank=True, null=True)
    leavedatetime = models.DateTimeField(blank=True, null=True)
    reachdatetime = models.DateTimeField(blank=True, null=True)
    routetype = models.TextField(blank=True, null=True)
    routestatus = models.TextField(blank=True, null=True)
    totaltakendistance = models.FloatField()
    totaltakentime = models.TextField()
    isreturntrip = models.IntegerField()
    returnrouteid = models.IntegerField(blank=True, null=True)
    returnexpectedleavedatetime = models.DateTimeField(blank=True, null=True)
    returnexpectedreachdatetime = models.DateTimeField(blank=True, null=True)
    returnleavedatetime = models.DateTimeField(blank=True, null=True)
    returnreachdatetime = models.DateTimeField(blank=True, null=True)
    iscancel = models.IntegerField()
    cancelreason = models.TextField(blank=True, null=True)
    canceledby = models.IntegerField(blank=True, null=True)
    canceleddate = models.DateTimeField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    ordernumber = models.TextField()
    vehicleinflag = models.IntegerField()
    nocommstatus = models.IntegerField(blank=True, null=True)
    poweroffstatus = models.IntegerField(blank=True, null=True)
    reachtimefound = models.IntegerField(blank=True, null=True)
    tripinfo_id = models.IntegerField(blank=True, null=True)
    tripstatus = models.TextField(blank=True, null=True)
    fromplantid = models.IntegerField(blank=True, null=True)
    toplantid = models.IntegerField(blank=True, null=True)
    leavetimefound = models.IntegerField(blank=True, null=True)
    tripdeviation = models.TextField(blank=True, null=True)
    routedeviation = models.TextField(blank=True, null=True)
    vehicleno = models.BigIntegerField(blank=True, null=True)
    vehicle = models.BinaryField(blank=True, null=True)
    sequence_no = models.IntegerField(blank=True, null=True)
    driver_name = models.TextField(blank=True, null=True)
    driver_mobileno = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_trip'


class IoclTripOld(models.Model):
    tripid = models.IntegerField()
    uniquecode = models.TextField()
    tripname = models.TextField(blank=True, null=True)
    routeid = models.IntegerField()
    vehicleid = models.IntegerField()
    driverid = models.IntegerField()
    expectedleavedatetime = models.DateTimeField(blank=True, null=True)
    expectedreachdatetime = models.DateTimeField(blank=True, null=True)
    leavedatetime = models.DateTimeField(blank=True, null=True)
    reachdatetime = models.DateTimeField(blank=True, null=True)
    routetype = models.TextField(blank=True, null=True)
    routestatus = models.TextField(blank=True, null=True)
    totaltakendistance = models.FloatField()
    totaltakentime = models.TextField()
    isreturntrip = models.IntegerField()
    returnrouteid = models.IntegerField(blank=True, null=True)
    returnexpectedleavedatetime = models.DateTimeField(blank=True, null=True)
    returnexpectedreachdatetime = models.DateTimeField(blank=True, null=True)
    returnleavedatetime = models.DateTimeField(blank=True, null=True)
    returnreachdatetime = models.DateTimeField(blank=True, null=True)
    iscancel = models.IntegerField()
    cancelreason = models.TextField(blank=True, null=True)
    canceledby = models.IntegerField(blank=True, null=True)
    canceleddate = models.DateTimeField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    ordernumber = models.TextField()
    vehicleinflag = models.IntegerField()
    nocommstatus = models.IntegerField(blank=True, null=True)
    poweroffstatus = models.IntegerField(blank=True, null=True)
    reachtimefound = models.IntegerField(blank=True, null=True)
    tripinfo_id = models.IntegerField(blank=True, null=True)
    tripstatus = models.TextField(blank=True, null=True)
    fromplantid = models.IntegerField(blank=True, null=True)
    toplantid = models.IntegerField(blank=True, null=True)
    leavetimefound = models.IntegerField(blank=True, null=True)
    tripdeviation = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_trip_old'


class IoclTripinfo(models.Model):
    distributorcode = models.TextField(blank=True, null=True)
    plantcode = models.TextField(blank=True, null=True)
    docno = models.TextField(blank=True, null=True)
    vehicleno = models.TextField(blank=True, null=True)
    documenttime = models.DateTimeField(blank=True, null=True)
    cancellation = models.TextField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    isprocess = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_tripinfo'


class IoclTriplog(models.Model):
    tripid = models.IntegerField(blank=True, null=True)
    tripstarttime = models.DateTimeField(blank=True, null=True)
    tripendtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_triplog'


class IoclUnregisterdata(models.Model):
    imei = models.TextField(blank=True, null=True)
    rawdata = models.TextField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_unregisterdata'


class IoclUserloginLog(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    device = models.TextField(blank=True, null=True)
    deviceid = models.IntegerField(blank=True, null=True)
    ipaddress = models.TextField(blank=True, null=True)
    startdatetime = models.DateTimeField(blank=True, null=True)
    enddatetime = models.DateTimeField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    os_flag = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_userlogin_log'


class IoclUsers(models.Model):
    uniquecode = models.TextField()
    roleid = models.IntegerField()
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    mobileno = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    usertype = models.TextField(blank=True, null=True)
    employeeno = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    stateid = models.IntegerField()
    companyid = models.IntegerField()
    transporterno = models.TextField(blank=True, null=True)
    isverify = models.IntegerField()
    groupid = models.IntegerField()
    repot_emailids = models.TextField(blank=True, null=True)
    is_auto_lpg_officer = models.IntegerField()
    parent_id = models.IntegerField()
    multi_companyid = models.TextField()
    sendemail = models.IntegerField(db_column='sendEmail', blank=True, null=True)  # Field name made lowercase.
    private_company_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_users'


class IoclVehicle(models.Model):
    uniquecode = models.TextField()
    transporterid = models.IntegerField(blank=True, null=True)
    companyid = models.TextField(blank=True, null=True)
    vehicleno = models.TextField(blank=True, null=True)
    engineid = models.TextField(blank=True, null=True)
    chassisid = models.TextField(blank=True, null=True)
    deviceid = models.IntegerField(blank=True, null=True)
    installationdate = models.DateField(blank=True, null=True)
    vehiclecolor = models.TextField(blank=True, null=True)
    vehicleimage = models.TextField(blank=True, null=True)
    tanklimit = models.FloatField(blank=True, null=True)
    vehiclecapacity = models.TextField(blank=True, null=True)
    vehiclestatus = models.TextField(blank=True, null=True)
    milege = models.FloatField(blank=True, null=True)
    startingmeter = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    inmaintenance = models.IntegerField()
    last_odometer = models.CharField(max_length=20, blank=True, null=True)
    new_device_odometer = models.IntegerField(blank=True, null=True)
    moreinfo = models.TextField(blank=True, null=True)
    cronjob = models.IntegerField()
    travelhistory_report = models.IntegerField()
    speedmonitor_report = models.IntegerField()
    distancemovement_report = models.IntegerField()
    stoppage_report = models.IntegerField()
    inaccident = models.IntegerField(blank=True, null=True)
    inpendinginstallation = models.IntegerField()
    owner_name = models.TextField(blank=True, null=True)
    imei_no = models.TextField(blank=True, null=True)
    rto_name = models.TextField(blank=True, null=True)
    vehiclecategoryid = models.BigIntegerField(blank=True, null=True)
    vehicletypeid = models.BigIntegerField(blank=True, null=True)
    owners_address = models.TextField(blank=True, null=True)
    owners_contact = models.TextField(blank=True, null=True)
    vltmanufacturerid = models.BigIntegerField(blank=True, null=True)
    vltmodelid = models.BigIntegerField(blank=True, null=True)
    installation_date = models.DateField(blank=True, null=True)
    simcardproviderid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_vehicle'


class IoclVehicle012021(models.Model):
    uniquecode = models.TextField()
    transporterid = models.IntegerField(blank=True, null=True)
    companyid = models.TextField(blank=True, null=True)
    vehicleno = models.TextField(blank=True, null=True)
    engineid = models.TextField(blank=True, null=True)
    chassisid = models.TextField(blank=True, null=True)
    deviceid = models.IntegerField(blank=True, null=True)
    installationdate = models.DateField(blank=True, null=True)
    vehiclecolor = models.TextField(blank=True, null=True)
    vehicleimage = models.TextField(blank=True, null=True)
    tanklimit = models.FloatField()
    vehiclecapacity = models.TextField(blank=True, null=True)
    vehiclestatus = models.TextField(blank=True, null=True)
    milege = models.FloatField()
    startingmeter = models.IntegerField()
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    inmaintenance = models.IntegerField()
    last_odometer = models.CharField(max_length=20, blank=True, null=True)
    new_device_odometer = models.IntegerField(blank=True, null=True)
    moreinfo = models.TextField(blank=True, null=True)
    cronjob = models.IntegerField()
    travelhistory_report = models.IntegerField()
    speedmonitor_report = models.IntegerField()
    distancemovement_report = models.IntegerField()
    stoppage_report = models.IntegerField()
    inaccident = models.IntegerField(blank=True, null=True)
    inpendinginstallation = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_vehicle_01_2021'


class IoclVehicle022021(models.Model):
    uniquecode = models.TextField()
    transporterid = models.IntegerField(blank=True, null=True)
    companyid = models.TextField(blank=True, null=True)
    vehicleno = models.TextField(blank=True, null=True)
    engineid = models.TextField(blank=True, null=True)
    chassisid = models.TextField(blank=True, null=True)
    deviceid = models.IntegerField(blank=True, null=True)
    installationdate = models.DateField(blank=True, null=True)
    vehiclecolor = models.TextField(blank=True, null=True)
    vehicleimage = models.TextField(blank=True, null=True)
    tanklimit = models.FloatField()
    vehiclecapacity = models.TextField(blank=True, null=True)
    vehiclestatus = models.TextField(blank=True, null=True)
    milege = models.FloatField()
    startingmeter = models.IntegerField()
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    inmaintenance = models.IntegerField()
    last_odometer = models.CharField(max_length=20, blank=True, null=True)
    new_device_odometer = models.IntegerField(blank=True, null=True)
    moreinfo = models.TextField(blank=True, null=True)
    cronjob = models.IntegerField()
    travelhistory_report = models.IntegerField()
    speedmonitor_report = models.IntegerField()
    distancemovement_report = models.IntegerField()
    stoppage_report = models.IntegerField()
    inaccident = models.IntegerField(blank=True, null=True)
    inpendinginstallation = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_vehicle_02_2021'


class IoclVehicle032021(models.Model):
    uniquecode = models.TextField()
    transporterid = models.IntegerField(blank=True, null=True)
    companyid = models.TextField(blank=True, null=True)
    vehicleno = models.TextField(blank=True, null=True)
    engineid = models.TextField(blank=True, null=True)
    chassisid = models.TextField(blank=True, null=True)
    deviceid = models.IntegerField(blank=True, null=True)
    installationdate = models.DateField(blank=True, null=True)
    vehiclecolor = models.TextField(blank=True, null=True)
    vehicleimage = models.TextField(blank=True, null=True)
    tanklimit = models.FloatField()
    vehiclecapacity = models.TextField(blank=True, null=True)
    vehiclestatus = models.TextField(blank=True, null=True)
    milege = models.FloatField()
    startingmeter = models.IntegerField()
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    inmaintenance = models.IntegerField()
    last_odometer = models.CharField(max_length=20, blank=True, null=True)
    new_device_odometer = models.IntegerField(blank=True, null=True)
    moreinfo = models.TextField(blank=True, null=True)
    cronjob = models.IntegerField()
    travelhistory_report = models.IntegerField()
    speedmonitor_report = models.IntegerField()
    distancemovement_report = models.IntegerField()
    stoppage_report = models.IntegerField()
    inaccident = models.IntegerField(blank=True, null=True)
    inpendinginstallation = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_vehicle_03_2021'


class IoclVehicle042020(models.Model):
    uniquecode = models.TextField()
    transporterid = models.IntegerField(blank=True, null=True)
    companyid = models.TextField(blank=True, null=True)
    vehicleno = models.TextField(blank=True, null=True)
    engineid = models.TextField(blank=True, null=True)
    chassisid = models.TextField(blank=True, null=True)
    deviceid = models.IntegerField(blank=True, null=True)
    installationdate = models.DateField(blank=True, null=True)
    vehiclecolor = models.TextField(blank=True, null=True)
    vehicleimage = models.TextField(blank=True, null=True)
    tanklimit = models.FloatField()
    vehiclecapacity = models.TextField(blank=True, null=True)
    vehiclestatus = models.TextField(blank=True, null=True)
    milege = models.FloatField()
    startingmeter = models.IntegerField()
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    inmaintenance = models.IntegerField()
    last_odometer = models.CharField(max_length=20, blank=True, null=True)
    new_device_odometer = models.IntegerField(blank=True, null=True)
    moreinfo = models.TextField(blank=True, null=True)
    cronjob = models.IntegerField()
    travelhistory_report = models.IntegerField()
    speedmonitor_report = models.IntegerField()
    distancemovement_report = models.IntegerField()
    stoppage_report = models.IntegerField()
    inaccident = models.IntegerField(blank=True, null=True)
    inpendinginstallation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_vehicle_04_2020'


class IoclVehicle042021(models.Model):
    vehicleid = models.IntegerField(blank=True, null=True)
    uniquecode = models.TextField()
    transporterid = models.IntegerField(blank=True, null=True)
    companyid = models.TextField(blank=True, null=True)
    vehicleno = models.TextField(blank=True, null=True)
    engineid = models.TextField(blank=True, null=True)
    chassisid = models.TextField(blank=True, null=True)
    deviceid = models.IntegerField(blank=True, null=True)
    installationdate = models.DateField(blank=True, null=True)
    vehiclecolor = models.TextField(blank=True, null=True)
    vehicleimage = models.TextField(blank=True, null=True)
    tanklimit = models.FloatField()
    vehiclecapacity = models.TextField(blank=True, null=True)
    vehiclestatus = models.TextField(blank=True, null=True)
    milege = models.FloatField()
    startingmeter = models.IntegerField()
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    inmaintenance = models.IntegerField()
    last_odometer = models.CharField(max_length=20, blank=True, null=True)
    new_device_odometer = models.IntegerField(blank=True, null=True)
    moreinfo = models.TextField(blank=True, null=True)
    cronjob = models.IntegerField()
    travelhistory_report = models.IntegerField()
    speedmonitor_report = models.IntegerField()
    distancemovement_report = models.IntegerField()
    stoppage_report = models.IntegerField()
    inaccident = models.IntegerField(blank=True, null=True)
    inpendinginstallation = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_vehicle_04_2021'


class IoclVehicleInsurance(models.Model):
    uniquecode = models.TextField()
    vehicleid = models.IntegerField()
    insurancecompanyname = models.TextField(blank=True, null=True)
    insurancestartdate = models.DateField(blank=True, null=True)
    insuranceenddate = models.DateField(blank=True, null=True)
    iscurrent = models.IntegerField()
    insurancepolicyno = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_vehicle_insurance'


class IoclVehicleOld(models.Model):
    uniquecode = models.TextField()
    transporterid = models.IntegerField(blank=True, null=True)
    companyid = models.TextField(blank=True, null=True)
    vehicleno = models.TextField(blank=True, null=True)
    engineid = models.TextField(blank=True, null=True)
    chassisid = models.TextField(blank=True, null=True)
    deviceid = models.IntegerField(blank=True, null=True)
    installationdate = models.DateField(blank=True, null=True)
    vehiclecolor = models.TextField(blank=True, null=True)
    vehicleimage = models.TextField(blank=True, null=True)
    tanklimit = models.FloatField()
    vehiclecapacity = models.TextField(blank=True, null=True)
    vehiclestatus = models.TextField(blank=True, null=True)
    milege = models.FloatField()
    startingmeter = models.IntegerField()
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    inmaintenance = models.IntegerField()
    last_odometer = models.CharField(max_length=20, blank=True, null=True)
    new_device_odometer = models.IntegerField(blank=True, null=True)
    moreinfo = models.TextField(blank=True, null=True)
    cronjob = models.IntegerField()
    travelhistory_report = models.IntegerField()
    speedmonitor_report = models.IntegerField()
    distancemovement_report = models.IntegerField()
    stoppage_report = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_vehicle_old'


class IoclVehiclePuc(models.Model):
    uniquecode = models.TextField()
    vehicleid = models.IntegerField()
    pucno = models.TextField(blank=True, null=True)
    pucstartdate = models.DateField(blank=True, null=True)
    pucenddate = models.DateField(blank=True, null=True)
    iscurrent = models.IntegerField()
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_vehicle_puc'


class IoclVehicleQueue(models.Model):
    uniquecode = models.TextField()
    vehicleid = models.ForeignKey(IoclVehicle, models.DO_NOTHING, db_column='vehicleid', blank=True, null=True)
    queueno = models.IntegerField(blank=True, null=True)
    zone_status = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    tripid = models.ForeignKey(IoclTrip, models.DO_NOTHING, db_column='tripid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_vehicle_queue'


class IoclVehicleTmp(models.Model):
    vehicleid = models.IntegerField(blank=True, null=True)
    uniquecode = models.TextField(blank=True, null=True)
    transporterid = models.IntegerField(blank=True, null=True)
    companyid = models.TextField(blank=True, null=True)
    vehicleno = models.TextField(blank=True, null=True)
    engineid = models.TextField(blank=True, null=True)
    chassisid = models.TextField(blank=True, null=True)
    deviceid = models.IntegerField(blank=True, null=True)
    installationdate = models.DateField(blank=True, null=True)
    vehiclecolor = models.TextField(blank=True, null=True)
    vehicleimage = models.TextField(blank=True, null=True)
    tanklimit = models.FloatField(blank=True, null=True)
    vehiclecapacity = models.TextField(blank=True, null=True)
    vehiclestatus = models.TextField(blank=True, null=True)
    milege = models.FloatField(blank=True, null=True)
    startingmeter = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    inmaintenance = models.IntegerField(blank=True, null=True)
    last_odometer = models.CharField(max_length=20, blank=True, null=True)
    new_device_odometer = models.IntegerField(blank=True, null=True)
    moreinfo = models.TextField(blank=True, null=True)
    cronjob = models.IntegerField(blank=True, null=True)
    travelhistory_report = models.IntegerField(blank=True, null=True)
    speedmonitor_report = models.IntegerField(blank=True, null=True)
    distancemovement_report = models.IntegerField(blank=True, null=True)
    stoppage_report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_vehicle_tmp'


class IoclVehiclecategoryMaster(models.Model):
    name = models.TextField(blank=True, null=True)
    uniquecode = models.UUIDField()
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_vehiclecategory_master'


class IoclVehicletypeMaster(models.Model):
    name = models.TextField(blank=True, null=True)
    uniquecode = models.UUIDField()
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_vehicletype_master'


class IoclVltmanufacturerMaster(models.Model):
    uniquecode = models.UUIDField()
    name = models.TextField(blank=True, null=True)
    manufacturer_code = models.TextField(blank=True, null=True)
    cin_no = models.TextField(blank=True, null=True)
    gst_no = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phoneno = models.TextField(blank=True, null=True)
    emailid = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    ais_140_approved = models.IntegerField()
    smart_mobility_member = models.IntegerField()
    username = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_vltmanufacturer_master'


class IoclVltmodelMaster(models.Model):
    uniquecode = models.UUIDField()
    name = models.TextField(blank=True, null=True)
    manufacturer_code_id = models.BigIntegerField()
    model_code = models.TextField(blank=True, null=True)
    production_date = models.DateField(blank=True, null=True)
    is_irnss = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_vltmodel_master'


class IoclWaypoint(models.Model):
    uniquecode = models.UUIDField()
    waypointname = models.TextField()
    address = models.TextField(blank=True, null=True)
    cityid = models.IntegerField(blank=True, null=True)
    latitude = models.TextField()
    longitude = models.TextField()
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()
    havegeofence = models.IntegerField()
    geofence = models.IntegerField()
    roadtype = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_waypoint'


class IoclZonemaster(models.Model):
    zonename = models.TextField(blank=True, null=True)
    latitude1 = models.TextField()
    longitude1 = models.TextField()
    latitude2 = models.TextField(blank=True, null=True)
    longitude2 = models.TextField(blank=True, null=True)
    latitude3 = models.TextField(blank=True, null=True)
    longitude3 = models.TextField(blank=True, null=True)
    latitude4 = models.TextField(blank=True, null=True)
    longitude4 = models.TextField(blank=True, null=True)
    latitude5 = models.TextField(blank=True, null=True)
    longitude5 = models.TextField(blank=True, null=True)
    latitude6 = models.TextField(blank=True, null=True)
    longitude6 = models.TextField(blank=True, null=True)
    latitude7 = models.TextField(blank=True, null=True)
    longitude7 = models.TextField(blank=True, null=True)
    latitude8 = models.TextField(blank=True, null=True)
    longitude8 = models.TextField(blank=True, null=True)
    latitude9 = models.TextField(blank=True, null=True)
    longitude9 = models.TextField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    radius = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iocl_zonemaster'


class IoclZonetype(models.Model):
    uniquecode = models.TextField()
    zonetype = models.TextField(blank=True, null=True)
    createdby = models.IntegerField()
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'iocl_zonetype'


class LoginMst(models.Model):
    username = models.TextField(blank=True, null=True)
    id_pk = models.AutoField(primary_key=True)
    imei = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'login_mst'


class Rawdata2(models.Model):
    data = models.TextField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    track_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    imei = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    event_code = models.IntegerField(blank=True, null=True)
    dashboard = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawdata2'


class Rawdata22(models.Model):
    data = models.TextField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    track_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    imei = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    event_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawdata2_2'


class RawdataB(models.Model):
    data = models.TextField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    track_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    imei = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    event_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawdata_b'


class RawdataB2(models.Model):
    data = models.TextField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    track_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    imei = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    event_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawdata_b2'


class RawdataFuturedate(models.Model):
    data = models.TextField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    track_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    imei = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    event_code = models.IntegerField(blank=True, null=True)
    dashboard = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawdata_futuredate'


class RawdataInvalid(models.Model):
    data = models.TextField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    track_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    imei = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    event_code = models.IntegerField(blank=True, null=True)
    dashboard = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawdata_invalid'


class RawdataItraold(models.Model):
    data = models.TextField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    track_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    imei = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    event_code = models.IntegerField(blank=True, null=True)
    dashboard = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawdata_itraold'


class ReportMst(models.Model):
    username = models.TextField(blank=True, null=True)
    loginid = models.TextField(blank=True, null=True)
    user_location = models.TextField(blank=True, null=True)
    veh_location = models.TextField(blank=True, null=True)
    veh_no = models.TextField(blank=True, null=True)
    veh_status = models.TextField(blank=True, null=True)
    id_pk = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'report_mst'


class TestLocation(models.Model):
    locationid = models.BigIntegerField(blank=True, null=True)
    locationname = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'test_location'


class Trackreport(models.Model):
    vehicleid = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    reporttype = models.TextField(blank=True, null=True)
    emailid = models.TextField(blank=True, null=True)
    emailsenttime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'trackreport'


class UpTime2(models.Model):
    date = models.DateField(blank=True, null=True)
    veh_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    speed_non_zero_count = models.IntegerField(blank=True, null=True)
    speed_zero_count = models.IntegerField(blank=True, null=True)
    ign_on_count = models.IntegerField(blank=True, null=True)
    ign_off_count = models.IntegerField(blank=True, null=True)
    total_count = models.IntegerField(blank=True, null=True)
    last_location = models.TextField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    last_speed = models.IntegerField(blank=True, null=True)
    last_ign = models.IntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    no_data_flag = models.IntegerField(blank=True, null=True)
    near_plant = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'up_time2'


class UpTime2April(models.Model):
    id_pk = models.BigIntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    veh_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    speed_non_zero_count = models.IntegerField(blank=True, null=True)
    speed_zero_count = models.IntegerField(blank=True, null=True)
    ign_on_count = models.IntegerField(blank=True, null=True)
    ign_off_count = models.IntegerField(blank=True, null=True)
    total_count = models.IntegerField(blank=True, null=True)
    last_location = models.TextField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    last_speed = models.IntegerField(blank=True, null=True)
    last_ign = models.IntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    no_data_flag = models.IntegerField(blank=True, null=True)
    near_plant = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'up_time2_april'


class UpTime2Dup(models.Model):
    date = models.DateField(blank=True, null=True)
    veh_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    speed_non_zero_count = models.IntegerField(blank=True, null=True)
    speed_zero_count = models.IntegerField(blank=True, null=True)
    ign_on_count = models.IntegerField(blank=True, null=True)
    ign_off_count = models.IntegerField(blank=True, null=True)
    total_count = models.IntegerField(blank=True, null=True)
    last_location = models.TextField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    last_speed = models.IntegerField(blank=True, null=True)
    last_ign = models.IntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    no_data_flag = models.IntegerField(blank=True, null=True)
    near_plant = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'up_time2_dup'


class UpTimenew3(models.Model):
    date = models.DateField(blank=True, null=True)
    veh_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    speed_non_zero_count = models.IntegerField(blank=True, null=True)
    speed_zero_count = models.IntegerField(blank=True, null=True)
    ign_on_count = models.IntegerField(blank=True, null=True)
    ign_off_count = models.IntegerField(blank=True, null=True)
    total_count = models.IntegerField(blank=True, null=True)
    ign_on_minute = models.IntegerField(blank=True, null=True)
    ign_off_minute = models.IntegerField(blank=True, null=True)
    last_ign = models.IntegerField(blank=True, null=True)
    no_data_flag = models.IntegerField(blank=True, null=True)
    near_plant = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'up_timenew3'


class Waypoint(models.Model):
    uniquecode = models.UUIDField()
    address = models.TextField(blank=True, null=True)
    waypointname = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    roadtype = models.TextField(blank=True, null=True)
    geofencing = models.IntegerField()
    status = models.IntegerField()
    entby = models.IntegerField()
    entdt = models.DateTimeField()
    updby = models.IntegerField(blank=True, null=True)
    upddt = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'waypoint'


class Waypointlatlong(models.Model):
    uniquecode = models.UUIDField()
    waypointid = models.IntegerField()
    latitude = models.TextField()
    longitude = models.TextField()
    efffrdt = models.DateTimeField()
    efftodt = models.DateTimeField(blank=True, null=True)
    entby = models.IntegerField()
    entdt = models.DateTimeField(blank=True, null=True)
    updby = models.IntegerField(blank=True, null=True)
    upddt = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'waypointlatlong'
