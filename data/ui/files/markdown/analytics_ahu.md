# Analytic Rules

The following analytic rules are recommended to be run on **Air Handling Units.** The implementation of each of these will vary depending on the analytics provider used, but this list will provide a good start to understanding how well your equipment is running.

1.	Equipment Scheduling 
  
    Review points that directly or indirectly indicate a unit is running outside of the unit scheduled hours plus and minus a transition window (fan status, discharge static pressure, discharge air temp)

2.	Duct Static Pressure Reduce/Reset
    
    Alarm when all VAV boxes in service area are below 90% open.

3.	Economizer OA Damper above minimum position

    Show periods when OA damper should be at minimum position per outside air temp, internal CO2, building pressure, but it is not.  Rule to adjust for ahu type (ie. Constant volume vs variable volume)

4.	Economizer excessive outside air

    Winter only, triggers when calculated OA% is greater than minimum outside air required by 10%.

5.	Economizer not operating

    Looks at various aspects of economizer function to trigger when it is not at minimum position but should be.

6.	Supply Air Temperature Reset 
  
    Trigger when discharge air deviates from calculated ideal set point by 5F or more.

7.	Optimum Start for AHU
  
    Trigger when space temperature is brought up to set point more than 1 hour prior to mall occupancy.  Rule does not trigger if zone temperature did not set back more than 5 degrees the previous night.

8.	Simultaneous Heating and Cooling

    Trigger when an individual unit is simultaneously heating & cooling.  
    This rule can easily be duplicated and modified to compare multiple units by adding tags to define a group of AHUs (tag => ahuGroup: “Str”).

9.	Heating and cooling cycling
    
    Trigger when AHU switches quickly from heat to cool mode and back within 30 minutes.

10.	Setback Space Temperature
  
    Trigger when zone temp is not set back at night indicating heating or cooling is active overnight.

11.	Cooling Compressor/valve failure
    
    Trigger when a compressor turning on, or valve opening, does not result in cooling

12.	Heating element/valve failure
    
    Trigger when a compressor turning on, or valve opening, does not result in heating

13.	PID Loop errors

    PID Loop rules run on all points likely to be controlled by a PID Loop such as dampers position, valve position, and VFD speeds.  
    Trigger when there are large swings between fully open/closed.
    Also trigger when loop hunting occurring (adjustable # peaks, # troughs, time duration).
