# The Ontology Alignment Project
Version 1.1 - August 4, 2020

## Why make another Taxonomy/Ontology/Naming standard'?'

First, let's get this question answered and out of the way! Currently, there are two main standards for naming and tagging in the building automation industry globally. We believe these are crucial first steps to solving the enormous challenges associated with building system data and efforts to make that data both available and useful across enterprises. [Project Haystack](https://project-haystack.dev/) and [Brick Schema](https://brickschema.org/) have given us a great start and we hope to contribute anything new from our taxonomy back to these standards as applicable. Our ultimate goal, which has carried through all aspects of this effort, is to support and extend the methods and tags already defined in these existing standards at a rate that is compatible with real-world integration project deliverables and timeframes.

We are driven by project work that dictates certain milestones. On projects, naming and tagging standarization needs to happen quickly, and it needs to accommodate a steady stream of new devices and systems within the taxonomy. We strive to make our process open and inclusive within the confines of these goals. To learn more about the Ontology Alignment Project (OAP) and to inquire about our working group, contact oap@buildingsiot.com.

## Who is this taxonomy for'?'

The Ontology Alignment Project is openly available for use by systems integrators or anyone responsible for establishing a building automation system database that is expected to track assets, trigger alarms, enable analytics, store histories and other relevant functions.


***

## Using the Ontology Alignment Project

### Glossary of Terms

#### Primary Terms

##### Definitions

Definitions are used to establish a set of one or more marker tags used in combination. Think of definitions like compound words. Taken separate, each word can mean something different. Put together, the combination of the two or more words become a new term.

Definitions are formatted as individual short names in all CAPS. Each tag name used in a definition must itself be formally defined and must be a subtype of marker.

Definitions are applied to dicts by applying each tag separately.

> To apply the ELECMETER definition to a dict, we would add the individual tags **device, elec,** and **meter.**
>> In Haystack 3, this electric meter would be an equip, but with the addition of the device concept in Haystack 4, it is more appropriate to refer to the meter entity as a device.
>
> To apply the DAT definition to a dict, add individual tags **point, discharge, air, temp,** and **sensor.**

The definition short name is significant - the symbol itself defines a unique identifier.

Definitions do not have implied subtyping. For example HWP does not imply that it subtypes from either hot or water. Subtyping must be explicitly specified in the definition via the is tag.

***

##### Devices

Devices are "Microprocessor based hardware devices" as defined by Project Haystack. This definition is taken literally to be anything that contains a microprocessor and runs software to execute logic.

> A controller is an obvious example of a device in the HVAC System or Lighting Control System. In addition, the ports, network and IO would be considered devices as well, with a deviceRef of the controller.
>
> In the case of information systems, the network switch would be considered an device, as would its associated ports.

***

##### Equips

Project Haystack describes an equip as an "Equipment asset." This term has be liberally applied to all entities containing points or data definitions, but this is too broad, especially with the new device entity. Careful consideration must be given for each equip to ensure it is not a device.

> An AHU is an obvious example of an equip in the HVAC System.
> In the case of lighting, the Lighting Control Panel (LCP) would be considered an equip.

**An entity may not be both an EQUIP and a DEVICE as they are meant to be peer level entities separated only by the presence of a microprocessor.**

***

##### Sites

A Site is a geographic location of the built environment. Specific Site types are further defined using the [Energy Star Property Types](https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager/identify-your-property-type-0).

***

##### Spaces

A Space is a three-dimensional volume in the built environment.

***

##### Systems

A **system** is a group of interacting or interrelated entities that form a unified whole. A system is delineated by its spatial and temporal boundaries, surrounded and influenced by its environment, described by its structure and purpose and expressed in its functioning.

[^1]: Definition sourced from [wiki](https://en.wikipedia.org/wiki/System)

***

#### Cards (Areas that further describe)

This site contains a series of cards, each providing additional context and information about the object of focus.

##### Type

The Type card contains the complete set of tags that define the type of object as described in the Definitions section above.
> For example, a Discharge Air Duct (navName: DADUCT) would have a type definition with the following tags: **equip, duct, discharge,** and **air**

***

##### Identification

The Identification card contains the tags that are used to identity a specific instance of an object. In the case of equipment, this could be thought of as "boilerplate" information.

Included in this set of tags would be:

* A unique identifier of the object, often something like a UUID.
* A display name that is human-readable that would help distinguish the object from others of its type, e.g. AHU1

***

##### Reference (Relationships)

The Reference card contains the list of reference tags that could be defined for an object to indicate a relationship to another object.

References model how entities are related to one another. Entities cross reference each other with ref tags using the id tag as the primary identifier. This design is just like the relational model with primary key (the id tag) and foreign keys (other ref tags). We use the term reference to denote instance-to-instance information versus definition-to-definition associations.
> For example, a Energy Valve on an AHU would contain an **equipRef** to the appropriate AHU.

###### Reference Example

Here is an HVAC System example:

    hot water plant entity
    id: @hwp, hot, water, plant, equip
    
    AHU entity which receives hot water from the plant above
    id: @ahu, ahu, equip, hotWaterPlantRef: @hwp

Here is an SPACE example:

    HVAC Zone
    id: @HVACZone22, hvac, zone
    
    Office entity which receives conditioned air to the Room above
    id: @Office355, space, room, hvacZoneRef: @HVACZone22

Here is an example defining multiple references:

    VAV Controller entity
    id: &CNTRL399, device
    
    VAV entity
    id: @VAV22, equip, vav, air, ahuRef: @AHU5, deviceRef: &CNTRL399
    
    HVAC Zone
    id: @HVACZone22, hvac, zone, vavRef: @VAV33
    
    Office entity which receives conditioned air to the Room above
    id: @Office355, space, room, hvacZoneRef: @HVACZone22

***

##### Definitions (Points)

The items listed in the Definitions card are the definitions (or points) that can be directly assigned this site, space, equip or device. This is not to be prescriptive as there is some flexibility for modeling sub-equip and sub-devices.

If a definition in this list is created for the object, then the reference to the object must be specified to it.
> For example, if the definition *Discharge Air CO2 (DACO2)* is created for a *Discharge Air Duct (DADUCT)*, then there should be an **equipRef** on the definition that relates it to the equipment.

***

##### Alarm

The Alarm card is applicable to definitions and is the set of tags that define their alarm configuration.

Ontologies inform alarm configurations in critical ways. While some alarms are triggered through an analytics platform at the enterprise, much of the fault detection and diagnostics on your system happens in near-real-time. As such, alarms need to be applied closer to the edge. Where alarms are executed against tag rules or to measure a specific data point, it is important to consider the alarm type. It is also important to be mindful of alarm fatigue which will come when too many alarms are set up within a given system.

Within the OAP, we attempt to define the minimum point alarm requirements while making an attempt to reduce the overall number of alarms. It is difficult to achieve this balance with every unique application, so alarm configurations should be evaluated independently for each system. Here, though, we provide a general template for configuring alarms within the OAP naming conventions.

> Niagara 4 Users:
> Alarm Name Convention: Use bFormat: %parent.parent.parent.displayName%_%parent.displayName%
> This will have all histories named EquipName_PointName, ex. AHU1_MAT

***

##### History

The History card is applicable to definitions and is the set of tags that define how data values will be measured and stored.

Similar to Alarms, Histories are a critical piece of an integrated automation system. Histories can track any points within your taxonomy at any time interval. Histories become useful when you're applying advanced analytics to your system, or when you need to investigate an ongoing problem. Given that we do not know when a history on a specific point will be valuable, the tendency is to place a trend or history record on every piece of data. The OAP subscribes to this ideology, but we believe it is also important to clearly define when each record is to be stored and the length of time the data needs to be retained. Just like alarms, it will be important to look at each application to determine if the suggested default history rules will appropriately suit the application.

> Niagara 4 Users:
> History Name Convention: Use bFormat: %parent.parent.parent.name%_ %parent.name%
> This will have all histories named EquipName_PointName, ex. AHU1_MAT.

***

##### Roots

The Roots card is applicable to definitions and represents the **sites**, **spaces**, **equips** and **devices** that a definition can be assigned to.  When a specific instance of the definition is created, a reference to the specific root should be included.
> For example, in instance of the definition *Discharge Air Temp (DAT)* will contain an reference (i.e. equipRef) to the specific equipment that it is related to (e.g. *Discharge Air Duct (DADUCT)*)

***

##### Extended By

The Extended By card is meant to indicate the **definitions**, **equips** and **devices** that extend this particular definition, equip, or device.  It is meant for informational purposes and is not required when creating specific instances of objects.

***

## Applying the information in this site

One of the bigger challenges with Project Haystack and Brick is the lack of consistent methodology for applying the standards to data. The Ontology Alignment Project attempts to resolve this issue. The short name, or navName, shown in ALL CAPS, is the preferred short name for the point in the database at the device level. It is well understood that some devices do not allow for customization of the point names in the device and for those devices, the manufacturer names are sufficient. For all other programmable or highly configurable devices, it is required that the names in this site be used to identify the data or point in the device. There are a lot of advantages to this. The biggest is the time it takes human or AI to find the point is greatly reduced, thus making integration time minimal.

> It is **required** that the names in this site be used to identify the data or point in the programmable or highly configurable device.

There are examples throughout this site illustrating the best definitions to apply to data and/or points in the system being modeled. If a new definition is required, there is a simple process to get the new term added to the DEV site of the taxonomy. This method allows us to add the definition in a timely manner, but provides a review in case modification needs to be made prior to releasing the new definition in the next version update.

### Navigating the site

The site can be navigated in a few ways. You can simply use the menu to navigate to the specific definition, device, equip, etc. or you can locate the appropriate information by navigating the systems. You may also search for key words in the Search Bar at the top right of the page. This will populate all of the areas where the key word occurs. 

> **Looking for something quickly?** Try the key word search!

***

## Contributors

- [Buildings IOT](https://www.buildingsiot.com/)
- [ControlTech](https://www.controltech.net.au/)

***

## FAQ

### Add Tags or Definitions to this taxonomy

Send an email to oap@buildingsiot.com with your suggestions and requests. The OAP team meets weekly to discuss this additions and will add as required. The goal is to quick expand this site, as well as to provide many examples. The industry needs consistency with these models.

### Join the OAP Team

You can! We like to keep the team relatively small, but we also have need to add experts in various industries to make sure we get the devices, equips, and definitions right! If you want to contribute, please submit your request to oap@buildingsiot.com

### Site Updates

As we discuss above, OAP considers this taxonomy to be an ongoing effort. With the release of version 1, we are continuing to add to the model on a dev site. When we reach a point where enough information has been added, we will issue version 2. Versions will be linked from the left-hand sidebar of the site, under the OAP logo.

### Other usability questions

With the completion of version 1 and the proof of concept achieved, our team is working on a training section that further describes how to apply the OAP for real-world data modeling. We are developing these training resources with system integrators in mind.

***


