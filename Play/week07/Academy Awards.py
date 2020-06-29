def academy_awards(alist):
    movies = {}

    for i in alist:
        movies[i[1]] = movies.get(i[1], 0) + 1

    return movies

print(academy_awards([('Best Picture', 'Moonlight'), ('Best Director', 'La La Land'), ('Best Actor', 'Manchester by the Sea'), ('Best Actress', 'La La Land'), ('Best Supporting Actor', 'Moonlight'), ('Best Supporting Actress', 'Fences'), ('Best Original Screenplay', 'Manchester by the Sea'), ('Best Original Score', 'La La Land')]))