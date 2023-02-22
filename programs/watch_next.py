import spacy
nlp = spacy.load("en_core_web_md")

last_desc = nlp ("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

def watch_next (last_desc):
    movie_name = []
    movie_desc = []
    max_similarity = 0
    best_match = ""

    with open("movies.txt", "r") as m:
        for line in m:
            movie = line.split(":") #easier to store both parts together
            name = movie[0].strip()
            desc = nlp(movie[1].strip("\n"))
            #can be done using loop, more efficient to assign vars
            movie_name.append(name)
            movie_desc.append(desc)
            similarity = last_desc.similarity(desc)

            #check if similarity > current most similar desc
            #if not, become max_similar and best_match
            if similarity > max_similarity:
                max_similarity = similarity
                best_match = name

    print(f"The best match for the last movie is: {best_match}")

watch_next(last_desc)
#expected output: movie c
