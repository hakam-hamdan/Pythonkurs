# Film Library Management System (English Version)

import json
import os

DATA_FILE = "movies.json"


def load_data():
    """Load movie library from file if exists."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # JSON keys are strings -> convert to int:
            return {int(k): v for k, v in data.items()}
    except (json.JSONDecodeError, IOError):
        print("Warning: couldn't read JSON file. Starting empty library.")
        return {}


def save_data(movies):
    """Save movie data to JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({str(k): v for k, v in movies.items()}, f, ensure_ascii=False, indent=2)


def generate_id(movies):
    """Generate the next ID for a new movie."""
    if not movies:
        return 1
    return max(movies.keys()) + 1


def parse_genres(s):
    """Convert comma-separated string into list of genres."""
    return [g.strip() for g in s.split(",") if g.strip()]


def add_movie(movies):
    print("\n-- Add a New Movie --")
    title = input("Movie Title: ").strip()
    if not title:
        print("Aborted: title is required.")
        return
    director = input("Director: ").strip()
    year_input = input("Release Year (optional): ").strip()
    year = int(year_input) if year_input.isdigit() else None
    genres_text = input("Genres (comma-separated): ").strip()
    genres = parse_genres(genres_text) if genres_text else []

    new_id = generate_id(movies)
    movies[new_id] = {
        "title": title,
        "director": director,
        "year": year,
        "genres": genres
    }
    save_data(movies)
    print(f"Movie added successfully! ID: {new_id}")


def edit_movie(movies):
    print("\n-- Edit Movie --")
    try:
        mid = int(input("Enter Movie ID: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    if mid not in movies:
        print("No movie found with that ID.")
        return

    movie = movies[mid]
    print("Leave blank to keep the current value.")
    print(f"Current title: {movie['title']}")
    title = input("New Title: ").strip() or movie["title"]
    print(f"Current director: {movie.get('director', '')}")
    director = input("New Director: ").strip() or movie.get("director")
    print(f"Current year: {movie.get('year')}")
    year_input = input("New Year: ").strip()
    year = int(year_input) if year_input.isdigit() else movie.get("year")
    print(f"Current genres: {', '.join(movie.get('genres', []))}")
    genres_text = input("New Genres (comma-separated): ").strip()
    genres = parse_genres(genres_text) if genres_text else movie.get("genres", [])

    movies[mid] = {
        "title": title,
        "director": director,
        "year": year,
        "genres": genres
    }
    save_data(movies)
    print("Movie updated.\n")


def delete_movie(movies):
    print("\n-- Delete Movie --")
    try:
        mid = int(input("Enter Movie ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    if mid not in movies:
        print("Movie not found.")
        return

    confirm = input(f"Are you sure you want to delete '{movies[mid]['title']}'? (y/n): ").strip().lower()
    if confirm == "y":
        del movies[mid]
        save_data(movies)
        print("Movie deleted.")
    else:
        print("Delete cancelled.")


def show_movie(mid, movie):
    year = movie.get("year") or "-"
    genres = ", ".join(movie.get("genres", [])) or "-"
    director = movie.get("director") or "-"
    print(f"[{mid}] {movie['title']} | Director: {director} | Year: {year} | Genres: {genres}")


def list_all(movies):
    print("\n-- All Movies --")
    if not movies:
        print("The library is empty.")
        return
    for mid, movie in sorted(movies.items(), key=lambda x: x[1]['title'].lower()):
        show_movie(mid, movie)


def filter_by_genre(movies):
    print("\n-- Filter by Genre --")
    q = input("Enter genre name or keyword: ").strip().lower()
    if not q:
        print("No input.")
        return
    results = [
        (mid, m) for mid, m in movies.items()
        if any(q in g.lower() for g in m.get("genres", []))
    ]
    if not results:
        print("No movies found for this genre.")
        return
    for mid, movie in sorted(results, key=lambda x: x[1]['title'].lower()):
        show_movie(mid, movie)


def filter_by_year(movies):
    print("\n-- Filter by Year --")
    s = input("Enter a year (e.g. 2010) or a range like 2000-2010: ").strip()
    if not s:
        print("No input.")
        return
    try:
        if "-" in s:
            a, b = s.split("-", 1)
            a, b = int(a), int(b)
            results = [
                (mid, m) for mid, m in movies.items()
                if m.get("year") and a <= m["year"] <= b
            ]
        else:
            y = int(s)
            results = [
                (mid, m) for mid, m in movies.items()
                if m.get("year") == y
            ]
    except ValueError:
        print("Invalid format.")
        return

    if not results:
        print("No movies match the given year.")
        return
    for mid, movie in sorted(results, key=lambda x: x[1]['title'].lower()):
        show_movie(mid, movie)


def main_menu():
    movies = load_data()
    print("Welcome to your Film Library System!")
    while True:
        print("\nMain Menu:")
        print("1. Add Movie")
        print("2. Edit Movie")
        print("3. Delete Movie")
        print("4. View All Movies")
        print("5. Filter by Genre")
        print("6. Filter by Year")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            edit_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            list_all(movies)
        elif choice == "5":
            filter_by_genre(movies)
        elif choice == "6":
            filter_by_year(movies)
        elif choice == "0":
            print("Saving and exiting...")
            save_data(movies)
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main_menu()





   
