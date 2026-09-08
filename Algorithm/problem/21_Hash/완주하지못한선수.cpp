// hash

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    
    unordered_map<string, int> count;
    
    for (string p:participant) count[p]++;
    for (string c:completion) count[c]--;
    for (auto x:count){
        if (x.second != 0) return x.first;
    } return "";
} 

// ------------------------------------------------------

// sort

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    for (int i = 0; i < completion.size(); i++){
        if (participant[i] != completion[i]) return participant[i];
    } return participant[participant.size()-1];
}


