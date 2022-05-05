MENU_PROMPT= "\n Enter 'a' to add the movie, Enter 'b' to show the movie title, Enter 'c' to find the movies, Enter 'q' to quit the movie :"

movies=[]

def add_movie():
  title= (input("Enter Movie Name :"))
  director= (input("Enter Director Name :"))
  year= (input("Enter released year of the movie :"))

  movies.append({
      'title': title,
      'director': director,
      'year': year
  })

def show_the_movies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"title:{movie['title']}")
    print(f"director:{movie['director']}")
    print(f"year:{movie['year']}")

def find_the_movies():
    search_title=(input("Enter the Movie name you're looking for :"))
    for movie in movies:
        if movie["title"]==search_title:
            print_movie(movie)

def menu():
    selection=(input("MENU_PROMPT"))
    while selection != 'q':
        if selection == "a":
            add_movie()
        elif selection == "b":
            show_the_movies()
        elif selection == "c":
            find_the_movies()
        else:
            print("The given value is error. So please try again!")
        selection = input(MENU_PROMPT)


menu()











