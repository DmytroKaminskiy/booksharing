# first_name, last_name, age
# select first_name, age from users;
# select age, first_name from users;

# Relation

sql_result_position = (
    ('Dima', 'Kaminskyi', 28),
    ('Alex', 'R', 26),
)

sql_result_dict = (
    {'first_name': 'Dima', 'last_name': 'Kaminskyi', 'age': 28},
    {'first_name': 'Alex', 'last_name': 'R', 'age': 26},
)


###############################################################################
# first_name + last_name

def get_full_name(user):
    return f"{user['first_name']} {user['last_name']}"


# for user in sql_result_dict:
#     print(get_full_name(user))

############################################################
# Object

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


# user1 = User(**sql_result_dict[0])  # __new__ -> self, __init__
# user2 = User(**sql_result_dict[1])

# print(user1.get_full_name())
# print(user2.get_full_name())

users = []
for record in sql_result_dict:
    users.append(User(**record))

print(users)

# ORM - object relation mapping
# Django ORM, SqlAlchemy ORM.

first_name = 'Dima'
last_name = 'Kaminskyi'
age = 29
