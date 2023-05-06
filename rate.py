import os
import numpy
import pandas

class Settings:
    def __init__(self, initial_setup=False):
        self.system_path = os.path.dirname(os.path.realpath(__file__))
        self.dataset_dir_path = os.path.join(self.system_path, "datasets")
        self.users_path = os.path.join(self.dataset_dir_path, "users.csv")
        if initial_setup:
            self.initial_setup()
        self.users = pandas.read_csv(self.users_path)
        self.save_after_each_joke = True
        self.set_user_id()
        self.set_ratings()
        self.set_dataset()

    def set_dataset(self):
        flag = True
        while flag:
            print("\nLoad dataset")
            print("------------")
            print("Choose a dataset to load: ")
            print("1. Jester")
            print("2. Reddit")
            print("3. StupidStuff")
            print("4. WockaJokes")
            print("5. Back")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice.isdigit():
                choice = int(choice)
                if choice >= 1 and choice <= 6:
                    flag = False
                if choice == 1:
                    self.dataset_name = "jester"
                    self.dataset = pandas.read_csv(os.path.join(self.dataset_dir_path, "jester_items.csv"))
                    self.dataset_code = 'JE'
                    print("Loading Jester dataset...")
                elif choice == 2:
                    self.dataset_name = "reddit"
                    self.dataset = pandas.read_json(os.path.join(self.dataset_dir_path, "reddit_jokes.json"))
                    self.dataset_code = 'RE'
                    print("Loading Reddit dataset...")
                elif choice == 3:
                    self.dataset_name = "stupidstuff"
                    self.dataset = pandas.read_csv(os.path.join(self.dataset_dir_path, "stupidstuff_shuffled.csv"))
                    self.dataset_code = 'SS'
                    print("Loading StupidStuff dataset...")
                elif choice == 4:
                    self.dataset_name = "wockajokes"
                    self.dataset = pandas.read_json(os.path.join(self.dataset_dir_path, "wocka.json"))
                    self.dataset_code = 'WO'
                    print("Loading WockaJokes dataset...")
                elif choice == 5:
                    return
                elif choice == 6:
                    exit()
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("Invalid choice. Please try again.")

    def set_user_id(self):
        flag = True
        while flag:
            print("\nSet User ID")
            print("-----------")
            print("1. Create new user")
            print("2. Enter existing user")
            print("3. Back")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice.isdigit():
                choice = int(choice)
                if choice >= 1 and choice <= 4:
                    flag = False
                if choice == 1:
                    self.user_id = self.create_user()
                elif choice == 2:
                    print("Enter your user id or name: ")
                    user = input()
                    if user in self.users['user_id'].values or user.lower() in self.users['name'].str.lower().values:
                        if user.startswith('USF'):
                            self.user_id = user
                        else:
                            self.user_id = self.users.loc[self.users['name'].str.lower() == user.lower()]['user_id'].values[0]
                        print(f"User id set to {self.user_id}.")
                    else:
                        flag = True
                        print("User id does not exist. Please try again.")
                elif choice == 3:
                    return
                elif choice == 4:
                    exit()
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("Invalid choice. Please try again.")

    def set_ratings(self):
        self.ratings_path = os.path.join(self.dataset_dir_path, f"ratings_{self.user_id}.csv")
        self.ratings = pandas.read_csv(self.ratings_path)

    def get_dataset(self):
        return self.dataset

    def get_user_id(self):
        return self.user_id

    def get_dataset_code(self):
        return self.dataset_code

    def create_user(self):
        print("\nCreate user")
        print("-----------")
        print("Enter your name: ")
        name = input()
        print("Enter your age: ")
        age = input()
        print("Enter your gender: ")
        gender = input()
        print("Enter your ethnicity: ")
        ethnicity = input()
        print("Enter your country: ")
        country = input()
        print("Enter your location: ")
        location = input()
        print("Creating user...")

        user_id = f"USF{str(self.users.shape[0] + 1000)}"
        new_user_row  = {'user_id': user_id, 'name': name, 'age': age, 'gender': gender, 'ethnicity': ethnicity, 'country': country, 'location': location}
        self.users = self.users.append(new_user_row, ignore_index=True)
        self.users.to_csv(self.users_path, index=False)

        print(f"User created successfully! Setting the current user to {name}.")
        print(f"Your user id is: {user_id}")

        self.ratings_path = os.path.join(self.dataset_dir_path, f"ratings_{user_id}.csv")
        self.ratings = pandas.DataFrame(columns=['joke_id', 'user_id', 'rating'])
        self.ratings.to_csv(self.ratings_path, index=False)

        return user_id

    def initial_setup(self):
        """
        This function is called initially to setup the program.

        It checks if the files "ratings.csv" and "users.csv" exist in the dataset directory.
        If they do not exist, it will create them. Columns in the ratings.csv file are
        'joke_id', 'user_id', 'rating'. Columns in the users.csv file are 'user_id', 'name'.
        """
        if not os.path.exists(self.dataset_dir_path):
            os.mkdir(self.dataset_dir_path)

        if not os.path.exists(self.users_path):
            self.users = pandas.DataFrame(columns=['user_id', 'name', 'age', 'gender', 'ethnicity', 'country', 'location'])
            self.users.to_csv(self.users_path, index=False)
            self.create_user()

    def change_settings(self):
        flag = True
        while flag:
            print("\nChange settings")
            print("---------------")
            print("1. Change dataset")
            print("2. Change user id")
            print("3. Save settings")
            print("4. Back")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice.isdigit():
                choice = int(choice)
                if choice >= 1 and choice <= 5:
                    flag = False
                if choice == 1:
                    self.set_dataset()
                elif choice == 2:
                    self.set_user_id()
                elif choice == 3:
                    print("Change saving settings...")
                    print("1. Save ratings after each joke")
                    print("2. Save ratings after each session")
                    saving_choice = int(input("Enter your choice: "))
                    if saving_choice == 1:
                        self.save_after_each_joke = True
                        print("Saving settings changed to save after each joke.")
                    elif saving_choice == 2:
                        self.save_after_each_joke = False
                        print("Saving settings changed to save after each session.")
                    else:
                        print("Invalid choice. Please try again.")
                        return
                elif choice == 4:
                    return
                elif choice == 5:
                    exit()
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("Invalid choice. Please try again.")

    def save_ratings(self):
        """
        This function is used to save the ratings in the ratings dataframe to the
        ratings.csv file.
        """
        self.ratings.to_csv(self.ratings_path, index=False)

    def change_rating(self, id):
        """
        This function is used to change the rating of a joke.
        """
        if id in self.ratings['joke_id'].values:
            print("Enter new rating: ")
            rating = input()
            self.ratings.loc[self.ratings['joke_id'] == id, 'rating'] = rating
            print("Rating changed successfully!")
            self.save_ratings()
        else:
            print("Joke id not found in ratings.")


def get_unrated_jokes(dataset, user_id, ratings, dataset_code):
    """
    This function is used to get the list of jokes that have not been rated by the user.
    """
    joke_column_name = 'id' if 'id' in dataset.columns else 'jokeId'
    user_ratings = ratings[ratings['user_id'] == user_id]
    ratings_id_set = set(user_ratings['joke_id'])
    unrated_jokes = dataset.copy()
    unrated_jokes['joke_id'] = dataset_code + unrated_jokes[joke_column_name].astype(str)
    unrated_jokes = unrated_jokes[~unrated_jokes['joke_id'].isin(ratings_id_set)]
    unrated_jokes.drop(columns=['joke_id'], inplace=True)
    return unrated_jokes

def rate_jokes(settings):
    """
    This function is used to rate jokes.

    It checks the ratings.csv file to see if the user has already rated the joke.
    It finds the joke in the dataset that has not been rated by the user. It then
    displays the joke to the user and asks them to rate it. The user can rate the
    joke from 1 to 10. The user can also choose to skip the joke by entering 's'
    or 'S'. If the user chooses to skip the joke, the joke is not rated and the
    program moves on to the next joke. If the user chooses to rate the joke, the
    rating is saved in the ratings.csv file. The program then moves on to the next
    joke until the user stops rating by entering 'q' or 'Q', or until all jokes
    have been rated.
    """
    dataset_code = settings.get_dataset_code()
    unrated_jokes = get_unrated_jokes(settings.get_dataset(), settings.get_user_id(), settings.ratings, dataset_code)
    if len(unrated_jokes) == 0:
        print("You have already rated all the jokes.")
        return
    for index, row in unrated_jokes.iterrows():
        joke_id = row['id'] if 'id' in row else row['jokeId']
        dataset_joke_id = f"{dataset_code}{joke_id}"
        print(f"Joke {joke_id} : {dataset_joke_id}")
        if 'title' in row.index and row['title'] != '':
            print(row['title'])
        if 'category' in row.index and row['category'] != '':
            print(f"Category: {row['category']}")
        if 'body' in row.index and row['body'] != '':
            print(row['body'])
        if 'jokeText' in row.index and row['jokeText'] != '':
            print(row['jokeText'])
        print("Rate this joke from 0 to 10. Enter 's' to skip or 'q' to quit.")
        rating_flag = True
        while rating_flag:
            rating = input()
            if rating == 's' or rating == 'S':
                rating_flag = False
                continue
            elif rating == 'q' or rating == 'Q':
                settings.save_ratings()
                rating_flag = False
                break
            elif rating.isdigit() and int(rating) >= 0 and int(rating) <= 10:
                new_rating_row = {'joke_id': dataset_joke_id, 'user_id': settings.get_user_id(), 'rating': rating}
                settings.ratings = settings.ratings.append(new_rating_row, ignore_index=True)
                print("Rating added.")
                if settings.save_after_each_joke:
                    settings.save_ratings()
                    print("Rating saved successfully!")
                rating_flag = False
            else:
                print("Invalid rating. Please try again. ")
                continue
        if rating == 'q' or rating == 'Q':
            break
    settings.save_ratings()
    print("You have finished rating jokes.")

def display_menu():
    print("\nSelect an option from the menu below: ")
    print("1. Rate jokes")
    print("2. Change settings")
    print("3. Change rating")
    print("4. Exit")

def main():
    settings = Settings()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                rate_jokes(settings)
            elif choice == 2:
                settings.change_settings()
            elif choice == 3:
                print("Enter joke id: ")
                id = input()
                settings.change_rating(id)
            elif choice == 4:
                exit()
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
