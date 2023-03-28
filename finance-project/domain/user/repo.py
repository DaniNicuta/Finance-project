import json

from domain.user.factory import UserFactory
from domain.user.user import User


class UserRepo:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.__load()

    def add(self, new_user: User):
        self.__users.append(new_user)
        users_info = [(str(x.id), x.username, x.stocks) for x in self.__users]
        users_json = json.dumps(users_info)
        with open(self.file_path, "w") as file:
            file.write(users_json)

    def get_all(self) -> list[User]:
        return self.__users

    def get_by_id(self, id_) -> User:
        for u in self.__users:
            if u.id == id_:
                return u

    def __load(self):
        try:
            with open(self.file_path) as f:
                contents = f.read()
            users_info = json.loads(contents)
            factory = UserFactory()
            self.__users = [factory.make_from_persistance(x) for x in users_info]
        except:
            self.__users = []
