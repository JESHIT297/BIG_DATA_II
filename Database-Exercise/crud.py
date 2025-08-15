import os 
from database import con, cur

def create_user():
    os.system('clear')
    new_data = '''
        INSERT INTO users (firstname, lastname, ide_number, email) VALUES ('Jeshit', 'Armero', '4321', 'jeshit@gmail.com');
    '''

    con.execute(new_data)
    con.commit()
    print('::: User has been created sucesfully! :::')

create_user()