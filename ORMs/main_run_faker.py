from faker_inject import FakerModels

def main():

    run_faker = FakerModels()

    rounds = 20

    for i in range(rounds):

        run_faker.fake_user_inject()
        run_faker.fake_car_inject()
        run_faker.fake_address_inject()

    print(f"The faker generated {rounds} rounds of Users, Cars and Address ")

if __name__ == "__main__":
    main()

