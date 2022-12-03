#include<iostream>
#include<string>
using namespace std;

int main(){
    string s[3];
    int points = 0;

    while(1){
        char typee;

        for(int i = 0; i < 3; i++){
            getline(cin, s[i]);
        }

        if(s[0].length() == 0) break;
    
        for (int i = 0; i < s[0].length(); i++){
            for(int j = 0 ; j< s[1].length(); j++){
                bool f = s[0][i] == s[1][j];
                if(!f)continue;
                for(int k = 0; k < s[2].length(); k++){
                    if(f && s[2][k] == s[1][j]){
                        typee = s[1][j];
                        i = s[0].length()-1;}//to end for loop
                }          
            }
        }

        if(typee > 96){
        points += (typee - 96);}
        else if(typee < 96){
        points += (typee - 38);}//In ASCII 'A'=65 ,now 'A'=27

        //cout<<typee<<endl;
    }
    cout<<"points: "<<points<<endl;
}