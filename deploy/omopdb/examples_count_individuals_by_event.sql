/*
 Examples
 */
-- Condition: Heart disease. Has four descendants at various levels, and concept itself also occurs.
select * from public.count_individuals_by_event(
    'SNOMED:56265001'
); -- 34
select * from public.count_individuals_by_event(
    'SNOMED:56265001',
    24,
    42
); -- 17
select * from public.count_individuals_by_event(
    'SNOMED:56265001',
    _include_descendants := TRUE
); -- 504

-- Condition: Non-small cell lung cancer.
select public.count_individuals_by_event(
    'SNOMED:254637007'
); -- 12

-- Drug:  Warfarin
select public.count_individuals_by_event(
    'RxNorm:855332'
); -- 137
select public.count_individuals_by_event(
    'RxNorm:855332',
    _gender_code := 'Gender:F'
); -- 44

-- Measurement: Cholestrol in Serum or Plasma
select public.count_individuals_by_event(
   'LOINC:2093-3'
); -- 495
select public.count_individuals_by_event(
   'LOINC:2093-3',
    _min_value := 250,
    _unit_code := 'UCUM:mg/dL'
); -- 130
select public.count_individuals_by_event(
   'LOINC:2093-3',
   _max_value := 160,
   _unit_code := 'UCUM:mg/dL'
); -- 344 (note, persons can have multiple measurements, with different values)
select public.count_individuals_by_event(
   'LOINC:LP15493-7', -- Cholestrol, LOINC Component
    _include_descendants := TRUE
); -- 495 (all, in HDL and in LDL)

-- Observation: history of cardiac arrest
select public.count_individuals_by_event(
   'SNOMED:429007001'
); -- 155
select public.count_individuals_by_event(
   'SNOMED:429007001',
    _value_code := 'None:No matching concept'
); -- 155