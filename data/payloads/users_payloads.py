from faker import Faker


faker = Faker()

class UsersPayloads:

    @staticmethod
    def get_random_valid_user():
        return {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name(),
            "nickname": faker.user_name()
        }
