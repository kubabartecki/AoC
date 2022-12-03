#include<iostream>
#include<string>
//#include<bits/stdc++.h>
#include<map>

using namespace std;

int main(){
    string s=" ";
    int points = 0;
    map<char,int> sec, fir;
    map<int,int> res;
    
    sec = {{'X',1},
            {'Y',2},
            {'Z',3}};

    fir = {{'A',1},
            {'B',2},
            {'C',3}};
    
    res = {{-1,6},
            {0,3},
            {1,0},
            {-2,0},
            {2,6}};

    getline(cin,s); 
    while(s[0] != '\0'){
        points += res[ fir[s[0]] - sec[s[2]] ];
        points += sec[s[2]];
        getline(cin,s);
    }
    cout<<"points: "<<points<<endl;
}