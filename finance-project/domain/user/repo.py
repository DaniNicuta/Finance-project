import json
import uuid
from singleton import singleton
from domain.asset.repo import AssetRepo
from domain.user.factory import UserFactory
from domain.user.persistace_interface import UserPersistenceInterface
from domain.user.user import User


@singleton
class UserRepo:
    def __init__(self, persistence: UserPersistenceInterface):
        print("Init user repo ")
        self.__persistence = persistence
        self.__users = None

    def add(self, new_user: User):
        self.__persistence.add(new_user)
        self.__users = self.__persistence.get_all()

    def get_all(self) -> list[User]:
        self.check_users_not_none()
        return self.__users

    def get_by_id(self, uid: str) -> User:
        self.check_users_not_none()
        for u in self.__users:
            if u.id == uuid.UUID(hex=uid):
                assets = AssetRepo().get_for_user(u)
                return User(uuid=u.id, username=u.username, stocks=assets)

    def check_users_not_none(self):
        if self.__users is None:
            self.__users = self.__persistence.get_all()

    def delete_by_id(self, id_: str):
        self.__users = [u for u in self.__users if str(u.id) != id_]

        # with open(self.file_path) as f:
        #     content = f.read()
        # user_info = json.loads(content)
        #
        # for every_user in user_info:
        #     if every_user[0] == id_:
        #         user_info.remove(every_user)
        #
        # with open(self.file_path, "w") as f:
        #     json.dump(user_info, f)
