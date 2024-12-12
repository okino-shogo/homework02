from db_config import Message

print("===== Welcome to CRM Application =====")
print("[S]how: Show all users info")
print("[A]dd: Add new user")
print("[Q]uit: Quit The Application")
print("======================================")
print("")


# ユーザー一覧表示
def all_star():
    messages = Message.select()
    for i in messages:
        print(f"Name: {i.name} Age: {i.age}")


# 新規ユーザー追加
def add_user(name, age):
    Message.create(name=name, age=age)


while True:

    user_cm = input("Your command >")

    if user_cm == "S":
        all_star()
        print("")

    elif user_cm == "A":
        new_name = input("New user name >")
        new_age = input("New user age >")
        add_user(new_name, new_age)
        print(f"Add new user: {new_name}")
        print("")
    # 終了する
    elif user_cm == "Q":
        print("Bye!")
        break

    else:
        print("command not found")
        print("")
