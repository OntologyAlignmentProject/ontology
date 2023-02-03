# Analytic Rules

The following analytic rules are recommended to be run on **VAV Boxes.** The implementation of each of these will vary depending on the analytics provider used, but this list will provide a good start to understanding how well your equipment is running.

1.	Equipment Scheduling 
  
    Review points that directly or indirectly indicate a unit is running outside of the space scheduled hours plus and minus a transition window (damper position, discharge static pressure, discharge air temp)

2.  PID Loop errors

    PID Loop rules run on all points likely to be controlled by a PID Loop such as dampers position, and valve position.
    Trigger when there are large swings between fully open/closed.
    Also trigger when loop hunting occurring (adjustable # peaks, # troughs, time duration).

3.  VAV airflow greater than setpoint

    Triggers when the airflow exceeds the airflow setpoint by 10% for longer than 1 minute.