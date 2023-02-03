# Modeling a Power Meter (DEVICE)

A Power Meter is a device, monitoring the power production or usage, as well as the energy production and/or usage.

> Tags applied on the Power Meter 200 Entity: device, elec, meter
>
> The following example would represent an electric power meter installed on Circuit Breaker 12 on MVSG3. The Breaker is named MSVG312.

    &PWRMETER200    device, elec, meter, siteRef: @SITE, spaceRef: @ROOF,
                    equipRef: @MVSG312
      $DEVST          status, sensor, deviceRef: &PWRMETER200