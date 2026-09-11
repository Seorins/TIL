#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;

    for(int a : arr){
        if(!answer.empty() && answer.back() == a) continue;
        answer.push_back(a);
    }

    return answer;
}

// ------------------------------------------------------


#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    arr.erase(unique(arr.begin(), arr.end()), arr.end());
    
    return arr;
}