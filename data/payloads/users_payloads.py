from faker import Faker


faker = Faker()

class UsersPayloads:

    @staticmethod
    def create_user():
        return {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name(),
            "nickname": faker.user_name()
        }
