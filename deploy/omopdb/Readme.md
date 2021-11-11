# Setup
The queries in this folder need to be run as a one-time setup of the EHD Beacon.

First, run [view_clinical_events.sql](view_clinical_events.sql).
- Replace `@cdm` with your OMOP CDM schema.
- Replace `@vocab` with your OMOP Vocabulary schema (can be the same as your OMOP CDM schema).

Then, run [count_individuals_by_event.sql](count_individuals_by_event.sql). No replacement necessary. 
This creates a Pl/gSQL function.

Both the view and the function will be created in the `public` schema.

# Examples
To test whether the scripts executed correctly, you can use the examples given.