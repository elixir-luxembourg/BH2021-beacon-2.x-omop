# Setup
The queries in this folder need to be run as a one-time setup of the EHD Beacon.
This creates a view and PL/pgsql functions in the `public` schema. 
These are used by the Beacon endpoints.

For the `api/individuals` endpoint, two script need to be run on deploy:

First, run [view_clinical_events.sql](view_clinical_events.sql).
- Replace `@cdm` with your OMOP CDM schema.
- Replace `@vocab` with your OMOP Vocabulary schema (can be the same as your OMOP CDM schema).

Then, run [count_individuals_by_event.sql](count_individuals_by_event.sql). No replacement necessary. 
This creates a Pl/gSQL function.

For the `api/filter_endpoints`, the script in [get_filtering_terms.sql](get_filtering_terms.sql) needs to be run.
- Replace `cdm_synthea10` with your OMOP CDM schema, which should also include the OMOP vocabularies tables.

# Examples

To test whether the scripts executed correctly, you use the example queries given in:
- [examples_view_clinical_events.sql](examples_view_clinical_events.sql)
- [examples_count_individuals_by_event.sql](examples_count_individuals_by_event.sql)

# Notes and Todos

## View `clinical_events`
**Note**
- Note: the view includes the column `ordinal`. This is a counter that increments for each observation of the same code for a person. i.e. if `ordinal = 1` then this is the first occurrence of this code in that person's history. 
 

## Function `count_individuals_by_event`
- TODO: Include hierarchical descendants of a given code is **not** supported. It can be done, but requires some changes to the view. 
- Note: The `age` parameters are implemented such that it will count every person that has an occurrence of the given code(s) in that age range. This is not necessary the age of onset (i.e. the first occurrence, see also the `ordinal` variable) 
- Note: When no parameters are supplied, a distinct count of all persons is given. It is also possible to only 
- Note: The function does not support multiple measures with multiple different values. The same value range is applied to all given codes.

## Function `get_filtering_terms`
- 