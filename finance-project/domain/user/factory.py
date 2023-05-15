from domain.user.user import User
import uuid


class InvalidUsername(Exception):
    pass


class UserFactory:
    def make_new(self, username: str) -> User:
        if len(username) < 6:
            raise InvalidUsername("Username should have at least 6 characters")
        elif len(username) > 20:
            raise InvalidUsername("Username must be less than 20 characters")
        elif not username.isalnum() and "-" not in username:
            raise InvalidUsername("Username must contain letters, numbers and - ")
        user_uuid = uuid.uuid4()
        return User(user_uuid, username)

    @classmethod
    def make_from_persistence(cls, info: tuple) -> User:
        return User(
            uuid=uuid.UUID(info[0]),
            username=info[1],
        )
