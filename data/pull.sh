wget -c http://www.mpi-sws.org/~cristian/data/cornell_movie_dialogs_corpus.zip
tar -C ./ -xvf cornell_movie_dialogs_corpus.zip --strip-components=1 "cornell movie-dialogs corpus/movie_conversations.txt"
tar -C ./ -xvf cornell_movie_dialogs_corpus.zip --strip-components=1 "cornell movie-dialogs corpus/movie_lines.txt"
rm cornell_movie_dialogs_corpus.zip

