#include<string>
#include<vector>

using namespace std;

bool solution(string st)
{   
    vector<char> stack;
    
    for(char s:st){
        if(s == '('){
            stack.push_back(s);
        }else{
            if(stack.empty()) return false;
            stack.pop_back();
        }
    } return stack.empty();
}


// -------------------------------------------------


#include<string>

using namespace std;

bool solution(string st)
{   
    int cnt = 0;
    
    for(char s:st){
        if(s == '('){
            cnt++;
        }else{
            if(cnt == 0) return false;
            cnt--;
        }
    } return cnt == 0;
}