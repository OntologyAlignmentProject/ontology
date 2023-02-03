# Modeling a Network Switch (DEVICE)

## Switch Device

A Network Switch is a device, which contains multiple PORT DEVICES. PORTS are mostly RJ45 and connected to other RJ45 Ports on an edge device.

> Tags applied on the Network Switch Entity: device, network, switch, managed
>
> The following example would represent a network switch, containing 12 RJ45 communication ports, 4 SFP communication ports, and 2 power supplies. The Network Switch is named NETSW29.

    &NETSW29    device, network, switch, managed, sfpPortNum: 4, 
                rj45PortNum: 12, siteRef: @SITE, spaceRef: @Network Room 332
      $DEVST      status, sensor, deviceRef: &NETSW29
      $PWRSUPST   status, power, supply, sensor, deviceRef: &NETSW29

## Port Device

A Port is a device, which may be contained by a Network Switch, Controller, or any other device. PORTS are mostly RJ45 and connected to other RJ45 Ports on a device.

> At minimum, tags applied on the Port Entity include: device, port
>
> The following example would represent a network switch, containing 12 RJ45 communication ports, 4 SFP communication ports, and 2 power supplies. The Port is named PORT334.

    &PORT291    device, port, poe, rj45PortId: 2, siteRef: @SITE
                spaceRef: @Network Room 332, deviceRef: NETSW29
      $CONNST     connection, status, sensor, deviceRef: &PORT291
      $POEEN      poe, enable, cmd, deviceRef: &PORT291
      $BWUSE      bandwidth, usage, sensor, deviceRef: &PORT291
      $REALPWR    power, sensor, deviceRef: &PORT291