#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    
    unordered_map<string, int> c;
    
    int answer = 1;
    
    for(int i=0; i < clothes.size(); i++){
        c[clothes[i][1]]++;
    }
    
    for(auto x: c){
        answer *= (x.second + 1);
    }
    
    return answer -1;
        
}