#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

bool solution(vector<string> phone_book) {
    
    unordered_set<string> numbers(phone_book.begin(), phone_book.end());
    
    for (string number : phone_book) {
        string temp = "";
        
        for (int i = 0; i < number.size()-1; i++) {
            temp += number[i];
            
            if (numbers.find(temp) != numbers.end()) {
                return false;
            }
        }
    }
    
    return true;
}


// -------------------------------------------------------------------

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    
    sort(phone_book.begin(), phone_book.end());
        
    for(int i = 0; i < phone_book.size()-1; i++){
        if(phone_book[i] == phone_book[i+1].substr(0, phone_book[i].size())){
            return false;
        }
    } return true;
    
}