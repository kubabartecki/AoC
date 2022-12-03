#include<iostream>
#include<string>
using namespace std;

int main(){
    string s=" ";
    int points = 0;

    getline(cin,s);
    while(s[0] != '\0'){
        points += (s[2] - 87) + ((s[0]-s[2]+1)%3) * -3;
        getline(cin,s);
    }
    cout<<"points: "<<points<<endl;
}