# Importing spacy and loading model.
import spacy
nlp = spacy.load("en_core_web_md")

# Defining function to get suggested movie after entering a movie description.
def watch_next(movie_description):
    hulk_nlp = nlp(movie_description)

    # Opening movies.txt and converting to list using readlines.
    with open("movies.txt", "r") as file:
        movies_data = file.readlines()

    # Creating list of similarity score.
    similarity_list = []
    for desc in movies_data:
        similarity_list.append(nlp(desc).similarity(hulk_nlp))

    # Creating dictionary with movie description data, and similarity score.
    movies_dict = {movies_data[i]: similarity_list[i] for i in range(len(movies_data))}

    # Printing the movie with max similarity score.
    print(f"You should watch : {(max(movies_dict, key=movies_dict.get))}")


# Variable with hulk movie description.
planet_hulk_description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

# Calling function.
watch_next(planet_hulk_description)