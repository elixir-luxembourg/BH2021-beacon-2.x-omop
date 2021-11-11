select *
from public.clinical_events
-- where domain_name = 'Measurement'
ORDER BY random();

select *
from public.clinical_events
where value_code IS NOT NULL AND value_code != 'None:No matching concept'
;

select person_id, value_as_number, unit_code
from public.clinical_events
where event_code = 'LOINC:2093-3'
and value_as_number > 200
;
