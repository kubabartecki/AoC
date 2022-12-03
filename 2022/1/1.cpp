#include<iostream>
#include<string>

int main(){

std::string s;
int max=0, tmp = 0;
std::cout<<max;

while(1){
std::getline(std::cin, s);
if(s.length() != 0) tmp += stoi(s);
else{
    if(tmp > max) max = tmp;
    else if(tmp == 0) break;
    tmp = 0;}
}

std::cout<<"Result: "<<max<<std::endl;

}