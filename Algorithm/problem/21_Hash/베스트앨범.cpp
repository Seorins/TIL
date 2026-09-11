#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    
    unordered_map<string, int> gen_plays;
    unordered_map<string, vector<pair<int, int>>> gen_songs;
    
    for(int i = 0; i < genres.size(); i++){
        gen_plays[genres[i]] += plays[i];    
        gen_songs[genres[i]].push_back({plays[i], i});    
    }
    
    vector<pair<string, int>> gen_order;
    
    for (auto& [genre, total] : gen_plays){
        gen_order.push_back({genre, total});
    }
    
    sort(gen_order.begin(), gen_order.end(), 
         [](const pair<string, int>& a, const pair<string, int>& b){
             return a.second > b.second;
         });
    
    for(auto& [genre, total] : gen_order){
        vector<pair<int, int>>& songs = gen_songs[genre];
        
        sort(songs.begin(), songs.end(), 
            [](const pair<int, int>& a, const pair<int, int>& b){
                if(a.first == b.first){
                    return a.second < b.second;
                }
                return a.first > b.first;
            });
        
        for(int i = 0; i < songs.size() && i < 2; i++){
            answer.push_back(songs[i].second);
        }
    }
    return answer;
}