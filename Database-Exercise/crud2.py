import os 
from database import con, cur

def create_user():
    os.system('clear')
    fname = input('Enter your Firstname:')
    lname = input('Enter your Lastname:')
    ide_num = input('Enter your Ide_number:')
    email = input('Enter your Email:')
    new_data = f'''
        insert into users(firstname, lastname, ide_number, email) values('{fname}','{lname}','{ide_num}','{email}')
    '''

    con.execute(new_data)
    con.commit()
    print("::: User has been created sucesfully! :::")

# create_user()
                  
# Read
def list_users():
    os.system('clear')
    users_data_query = '''
        select 
            id,
            firstname,
            lastname,
            ide_number,
            email,
            case when status = 1 then 'Active' else 'Inactive' end as status 
        from 
            users
    '''
    
    cur.execute(users_data_query)
    data = cur.fetchall()
    print(data)

list_users()