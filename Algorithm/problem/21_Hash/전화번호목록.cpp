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