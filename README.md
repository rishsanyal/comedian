# Project: Comedian

## Table of Contents
1. [Description](#description)
2. [Developers](#developers)
3. [Rating Jokes](#rating-jokes)
4. [Dataset](#dataset)


## Description
This project builds a joke recommendation system based on a dataset of English plaintext jokes built upon 2 majors paths:
1. User and their demographics based collaborative filtering.
2. Finding a humor best friend based on the jokes they like and using their humor to recommend jokes.

The dataset is described below in the [Dataset](#dataset) section.

To check out the work done, checkout the file `final.ipynb` for a one-stop workflow of the 5 steps performed in the project. The steps are described below alog with the files that contain the exploratory analysis and the code for the steps that ca be checked out individually for a better understanding of the work done.

1. Step 1: Generate Summary points of Jokes  (File: `step-1.ipynb`)
2. Step 2: Calculate features per demographic (File: `step-2.ipynb`)
3. Step 3: Get User's Humor Buddy (File: `step-3.ipynb`)
4. Step 4: Run the model for each demographic (File: `step-4.ipynb`)
5. Step 5: Run the model for according to their traits and buddy traits. (File: `step-5.ipynb`)

Finally predict jokes.

## Rating Jokes
The jokes are rated on a scale of 1 to 5. The rating is based on the joke's humor. The rating is not based on the joke's grammar, spelling, or any other aspect of the joke other than its humor. 

If you wish to rate jokes, you can use our CLI based program to rate jokes. You can find the source code of the program i the file `rate.py`. To run the program, you can use the following command:
```bash
python rate.py
```

Consequetly, the user goes through a menu driven program which takes you to set you up as a ew user or log into the system with your name or ID. Then, you can choose a specific dataset you would like to rate your jokes on. All your ratings will be saved in the `datasets` directory in the file `ratings_<your ID>.csv`. It is recommended that you rate at least 300 jokes to get a good recommendation. 

## Dataset
All datasets are stored in the `datasets` directory. The dataset is described below.

### 1. A dataset of English plaintext jokes

There are about 208 000 jokes in this database scraped from three sources.

I make no claim on ownership of these files, nor do I necessarily endorse the jokes in them. This dataset is provided for research purposes (see License section below).

This repository was archived in December 2022 and receives no further support.


#### Files
Currently the dataset contains jokes from three sources, each in a different file.

```
----------------------------------------------
reddit_jokes.json |  195K jokes | 7.40M tokens
stupidstuff.json  | 3.77K jokes |  396K tokens
wocka.json        | 10.0K jokes | 1.11M tokens
----------------------------------------------
TOTAL             |  208K jokes | 8.91M tokens
----------------------------------------------
```

#### Format
Each file is a JSON document, containing a flat list of joke objects. Each joke object always has the `body` field with additional fields varying based on the dataset, described below.

Obviously they are not all funny; to find the best ones, sort on the relevant additional fields.

Note that the title is in part of the joke many cases (especially for Reddit submissions).

#### reddit_jokes.json
Scraped from [/r/jokes](https://www.reddit.com/r/jokes). Contains all submissions to the subreddit as of 13.02.2017.

These jokes may have additional comments in them ([example](https://www.reddit.com/r/Jokes/comments/5k9tgu/this_is_the_dirty_joke_my_85yo_grandad_told_to/)).

Additional fields:

* `id` -- submission ID in the subreddit.
* `score` -- post score displayed on Reddit.
* `title` -- title of the submission.

```json
{
        "title": "My boss said to me, \"you're the worst train driver ever. How many have you derailed this year?\"",
        "body": "I said, \"I'm not sure; it's hard to keep track.\"",
        "id": "5tyytx",
        "score": 3
    }
```

#### stupidstuff.json
Scraped from [stupidstuff.org](http://stupidstuff.org/jokes/).

Additional fields:

* `id` -- page ID on stupidstuff.org.
* `category` -- see available categories [here](http://stupidstuff.org/jokes/category.htm).
* `rating` -- mean user rating on a scale of 1 to 5.

```json
{
        "category": "Blonde Jokes",
        "body": "A blonde is walking down the street with her blouse open, exposing one of her breasts. A nearby policeman approaches her and remarks, \"Ma'am, are you aware that I could cite you for indecent exposure?\" \"Why, officer?\" asks the blonde. \"Because your blouse is open and your breast is exposed.\" \"Oh my goodness,\" exclaims the blonde, \"I must have left my baby on the bus!\"",
        "id": 14,
        "rating": 3.5
    }
```


#### wocka.json
Scraped from [wocka.com](http://wocka.com/).

Additional fields:

* `id` -- page ID on wocka.com.
* `category` -- see available categories [here](http://www.wocka.com/).
* `title` -- title of the joke.

```json
{
        "title": "Infants vs Adults",
        "body": "Do infants enjoy infancy as much as adults enjoy adultery?",
        "category": "One Liners",
        "id": 17
    }
```

### 2. User Ratings
The user ratings are stored in the `datasets` directory in the file `ratings_<user ID>.csv`. The file contains the ratings of all the users in the following format:
```
joke_id, user_id, rating
```
The `joke_id` is a unique identifier for each joke with first two letters indicating the source of the joke. The `user_id` is a unique identifier for each user. The `rating` is the rating of the joke by the user. The rating is on a scale of 1 to 10. The rating is based on the joke's humor. The rating is not based on the joke's grammar, spelling, or any other aspect of the joke other than its humor.

### 3. User Demographics
The user information including their demographics is stored in the `datasets` directory in the file `users.csv`. The file contains the information of all the users in the following format:
```
user_id, name, age, gender, ethnicity, country, location, avg_user_rating, city, buddy
```


## License
This dataset is provided for research purposes and makes no ownership claim on any part of it. The question of copyright in the case of jokes is unclear and it is recommended to not using the dataset commercially.

For removal of copyrighted content, please contact me on GitHub.

## Citing
If you use the dataset of English plaintext jokes in academic work, please cite as follows:

```bibtex
@misc{pungas,
        title={A dataset of English plaintext jokes.},
        url={https://github.com/taivop/joke-dataset},
        author={Pungas, Taivo},
        year={2017},
        publisher = {GitHub},
        journal = {GitHub repository}
}
```
