
def input_int(prompt):
    while True:
        user_input = input(prompt)
        try:
            num = int(user_input)
            if num >= 1:
                return num
            else:
                print("Please enter a number >= 1.")
        except ValueError:
            print("Please enter a valid integer.")

def input_something(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Please enter something (not just whitespace).")

# Initial movie data
movies = [
    {"name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"]},
    {"name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action", "Adventure", "Drama"]},
    {"name": "Back to the Future", "year": 1985, "duration": 114, "genres": ["Adventure", "Comedy", "Sci-Fi"]}
]

print("Welcome to the Movie Admin CLI!")

while True:
    print("Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")
    choice = input("Enter your choice: ").lower().strip()
    
    if choice == 'a':
        # Add movie
        name = input_something("Enter movie name: ")
        year = input_int("Enter release year: ")
        duration = input_int("Enter duration in minutes: ")
        
        # Handle genres
        genres = []
        while not genres:
            genre_input = input_something("Enter genres (comma-separated): ")
            genres = [g.strip() for g in genre_input.split(',')]
            genres = [g for g in genres if g]  # Remove empty strings
            if not genres:
                print("Please enter at least one genre.")
        
        movie = {"name": name, "year": year, "duration": duration, "genres": genres}
        movies.append(movie)
        print(f"Added '{name}' to the list.")
        
    elif choice == 'l':
        # List all movies
        if not movies:
            print("No movies saved.")
        else:
            for i, movie in enumerate(movies, 1):
                print(f"{i}) {movie['name']} ({movie['year']})")
                
    elif choice == 's':
        # Search movies
        if not movies:
            print("No movies saved.")
        else:
            search_term = input_something("Enter search term: ")
            found = False
            for i, movie in enumerate(movies, 1):
                if search_term.lower() in movie['name'].lower():
                    print(f"{i}) {movie['name']} ({movie['year']})")
                    found = True
            if not found:
                print("No movies found matching that search term.")
                
    elif choice == 'v':
        # View movie
        if not movies:
            print("No movies saved.")
        else:
            index = input_int("Enter movie number: ") - 1
            if 0 <= index < len(movies):
                movie = movies[index]
                genres_str = ", ".join(movie['genres'])
                print(f"Name: {movie['name']}")
                print(f"Year: {movie['year']}")
                print(f"Duration: {movie['duration']} minutes")
                print(f"Genres: {genres_str}")
            else:
                print("Invalid index number.")
                
    elif choice == 'd':
        # Delete movie
        if not movies:
            print("No movies saved.")
        else:
            index = input_int("Enter movie number to delete: ") -1
            if 0 <= index < len(movies):
                movie = movies.pop(index)
                print(f"Deleted '{movie['name']}'.")
            else:
                print("Invalid index number.")
                
    elif choice == 'q':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice.")