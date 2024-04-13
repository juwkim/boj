from collections import defaultdict
def solution(genres, plays):
    plays_by_genre, songs_by_genre = defaultdict(int), defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        plays_by_genre[genre] += play
        songs_by_genre[genre].append((i, play))
    answer = []
    for genre in sorted(songs_by_genre, key=lambda x: -plays_by_genre[x]):
        answer.extend([*zip(*sorted(songs_by_genre[genre], key=lambda x: (-x[1], x[0]))[:2])][0])
    return answer