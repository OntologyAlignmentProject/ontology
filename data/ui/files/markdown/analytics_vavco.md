# Analytic Rules

The following analytic rules are recommended to be run on **VAV Boxes.** The implementation of each of these will vary depending on the analytics provider used, but this list will provide a good start to understanding how well your equipment is running.

1.	Equipment Scheduling 
  
    Review points that directly or indirectly indicate a unit is running outside of the space scheduled hours plus and minus a transition window (damper position, discharge static pressure, discharge air temp)

2.	Setback Space Temperature
  
    Trigger when zone temp is not set back at night indicating heating or cooling is active overnight.

3.  Cooling failure
    
    Trigger when a cooling is available and opening damper does not result in cooling

4.  PID Loop errors

    PID Loop rules run on all points likely to be controlled by a PID Loop such as dampers position, and valve position.
    Trigger when there are large swings between fully open/closed.
    Also trigger when loop hunting occurring (adjustable # peaks, # troughs, time duration).

5.  VAV unnecessary cooling

    Triggers when the VAV is delivering more than the min cooling flow when the zone is not calling for cooling.

6.  VAV airflow greater than setpoint

    Triggers when the airflow exceeds the airflow setpoint by 10% for longer than 1 minute.