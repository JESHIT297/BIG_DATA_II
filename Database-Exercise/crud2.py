import os 
from database import con, cur

def create_user():
    os.system('clear')
    print("::: Create new user :::")
    fname = input('Enter your Firstname: ')
    lname = input('Enter your Lastname: ')
    ide_num = input('Enter your Ide_number: ')
    email = input('Enter your Email: ')

    check_query = "SELECT * FROM users WHERE ide_number = ? OR email = ?"
    cur.execute(check_query, (ide_num, email))
    
    existing_user = cur.fetchone()
    if existing_user:
        print(f"\nError: A user with that ID number or email already exists. '{ide_num}' o el email '{email}'.")
        input("Press Enter to continue...")
        return 

    new_data = '''
    INSERT INTO users(firstname, lastname, ide_number, email) 
    VALUES (?, ?, ?, ?)
'''
    con.execute(new_data, (fname, lname, ide_num, email))
    con.commit()

    print("::: User has been created sucesfully! :::")
    

def list_users():
    os.system('clear')
    print("::: List all users :::")
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

def list_active_users():
    os.system('clear')
    print("::: List active users :::")
    user_data_query = '''
        select 
            id,
            firstname,
            lastname,
            ide_number,
            email,
            case when status = 1 then 'Active' else 'Inactive' end as status 
        from 
            users
        where
            status = 1
    '''
    cur.execute(user_data_query)
    data = cur.fetchall()
    print(data)

def list_inactive_users():
    os.system('clear')
    print("::: List inactive users :::")
    user_data_query = '''
        select 
            id,
            firstname,
            lastname,
            ide_number,
            email,
            case when status = 1 then 'Active' else 'Inactive' end as status 
        from 
            users
        where
            status = 0
    '''

    cur.execute(user_data_query)
    data = cur.fetchall()
    print(data)

def update_user():
    os.system('clear')
    print("::: Update user :::")

    user_id = input('Enter the ID of the user you want to update: ')

    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cur.fetchone()
    
    if user is None:
        print(f"Error: User does not exist with the ID {user_id}.")
        return
    
    print("\nEnter the new data (leave blank to avoid changing):")

    print(f"Current Firstname: {user[1]}")
    fname = input('New Firstname: ') or user[1]

    print(f"Current Lastname: {user[2]}")
    lname = input('New Lastname: ') or user[2]

    print(f"Current Ide_number: {user[3]}")
    ide_num = input('New Ide_number: ') or user[3]

    print(f"Current Email: {user[4]}")
    email = input('New email: ') or user[4]

    # Status
    current_status_text = 'Active' if user[5] == 1 else 'Inactive'
    print(f"Current Status: {current_status_text} ({user[5]})")

    while True:
        status_input = input('New status (1=Active, 0=Inactive, leave blank to not change): ')
        if status_input in ['1', '0', '']:
            break 
        else:
            print("Error: Please enter only '1', '0' or leave the field blank.")

    status = user[5] if status_input == '' else int(status_input)

    update_query = '''
        UPDATE users
        SET
            firstname = ?,
            lastname = ?,
            ide_number = ?,
            email = ?,
            status = ?
        WHERE
            id = ?
    '''

    values_to_update = (fname, lname, ide_num, email, status, user_id)

    cur.execute(update_query, values_to_update)
    con.commit()

    print("\n::: User updated successfully! :::")
    input("Press Enter to continue...")

def delete_user():
    os.system('clear')
    print("::: Delete user :::")

    user_id = input('Enter the ID of the user you want to delete: ')
    
    cur.execute("SELECT id, firstname, lastname FROM users WHERE id = ?", (user_id,))
    user = cur.fetchone()

    if user is None:
        print(f"Error: No user found with the ID {user_id}.")
        input("Press Enter to continue...")
        return
    
    print(f"\nUser found: {user[1]} {user[2]} (ID: {user[0]})")

    while True:
        confirmacion = input("Are you sure you want to delete this user? (y/n): ").lower()
        if confirmacion in ['y', 'n']:
            break
        else:
            print("Invalid answer. Please enter 'y' for yes or 'n' for no.")
    if confirmacion == 'y':
        delete_query = "DELETE FROM users WHERE id = ?"
        
        cur.execute(delete_query, (user_id,))
        con.commit() 
        
        print("\n::: User deleted successfully! :::")
    else:
        print("\nOperation cancelled.")

    input("Press Enter to continue...")

def search_user():
    os.system('clear')
    print("::: Serch user :::")

    user_id = input('Enter the ID of the user you want to search for: ')

    query = '''
        SELECT 
            id,
            firstname,
            lastname,
            ide_number,
            email,
            CASE WHEN status = 1 THEN 'Active' ELSE 'Inactive' END as status
        FROM 
            users 
        WHERE 
            id = ?
    '''

    cur.execute(query, (user_id,))
    user = cur.fetchone()

    if user:
        print("\n--- User Found ---")
        print(f"ID:         {user[0]}")
        print(f"Firstname:  {user[1]}")
        print(f"Lastname:   {user[2]}")
        print(f"Ide_number: {user[3]}")
        print(f"Email:      {user[4]}")
        print(f"Status:     {user[5]}")
        print("--------------------------")
    else:
        print(f"\nError: No user found with the ID '{user_id}'.")

    input("\nPress Enter to continue...")

def main_menu():
    while True:
        # os.system('clear')
        print("="*25)
        print("      Main Menu:")
        print("="*25)
        print("[1]. Create new user")
        print("[2]. List all users")
        print("[3]. List active users")
        print("[4]. List inactive users")
        print("[5]. Update user (id)")
        print("[6]. Delete user")
        print("[7]. Serch user (id)")
        print("[8]. Exit")
        print("="*25)
        
        option = input("Choose an option: ")

        if option == '1':
            create_user()
        elif option == '2':
            list_users()
        elif option == '3':
            list_active_users()
        elif option == '4':
            list_inactive_users()
        elif option == '5':
            update_user()
        elif option == '6':
            delete_user()
        elif option == '7':
            search_user()
        elif option == '8':
            print("\nGoodbye!")
            break
        else:
            print("\nError: Invalid option. Please choose a number from 1 to 8..")
            input("Press Enter to try again...")

# --- Punto de entrada del programa ---
if __name__ == "__main__":
    main_menu()