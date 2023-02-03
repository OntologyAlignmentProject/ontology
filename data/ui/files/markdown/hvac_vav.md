# Modeling an Variable Air Volume (VAV) Box (EQUIP)

    The **@** indicates an Equip, **&** indicates a Device, and **$** 
    indicates a Definition.
    
    The trailing integer identifies the unique instance of the device 
    or equip.

## Basic Cooling Only VAV Model

When using Project Haystack to tag data for an vav, it is typical to nest the points or data definitions as children of the vav entity. The example below illustrates a model that is simple to follow, but will limit the options when applying analytics to the data collected from this equip.

> **Required** Tags applied on the VAV 165 Entity: equip, vav, air
> **Optional** Tags applied on the VAV 165 Entity: reheat, coolingOnly
>
> The devices **&CNTRL223**, **&VFD29** and **&VFD35** are defined outside the context of this AHU.

    @VAV165   equip, vav, air, siteRef: @SITE, spaceRef: @ROOF, 
              deviceRef: &CNTRL94, ahuRef: @AHU12, spaceRef: #ROOM399
      $RUN22      run, cmd, equipRef: @VAV165
      $DATEMP     discharge, air, temp, sensor, equipRef: @VAV165
      $DAFLOW     discharge, air, flow, sensor, equipRef: @VAV165
      $DAFLOWSP   discharge, air, sp, flow, sensor, equipRef: @VAV165
      $DAHUM      discharge, air, humidity, sensor, equipRef: @VAV165
      $ZNCO2      zone, air, co2, sensor, equipRef: @VAV165
      $ZNHUM      zone, air, humidity, sensor, equipRef: @VAV165
      $ZNTEMP     zone, air, temp, sensor, equipRef: @VAV165
      $ZNHTGSP    zone, air, temp, heating, sp, equipRef: @VAV165
      $ZNCLGSP    zone, air, temp, heating, sp, equipRef: @VAV165
      $OADAMPCMD  discharge, air, damper, cmd, equipRef: @VAV165
      $OADAMPPOS  discharge, air, damper, sensor, equipRef: @VAV165