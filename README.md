# The Ontology Alignment Project

## Why make another building Taxonomy/Ontology/Naming standard?

First, let's get this question answered and out of the way! Currently, there are two main standards for naming and tagging in the building automation industry globally. We believe these are crucial first steps to solving the enormous challenges associated with building system data and efforts to make that data both available and useful across enterprises. [Project Haystack](https://project-haystack.dev/) and [Brick Schema](https://brickschema.org/) have given us a great start and we hope to contribute anything new from our taxonomy back to these standards as applicable. Our ultimate goal, which has carried through all aspects of this effort, is to support and extend the methods and tags already defined in these existing standards at a rate that is compatible with real-world integration project deliverables and timeframes.

We are driven by project work that dictates certain milestones. On projects, naming and tagging standarization needs to happen quickly, and it needs to accommodate a steady stream of new devices and systems within the taxonomy. We strive to make our process open and inclusive within the confines of these goals. To learn more about the Ontology Alignment Project (OAP) and to inquire about our working group, contact oap@buildingsiot.com.

## Who is this taxonomy for?

The Ontology Alignment Project is openly available for use by systems integrators or anyone responsible for establishing a building automation system database that is expected to track assets, trigger alarms, enable analytics, store histories and other relevant functions.

## Guide to YAML

### Entity Definition
The main entities defined in OAP are: point, site, equip, device, attribute, kpi and function. Marker tags are not considered a top-level entity, but are used throughout. Each entity in OAP is defined by a unique OAP code and a unique set of marker tags (with the exception of KPIs which do not leverage marker tags). 

### File Structure 
The OAP taxonomy and ontology is represented by a collection of YAML files. The YAML files are organized by domain folders. Each file is named by the entity type that it contains as well as the domain and sub-domain. For example `point.hvac.air.yaml`.


### Points 

Each point in OAP is defined with a common name, a description and an OAP point code ex. "DATSP" - discharge air temperature setpoint Each point has a list of unique tags to differentiate it from other points in the OAP.  There is no limit to how many levels of inheritance is allowable for points 
Ex. CMD -> SSCMD-> PSSCMD 

Points must have a kind. 
Numerical points should have a unit or a unit_type.

### Functions 

Functions house a collection of points that are used in a common control function and tend to be logically or commonly grouped together.  
Ex. DFVSC – Variable Speed Control for discharge fans contains all the points related to controlling the discharge fan. Such as DFSPCMD, DFCMD, DFST.  
Tags that are defined on functions are inherited by the equipment that uses the function as type_optional tags.

Functions are typically only defined on an entity that can have points namely equipment.


### Equips 

Equips are defined with a set of tags that include the equip tag as well as any other relevant marker tags.  Generally, we prefer to have only one level of inheritance for equip (a base type and a variant).
ex. Type: AHU -> subtype: DOAS


### Attributes 

Unlike points which typically correspond to streaming telemetry data, attributes define properties that are typically fixed or static

### Extension

Most entities in OAP are extensible including: sites, spaces, equips, devices, points, KPIs and attributes. This allows the subtype to inherit tags from its parent type. For points, spaces, sites, and equips extending will also cause inheritance of the unit, functions, kpis and attributes defined on an entity. 

For equips, points and functions are not inherited by default. In order for points or functions to be inherited by subtypes, they should be specified under `points_base` or `functions_base` respectively. 

For attributes, subtypes inherit tags and units.

For KPIs, subtypes inherit ranges, rollupCalculations, rollupIntervals, normalizations, comparisons, units, rangeFilters and profileWindows. 

### Contains 

Contains is typically used in conjunction with an `equip` entity. It is a useful way to indicate what equipment or sub equipment is typically found inside another equipment.  

### Type_Optional  

Type Optional tags are a way to tag equipment with additional information without having to define a new variant. `Type_optional` tags provide information that is not used to determine a variant but may be useful for analysis.


### Relationships

Relationships are defined in reference-tags.yaml. Each relationship is categorized by it's type (`REF`) as well as a a subtype (`FLOW`,`MEASURE`,`CONTAIN`). 
