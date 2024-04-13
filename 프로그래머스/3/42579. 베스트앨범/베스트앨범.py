from collections import defaultdict

def solution(genres, plays):
    plays_by_genre = defaultdict(int)
    songs_by_genre = defaultdict(list)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        plays_by_genre[genre] += play
        songs_by_genre[genre].append((i, play))
    answer = []
    for genre in sorted(songs_by_genre, key=lambda x: -plays_by_genre[x]):
        for i, p in sorted(songs_by_genre[genre], key=lambda x: (-x[1], x[0]))[:2]:
            answer.append(i)
    return answer