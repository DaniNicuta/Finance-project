import json
import uuid
import logging

from domain.user.factory import UserFactory
from domain.user.persistace_interface import UserPersistenceInterface
from domain.user.user import User

logging.basicConfig(
    filename="finance.log",
    level=logging.DEBUG,
    format="%(asctime)s _ %(levelname)s _ %(name)s _ %(message)s",
)


class FailedToWriteInPersistence(Exception):
    pass


class UserPersistenceFile(UserPersistenceInterface):
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_all(self) -> list[User]:
        try:
            with open(self.__file_path) as f:
                contents = f.read()
            users_info = json.loads(contents)
            factory = UserFactory()
            return [factory.make_from_persistance(x) for x in users_info]
        except FailedToWriteInPersistence as e:
            logging.error("Could not read file: " + str(e))
            return e

    def add(self, user: User):
        current_users = self.get_all()
        current_users.append(user)
        users_info = [(str(x.id), x.username, x.stocks) for x in current_users]
        users_json = json.dumps(users_info)
        try:
            with open(self.__file_path, "w") as file:
                file.write(users_json)
        except FailedToWriteInPersistence as e:
            logging.error("Could not write user info to persistence. Error: " + str(e))
            raise e

    def delete_by_id(self, _id: str):
        current_users = self.get_all()
        updated_users_list = [u for u in current_users if u.id != uuid.UUID(hex=_id)]
        users_info = [(str(u.id), u.username, u.stocks) for u in updated_users_list]
        json_current_users = json.dumps(users_info)
        try:
            with open(self.__file_path, "w") as f:
                f.write(json_current_users)
        except FailedToWriteInPersistence as e:
            logging.error("Could not write user info to persistence. Error: " + str(e))
            raise e

    def edit(self, _id: User.id, username: str):
        current_users = self.get_all()
        for user in current_users:
            if _id == uuid.UUID(hex=_id):
                user.username = username
            users_info = [(str(u.id), u.username, u.stocks) for u in current_users]
            users_json = json.dumps(users_info)
            try:
                with open(self.__file_path, "w") as f:
                    f.write(users_json)
            except FailedToWriteInPersistence as e:
                logging.error(
                    "Could not write user info to persistence. Error: " + str(e)
                )
                raise e
