import json

from domain.user.user import User


class UserRepo:
    def __init__(self, file_path: str):
        self.file_path = file_path
        try:
            with open(self.file_path) as f:
                contents = f.read()
            users_info = json.loads(contents)
            self.__users = [User(x) for x in users_info]
        except:
            self.__users = []

    def add(self, new_user: User):
        self.__users.append(new_user)
        users_info = [(x.id, x.username) for x in self.__users]
        users_json = json.dumps(users_info)
        with open(self.file_path, "w") as file:
            file.write(users_json)

    def get_all(self) -> list[User]:
        return self.__users

    # TODO homework, replace username with an id
    # when we create a user we should create a uuid for it
    # when we return all the user, each user should have the id field
    # when we query a single user or delete a user we should pass the id

    # create POST /<user_id>/stocks
    # the user can add a stock to its portfolio, by giving the ticker and the number of units it has
    # save the country, full name of the company
    # when we get a specific user we get the price of every stock the user has and the money it has on it

    def get_by_id(self, id_) -> User:
        for u in self.__users:
            if u.id == id_:
                return u
