from tasks.models import User

# Sample user data
users_data = [
    {
        "username": "admin_user",
        "email": "admin@example.com",
        "mobile": "1234567890",
        "first_name": "Admin",
        "last_name": "User",
        "role": "ADMIN",
        "password": "sample_admin",
    },
    {
        "username": "regular_user",
        "email": "user@example.com",
        "mobile": "0987654321",
        "first_name": "Regular",
        "last_name": "User",
        "role": "USER",
        "password": "sample_regular",
    },
    {
        "username": "john_doe",
        "email": "john@example.com",
        "mobile": "5551234567",
        "first_name": "John",
        "last_name": "Doe",
        "role": "USER",
        "password": "sample_john",
    },
    {
        "username": "jane_doe",
        "email": "jane@example.com",
        "mobile": "5559876543",
        "first_name": "Jane",
        "last_name": "Doe",
        "role": "USER",
        "password": "sample_jane",
    }
]

# Populate the database with the user data
user_created_count = 0
for user_data in users_data:
    try:
        user = User.objects.get_or_create(
            username=user_data["username"],
            email=user_data["email"],
            mobile=user_data["mobile"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            role=user_data["role"],
            password=user_data["password"]
        )
        user_created_count += 1
    except Exception as e:
        print(f'unable to create user: {user_data["username"]}')

print(f'{user_created_count}/5 Sample users created successfully.')
