/*
 Examples for count_individuals_by_event
 */
-- No event
select * from public.count_individuals_by_event(
    _gender_code := 'Gender:F'
); -- 2623

-- Condition: Heart disease. Has four descendants at various levels, and concept itself also occurs.
select * from public.count_individuals_by_event(
    ARRAY['SNOMED:56265001']
); -- 34
select * from public.count_individuals_by_event(
    ARRAY['SNOMED:56265001'],
    _min_age_of_onset := 24,
    _max_age_of_onset := 42
); -- 17
select * from public.count_individuals_by_event(
    ARRAY['SNOMED:56265001'],
    _include_descendants := TRUE
); -- 504 !== 34 (descendants to be implemented)

select * from public.count_individuals_by_event(
    _event_codes := ARRAY['SNOMED:56265001', 'SNOMED:410429000', 'SNOMED:53741008', 'SNOMED:230690007', 'SNOMED:22298006']
); -- 504  !== 577 (why?)

-- Condition: Non-small cell lung cancer.
select public.count_individuals_by_event(
    ARRAY['SNOMED:254637007']
); -- 12

-- Drug:  Warfarin
select public.count_individuals_by_event(
    ARRAY['RxNorm:855332']
); -- 137
select public.count_individuals_by_event(
    ARRAY['RxNorm:855332'],
    _gender_code := 'Gender:F'
); -- 44

-- Measurement: Cholestrol in Serum or Plasma
select public.count_individuals_by_event(
    ARRAY['LOINC:2093-3']
); -- 495
select public.count_individuals_by_event(
    ARRAY['LOINC:2093-3'],
    _min_value := 250,
    _unit_code := 'UCUM:mg/dL'
); -- 130
select public.count_individuals_by_event(
    ARRAY['LOINC:2093-3'],
   _max_value := 160,
   _unit_code := 'UCUM:mg/dL'
); -- 344 (note, persons can have multiple measurements, with different values)
select public.count_individuals_by_event(
    ARRAY['LOINC:LP15493-7'], -- Cholestrol, LOINC Component
    _include_descendants := TRUE
); -- 495 (all, in HDL and in LDL)

-- Observation: history of cardiac arrest
select public.count_individuals_by_event(
    ARRAY['SNOMED:429007001']
); -- 155
select public.count_individuals_by_event(
    ARRAY['SNOMED:429007001'],
    _value_code := 'None:No matching concept'
); -- 155