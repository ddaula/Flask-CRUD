# Flask-CRUD
Flask-CRUD-APP
CREATE TABLE public.Test_Cases
(
    id integer NOT NULL DEFAULT nextval('students_id_seq'::regclass),
    Test_Case_Name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    Test_Case character varying(2048) COLLATE pg_catalog."default" NOT NULL,
    Source_Query character varying(2048) COLLATE pg_catalog."default",
	Target_Query character varying(2048) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT Test_Cases_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.Test_Cases
    OWNER to postgres;
    
INSERT INTO public.test_cases(
	 test_case_name, test_case, source_query, target_query)
	VALUES ('data validation','validate data in source and target','select * from source_table123','select * from target_table123');
	
