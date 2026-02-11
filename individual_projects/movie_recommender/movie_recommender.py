import csv

MOVIE_FILE = "individual_projects/movie_recommender/movies_list.csv"


def load_movies(filename):
    movies = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    movie = {
                        "title": row["Title"].strip(),
                        "director": row["Director"].strip().lower(),
                        "genres": [g.strip().lower() for g in row["Genre"].split("/")],
                        "rating": row["Rating"].strip(),
                        "length": int(row["Length (min)"]),
                        "actors": [a.strip().lower() for a in row["Notable Actors"].split(",")]
                    }
                    movies.append(movie)
                except:
                    # Skip weird rows
                    continue

    except FileNotFoundError:
        print("ERROR: movie_list.csv not found.")
        return []

    return movies


def filter_by_genre(movies, genre):
    genre = genre.lower().strip()
    return [m for m in movies if any(genre in g for g in m["genres"])]


def filter_by_director(movies, director):
    director = director.lower().strip()
    return [m for m in movies if director in m["director"]]


def filter_by_actor(movies, actor):
    actor = actor.lower().strip()
    return [m for m in movies if any(actor in a for a in m["actors"])]


def filter_by_length(movies, min_len=None, max_len=None):
    results = []

    for m in movies:
        if min_len is not None and m["length"] < min_len:
            continue
        if max_len is not None and m["length"] > max_len:
            continue
        results.append(m)

    return results


def apply_filters(movies, filters):
    results = movies
    for f in filters:
        results = f(results)
    return results


def print_movies(movies):
    if not movies:
        print("No movies match those filters. Try removing one filter or widening the length range.\n")
        return

    print("\nResults:\n")
    for m in movies:
        print(
            f'Title: "{m["title"]}" — '
            f'Genres: {"|".join(m["genres"]).title()} — '
            f'Director: {m["director"].title()} — '
            f'Actors: {", ".join(m["actors"]).title()} — '
            f'Length: {m["length"]} min'
        )
    print()


def print_full_list(movies):
    print_movies(movies)


def main():
    movies = load_movies(MOVIE_FILE)

    print("Welcome to the Movie Recommender!")
    print("Search for movies using one or more filters.\n")

    while True:
        print("MAIN MENU:")
        print("1. Search / Get Recommendations")
        print("2. Print Full Movie List")
        print("3. Exit\n")

        choice = input("Type the number for the action you would like to perform: ").strip()
        print()

        if choice == "1":
            filters = []

            print("Choose filters to apply (enter numbers separated by commas, e.g., 1,3):")
            print("1. Genre")
            print("2. Director")
            print("3. Actor")
            print("4. Length (min/max)\n")

            selections = input("Selected filters: ").split(",")

            for s in selections:
                s = s.strip()

                if s == "1":
                    genre = input("Enter genre (e.g., 'Sci-Fi'): ")
                    filters.append(lambda m, g=genre: filter_by_genre(m, g))

                elif s == "2":
                    director = input("Enter director name: ")
                    filters.append(lambda m, d=director: filter_by_director(m, d))

                elif s == "3":
                    actor = input("Enter actor name: ")
                    filters.append(lambda m, a=actor: filter_by_actor(m, a))

                elif s == "4":
                    min_len = input("Enter minimum length in minutes (or leave blank): ").strip()
                    max_len = input("Enter maximum length in minutes (or leave blank): ").strip()

                    min_len = int(min_len) if min_len.isdigit() else None
                    max_len = int(max_len) if max_len.isdigit() else None

                    filters.append(lambda m, mn=min_len, mx=max_len: filter_by_length(m, mn, mx))

            results = apply_filters(movies, filters)
            print_movies(results)

        elif choice == "2":
            print_full_list(movies)

        elif choice == "3":
            print("Thanks for using the best Movie Recommender...")
            break

        else:
            print("Invalid option. Please try again.\n")


main()
