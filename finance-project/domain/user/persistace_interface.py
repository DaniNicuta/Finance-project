import abc

from domain.user.user import User


class UserPersistenceInterface(abc.ABC):
    @abc.abstractmethod
    def add(self, user: User):
        pass

    @abc.abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abc.abstractmethod
    def delete(self, uuid: int):
        pass

    @abc.abstractmethod
    def edit(self, user: User):
        pass


# TODO Homework, delete & edit
