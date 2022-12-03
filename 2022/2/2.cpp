#include<iostream>
#include<string>
using namespace std;

int main(){
    string s=" ";
    int points = 0;
    while(s.length()!=0){
        getline(cin,s);
        switch(s[0]){
            case 'A':{
                if(s[2]=='X'){
                    points+=(3+1);
                }
                else if(s[2]=='Y'){
                    points+=(6+2);
                }
                else if(s[2]=='Z'){
                    points+=(0+3);
                }
                break;
            }
            case 'B':{
                if(s[2]=='X'){
                    points+=(0+1);
                }
                else if(s[2]=='Y'){
                    points+=(3+2);
                }
                else if(s[2]=='Z'){
                    points+=(6+3);
                }
                break;
            }
            case 'C':{
                if(s[2]=='X'){
                    points+=(6+1);
                }
                else if(s[2]=='Y'){
                    points+=(0+2);
                }
                else if(s[2]=='Z'){
                    points+=(3+3);
                }
                break;
            }
            default: break;
        }
    }
    cout<<"points: "<<points<<endl;
}