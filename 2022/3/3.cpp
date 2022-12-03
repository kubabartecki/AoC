#include<iostream>
#include<string>
using namespace std;

int main(){
    string s=" ";
    int points = 0;

    getline(cin,s);
    while(s[0] != '\0'){
        int dl =s.length();
        int sec = dl/2;
        char typee ;
        for (int i = 0; i < sec; i++){
            for(int j = sec ; j< dl; j++){
                if(s[i] == s[j]){typee = s[i];
                i = sec-1;}
                //to end loop
            }
        }
        
        if(typee > 96){
        points += (typee - 96);}
        
        else if(typee < 96){
        points += (typee - 38);}//In ASCII 'A'=65 ,now 'A'=28
        
        //cout<<typee<<endl;
        getline(cin,s);
    }
    cout<<"points: "<<points<<endl;
}