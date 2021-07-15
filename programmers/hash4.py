# 프로그래머스 # hash  #'베스트앨범'

def solution(genres, plays):
    answer = []
    genres_dict = {}
    for genre, play in zip(genres, plays) :
        if genre in genres_dict :
            genres_dict[genre] += play
        else :
            genres_dict[genre] = play
    
    # max_genre
    genre_lst = list(zip(genres_dict.keys(), genres_dict.values()))
    genre_lst.sort(key = lambda x : x[1] , reverse=True)
    print(genre_lst) #[('pop', 3100), ('classic', 1450)]

    for genre in genre_lst : # pop -> classic
        idx_lst = []
        for i, (this_genre, play) in enumerate(zip(genres,plays)):
            if genre[0] == this_genre :
                idx_lst.append([i,play]) #{1:500}
        idx_lst.sort(key = lambda x : x[1], reverse=True)
        
        for i in range(len(idx_lst)):
            if i == 2:
                break
            answer.append(idx_lst[i][0])


    return answer


genres = ["classic", "pop", "classic", "classic", "pop", "jpop"]
# ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500, 4000]
# [500, 600, 150, 800, 2500]

print(solution(genres, plays))