#include<iostream>
#include<string>

int main(){

std::string s;
int top  = 3;
int max[3]={0,0,0}, inew = 0; //top value in max on "0" index

while(1){
    std::getline(std::cin, s);
    if(s.length() != 0) inew += stoi(s);
    else{
        if(inew == 0) break;//check end of input

        for(int i = 0; i < top; i++){
            if(inew > max[i]){
                for(int j = top-1; j > i; j--)
                    max[j] = max[j-1];
                
                max[i] = inew;
                break;
            }
        }
        inew = 0;
    }
}
int suma = 0;
for(int i = 0; i < top; i++) suma += max[i];
std::cout<<"Result: "<<max[0]<<" "<<max[1]<<" "<<max[2]<<" "<<"Sum: "<<suma<<std::endl;

}