# Modeling an Air Handling Unit (EQUIP)

    The **@** indicates an Equip, **&** indicates a Device, and **$** 
    indicates a Definition.
    
    The trailing integer identifies the unique instance of the device 
    or equip.

## Basic AHU Model

When using Project Haystack to tag data for an ahu, it is typical to nest the points or data definitions as children of the ahu entity. The example below illustrates a model that is simple to follow, but will limit the options when applying analytics to the data collected from this equip.

> Tags applied on the Air Handler 12 Entity: equip, ahu, air
>
> The devices **&CNTRL223**, **&VFD29** and **&VFD35** are defined outside the context of this AHU.

    @AHU12    equip, ahu, air, siteRef: @SITE, spaceRef: @ROOF, 
              deviceRef: &CNTRL223
      $RUN22      run, cmd, equipRef: @AHU12
      $DATEMP     discharge, air, temp, sensor, equipRef: @AHU12
      $DAFANCMD   discharge, air, fan, cmd, equipRef: @DAFAN12
      $DAFANST    discharge, air, fan, sensor, equipRef: @DAFAN12
      $VFDCMD     discharge, air, vfd, run, cmd, equipRef: @AHU12,
                  deviceRef: &DAVFD12
      $VFDSPD     discharge, air, vfd, speed, cmd, equipRef: @AHU12,
                  deviceRef: &DAVFD12
      $VFDFREQ    discharge, air, vfd, freq, sensor, equipRef: @AHU12,
                  deviceRef: &DAVFD12
      $VFDPWR     discharge, air, vfd, elec, real, power, sensor,
                  equipRef: @AHU12, deviceRef: &DAVFD12
      $VFDENE     discharge, air, vfd, elec, energy, sensor,
                  equipRef: @AHU12, deviceRef: &DAVFD12
      $RATEMP12   return, air, temp, sensor, equipRef: @AHU12
      $RACO212    return, air, co2, sensor, equipRef: @AHU12
      $RAFANCMD   return, air, fan, cmd, equipRef: @AHU12
      $RAFANST    return, air, fan, sensor, equipRef: @AHU12
      $RAFANCMD   discharge, air, fan, cmd, equipRef: @AHU12
      $RAFANST    discharge, air, fan, sensor, equipRef: @AHU12
      $VFDCMD     discharge, air, vfd, run, cmd, equipRef: @AHU12
                  deviceRef: &DAVFD13
      $VFDSPD     discharge, air, vfd, speed, cmd, equipRef: @AHU12
                  deviceRef: &DAVFD13
      $VFDFREQ    discharge, air, vfd, freq, sensor,
                  equipRef: @AHU12, deviceRef: &DAVFD13
      $VFDPWR     discharge, air, vfd, elec, real, power, sensor,
                  equipRef: @AHU12, deviceRef: &DAVFD13
      $VFDENE     discharge, air, vfd, elec, energy, sensor,
                  equipRef: @AHU12, deviceRef: &DAVFD13
      $MATEMP     mixed, air, temp, sensor, equipRef: @AHU12
      $MAFILTERST mixed, air, filter, sensor
      $MADAMPCMD  mixed, air, damper, cmd, equipRef: @AHU12
      $MADAMPPOS  mixed, air, damper, sensor, equipRef: @AHU12
      $OATEMP     outside, air, temp, sensor, equipRef: @AHU12
      $OAFLOW     outside, air, flow, sensor, equipRef: @AHU12
      $OACO2      outside, air, co2, sensor, equipRef: @AHU12
      $OADAMPCMD  outside, air, damper, cmd, equipRef: @AHU12
      $OADAMPPOS  outside, air, damper, sensor, equipRef: @AHU12

## Expanded AHU Model

An ahu is accurately tagged as an equip. The ahu may have sub-equips as well. These can include fans, coils, ducts, and dampers. It is up to the designer to determine the most effective way to model this ahu. Below is an example of a model that will allow many options when applying analytics to the data collected from this equip.

> Tags applied on the Air Handler 12 Entity: equip, ahu, air
> Sub-Equips: DADUCT, RADUCT, MADUCT, OADUCT, DAFAN, RAFAN, CLGCOIL, HTGCOIL
>
> The **@** indicates an Entity, **&** indicates a Device, and **$** indicates a DEF
>
> The trailing integer identifies the unique instance of the device or equip.
>
> The devices **&CNTRL223**, **&VFD29** and **&VFD35** are defined outside the context of this AHU.

    @AHU12    equip, ahu, air, siteRef: @SITE, spaceRef: @ROOF,
              deviceRef: &CNTRL223
      $RUN22      run, cmd, equipRef: @AHU12
      @DADUCT13   equip, discharge, air, duct, equipRef: @AHU12
        @CLGCOIL12    equip, cooling, coil, chilledWaterCooling,
                      equipRef: @AHU12
        @HTGCOIL44    equip, heating, coil, hotWaterHeating, 
                      equipRef: @AHU12
          $DATEMP1        discharge, air, temp, sensor, equipRef: @DADUCT13
                          inletEquipRef: @HTGCOIL12,
                          dischargeEquipRef: @CLGCOIL12
          $DATEMP2        discharge, air, temp, sensor, equipRef: @DADUCT13,
                          inletEquipRef: @CLGCOIL12
        @DAFAN12      equip, discharge, air, fan, equipRef: @AHU12,
                      deviceRef: &VFD29
          $DAFANCMD       discharge, air, fan, cmd, equipRef: @DAFAN12
          $DAFANST        discharge, air, fan, sensor, equipRef: @DAFAN12
          $VFDCMD         discharge, air, vfd, run, cmd, equipRef: @DAFAN12,
                          deviceRef: &DAVFD12
          $VFDSPD         discharge, air, vfd, speed, cmd, 
                          equipRef: @DAFAN12, deviceRef: &DAVFD12
          $VFDFREQ        discharge, air, vfd, freq, sensor, 
                          equipRef: @DAFAN12, deviceRef: &DAVFD12
          $VFDPWR         discharge, air, vfd, elec, real, power, sensor,
                          equipRef: @DAFAN12, deviceRef: &DAVFD12
          $VFDENE         discharge, air, vfd, elec, energy, sensor,
                          equipRef: @DAFAN12, deviceRef: &DAVFD12
        @RADUCT12     equip, return, air, duct, equipRef: @AHU12,
                      deviceRef: &VFD35
          $RATEMP12       return, air, temp, sensor, equipRef: @RADUCT12
          $RACO212        return, air, co2, sensor, equipRef: @RADUCT12
        @RAFAN12      equip, retun, air, fan, equipRef: @RADUCT12
          $RAFANCMD       return, air, fan, cmd, equipRef: @RAFAN12
          $RAFANST        return, air, fan, sensor, equipRef: @RAFAN12
          $RAFANCMD       discharge, air, fan, cmd, equipRef: @RAFAN12
          $RAFANST        discharge, air, fan, sensor, equipRef: @RAFAN12,
                          deviceRef: &DAVFD12
          $VFDCMD         discharge, air, vfd, run, cmd,
                          deviceRef: &DAVFD12, equipRef: @RAFAN12
          $VFDSPD         discharge, air, vfd, speed, cmd, 
                          deviceRef: &DAVFD12, equipRef: @RAFAN12
          $VFDFREQ        discharge, air, vfd, freq, sensor,
                          deviceRef: &DAVFD12, equipRef: @RAFAN12
          $VFDPWR         discharge, air, vfd, elec, real, power, sensor,
                          deviceRef: &DAVFD12, equipRef: @RAFAN12
          $VFDENE         discharge, air, vfd, elec, energy, sensor,
                          deviceRef: &DAVFD12, equipRef: @RAFAN12
        @MADUCT12       equip, mixed, air, duct, equipRef: @AHU12
          $MATEMP         mixed, air, temp, sensor, equipRef: @MADUCT12
          $MAFILTERST     mixed, air, filter, sensor, equipRef: @MADUCT12
        @MADAMP26       equip, mixed, air, damper, equipRef: @AHU12
          $MADAMPCMD      mixed, air, damper, cmd, equipRef: @MADAMP26
          $MADAMPPOS      mixed, air, damper, sensor, equipRef: @MADAMP26
        @OADUCT12       equip, outside, air, duct, equipRef: @AHU12
          $OATEMP         outside, air, temp, sensor, equipRef: @OADUCT12
          $OAFLOW         outside, air, flow, sensor, equipRef: @OADUCT12
          $OACO2          outside, air, co2, sensor, equipRef: @OADUCT12
        @OADAMP15       equip, damper, outside, air, ventilates, airCooling,
                        equipRef: @AHU12, equipRef: @OADAMP12
          $OADAMPCMD      outside, air, damper, cmd, equipRef: @OADAMP15
          $OADAMPPOS      outside, air, damper, sensor, equipRef: @OADAMP15