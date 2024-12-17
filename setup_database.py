import psycopg2

def create_tables():
    # Replace these values with your actual database connection parameters
    db_params = {
        'dbname': 'coursework',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
        'port': '5432',
    }

    # Connect to the database
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # SQL statements to create tables
    sql_statements = [
    '''
    CREATE TABLE IF NOT EXISTS public.department
    (
        id serial PRIMARY KEY,
        name VARCHAR(250) UNIQUE
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS public.employee_info
    (
        id serial PRIMARY KEY,
        user_id INTEGER,
        department_id INTEGER,
        "Name" VARCHAR(250),
        "Surname" VARCHAR(250),
        "Fathers_name" VARCHAR(250),
        "Date_of_birth" TIMESTAMP WITHOUT TIME ZONE,
        "Adress" VARCHAR,
        hire_date TIMESTAMP WITHOUT TIME ZONE,
        termination_date TIMESTAMP WITHOUT TIME ZONE,
        CONSTRAINT employee_info_user_id_key UNIQUE (user_id),
        CONSTRAINT employee_info_department_id_fkey FOREIGN KEY (department_id)
            REFERENCES public.department (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION,
        CONSTRAINT employee_info_user_id_fkey FOREIGN KEY (user_id)
            REFERENCES public.users (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS public.leave_request
    (
        id serial PRIMARY KEY,
        user_id INTEGER,
        start_date DATE,
        end_date DATE,
        status VARCHAR(50),
        CONSTRAINT leave_request_user_id_fkey FOREIGN KEY (user_id)
            REFERENCES public.users (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS public.note
    (
        id serial PRIMARY KEY,
        data VARCHAR(10000),
        date TIMESTAMP WITH TIME ZONE,
        user_id INTEGER,
        CONSTRAINT note_user_id_fkey FOREIGN KEY (user_id)
            REFERENCES public.users (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS public.salary
    (
        id serial PRIMARY KEY,
        user_id INTEGER,
        amount DOUBLE PRECISION,
        CONSTRAINT salary_user_id_key UNIQUE (user_id),
        CONSTRAINT salary_user_id_fkey FOREIGN KEY (user_id)
            REFERENCES public.users (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
    )
    '''
]

    # Execute SQL statements
    for sql_statement in sql_statements:
        cursor.execute(sql_statement)

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
