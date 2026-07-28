# 주요 정보 : 재생 횟수, 장르, 고유번호
def solution(genres, plays):
    gen_play = {}
    gen_song = {}
    answer = []
    
    for index, (genre, play) in enumerate(zip(genres, plays)):
        gen_play[genre] = gen_play.get(genre, 0) + play
        
        if not genre in gen_song.keys():
            gen_song[genre] = []
            
        gen_song[genre].append((index, play))
        
    for genre, plays in sorted(gen_play.items(), key = lambda x : x[1], reverse=True):
        for index, play in sorted(gen_song[genre], key = lambda x : (-x[1], x[0]))[:2]:
            answer.append(index)
            
    return answer