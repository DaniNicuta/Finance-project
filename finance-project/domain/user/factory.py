from domain.user.user import User


class InvalidUsername(Exception):
    pass


class UserFactory:
    # username should be at least 6 chars and max 20 chars, it can only contain letters, numbers & -
    def make(self, username: str) -> User:
        if len(username) < 6:
            raise InvalidUsername("Username should have at least 6 characters")
        elif len(username) > 20:
            raise InvalidUsername("Username must be less than 20 characters")
        elif not username.isalnum() and "-" not in username:
            raise InvalidUsername("Username must contain letters, numbers and - ")
        return User(username)
