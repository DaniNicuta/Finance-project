import unittest
import uuid
from domain.user.factory import UserFactory, InvalidUsername
from domain.user.user import User


class UserFactoryTestCase(unittest.TestCase):
    def test_it_creates_a_user_if_the_username_is_between_6_and_20_chars(self):
        username = "between-6-and-20"
        factory = UserFactory()

        actual_user = factory.make_new(username)

        self.assertEqual(username, actual_user.username)
        self.assertEqual(User, type(actual_user))

    def test_it_raises_exception_if_the_username_is_below_6_chars(self):
        username = "below"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)

        self.assertEqual(
            "Username should have at least 6 characters", str(context.exception)
        )

    # @unittest.skip("TODO")
    def test_it_raises_exception_if_the_username_is_above_20_chars(self):
        username = "thisisalongusernameeee"
        factory = UserFactory()
        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)

        self.assertEqual(
            "Username must be less than 20 characters", str(context.exception)
        )

    # @unittest.skip("TODO")
    def test_it_creates_a_user_if_the_username_has_valid_chars(self):
        username = "this-is-correct"
        factory = UserFactory()
        actual_user = factory.make_new(username)

        self.assertEqual(username, actual_user.username)

    # @unittest.skip("TODO")
    def test_it_raises_exception_if_the_username_has_invalid_chars(self):
        username = "t#is+is(wrong)"
        factory = UserFactory()
        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)
        self.assertEqual(
            "Username must contain letters, numbers and - ", str(context.exception)
        )

    def test_make_from_persistence(self):
        # set up
        factory = UserFactory()
        user_id = uuid.uuid4()
        username = "random-123"
        stocks = ["TSLA", "NVDA", "AMZN"]
        info = (str(user_id), username, stocks)
        # execution
        actual_user = factory.make_from_persistance(info)
        # assertion
        self.assertIsInstance(actual_user, User)
        self.assertEqual(actual_user.id, user_id)
        self.assertEqual(actual_user.username, username)
        self.assertEqual(actual_user.stocks, stocks)


if __name__ == "__main__":
    unittest.main()
