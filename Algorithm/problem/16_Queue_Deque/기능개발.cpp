#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days;
    
    for(int i = 0; i < progresses.size(); i++){
        days.push_back(ceil((100.0-progresses[i])/speeds[i]));
    }
    
    int cnt = 0;
    int idx = 0;
    
    for(int i = 0; i < days.size(); i++){
        if(days[i] <= days[idx]){
            cnt += 1;
            continue;
        }
        answer.push_back(cnt);
        cnt = 1;
        idx = i;
    }
    answer.push_back(cnt);
    
    return answer;
}