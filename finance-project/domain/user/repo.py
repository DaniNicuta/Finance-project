import uuid
import logging
from singleton import singleton
from domain.asset.repo import AssetRepo
from domain.user.persistace_interface import UserPersistenceInterface
from domain.user.user import User

logging.basicConfig(
    filename="finance.log",
    level=logging.DEBUG,
    format="%(asctime)s _ %(levelname)s _ %(name)s _ %(message)s",
)


class UserIDNotFound(Exception):
    pass


@singleton
class UserRepo:
    def __init__(self, persistence: UserPersistenceInterface):
        print("Init user repo ")
        self.__persistence = persistence
        self.__users = None

    def add(self, new_user: User):
        self.__persistence.add(new_user)
        self.__users = None
        self.check_users_not_none()
        logging.info(f"The user{new_user.username} was successfully created. ")

    def delete_by_id(self, _id: User.id):
        self.check_users_not_none()
        self.check_id_exists(_id)
        for u in self.__users:
            if _id == u.id:
                self.__users.remove(u)
        self.__persistence.delete_by_id(_id)
        logging.info(f"The user with ID {_id} was deleted successfully!")

    def edit(self, _id: User.id, username: str):
        self.check_users_not_none()
        self.check_id_exists(_id)
        for u in self.__users:
            if _id == u.id:
                u.username = username
        self.__persistence.edit(_id, username)
        logging.info(f"The user with ID {_id} was changed to {username}")

    def get_all(self) -> list[User]:
        self.check_users_not_none()
        return self.__users

    def get_by_username(self, username) -> User:
        self.check_users_not_none()
        for u in self.__users:
            if u.username == username:
                return u

    def get_by_id(self, _id: str) -> User:
        self.check_users_not_none()
        for u in self.__users:
            if u.id == uuid.UUID(hex=_id):
                assets = AssetRepo().get_for_user(u)
                return User(uuid=u.id, username=u.username, stocks=assets)

    def check_users_not_none(self):
        if self.__users is None:
            self.__users = self.__persistence.get_all()

    def check_id_exists(self, _id):
        if str(_id) not in [str(u.id) for u in self.__users]:
            logging.error(msg="The user ID does not exist!")
            raise UserIDNotFound("The user ID does not exist!")
