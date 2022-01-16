#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;
static unsigned int c=299792458;

void print(float inner){
    cout<<inner<<endl;
}
void print(string inner){
    cout<<inner<<endl;
}

int main(){

fstream io;
io.open("observer.cw");
unsigned short int dim;
double r_val;
string line;
while(getline(io,line)){
    dim=int(line[0])-48;
}
io.close();
double observer_l[dim+1];
io.open("observer.cw");


while(getline(io,line)){

    unsigned short int commas[dim+2];
    unsigned short int len=line.length();
    commas[dim+1]=len;
    unsigned short int in=0;
    for(unsigned short int i=0;i<len;i++){
        if(line[i]==','){
            commas[in]=i;
            in++;

        }
        
    }
    for(uint8_t i=0;i<dim+1;i++){
      string __="";
      for(uint8_t j=commas[i]+1;j<commas[i+1];j++){
          __+=line[j];
          
      }
      observer_l[i]=stof(__);
    }


}

io.close();


io.open("wave.cw");
while(getline(io,line)){
    
    unsigned short int commas[dim+6];
    unsigned short int len=line.length();
    unsigned short int in=1;
    commas[dim+5]=len;
    for(unsigned short int i=0;i<len;i++){
        if(line[i]==','){
            commas[in]=i;
            in++;
        }
        
    }
         double source_l[dim];
         string __="";
         for(unsigned short int j=0;j<commas[1];j++){
             __+=line[j];
         }
         source_l[0]=stof(__);



     for(unsigned short int i=1;i<dim;i++){
         __="";
         for(unsigned short int j=commas[i]+1;j<commas[i+1];j++){
             __+=line[j];
         }
         source_l[i]=stof(__);
     }


double r=0;
for(unsigned short int c=0;c<dim;c++){
    r+=pow((observer_l[c]-source_l[c]),2);
}
r=sqrt(r);
        double start;
     __="";
    for(unsigned short int xi=commas[dim]+1 ;xi<commas[dim+1];xi++){
        __+=line[xi];
        
    }
    start=stof(__)+r/c;//r+c is delay for propogation
    double end;
     __="";
    for(unsigned short int xi=commas[dim+1]+1 ;xi<commas[dim+2];xi++){
        __+=line[xi];
        
    }
    end=stof(__)+r/c;

 if(start<=observer_l[0]<=end){

unsigned short int i=0;
double wave[3];//amplitude, frequency, phase
for(unsigned short int j=dim+2;j<dim+5;j++){

 string __;
 for(unsigned short int k=commas[j]+1;k<commas[j+1];k++){
    __+=line[k];
 }
 
wave[i]=stof(__);
i++;


}

r_val+=wave[0]*sin(2*M_PIf64*wave[1]*(r/c-observer_l[0])+wave[2]);

 }
     
}

io.close();
fstream res;
res.open("result.cw");

res<<to_string(r_val);
res.close();
return 0;

}
