def solution(genres, plays):
    genre_cnt = {}
    genre_song = {}
    answer = []
    
    # 1. 장르를 기준으로 횟수 총합 
    for index, (genre, play) in enumerate(zip(genres, plays)):
        genre_cnt[genre] = genre_cnt.get(genre, 0) + play
        
    # 2. 장르별로 횟수와 고유번호 함께 저장하기 -> 장르에 따른 곡 정보 
        if not genre in genre_song.keys():
            genre_song[genre] = []
            
        # 여기다가 else 넣으면 처음에 []만 추가하고 노래를 추가 안 함
        genre_song[genre].append((index, play))
    
    
    # 3. 적절한 거 가져와서 출력
    sorted_genre = sorted(genre_cnt.items(), key=lambda x: x[1], reverse=True)
    
    for genre, plays in sorted_genre:
        songs = genre_song[genre]
        
        # 우선순위에 맞게 정렬
        songs.sort(key=lambda x: (-x[1], x[0]))

        # 최대 두 곡
        for index, play in songs[:2]:
            answer.append(index)
            
    return answer