#include<fstream>
#include<cmath>
#include<string>
using namespace std;
static float c=299792458;
static double PI_2M=2*M_PI;

int main()
{
    fstream io;
    string read;

    io.open("MemoriesWillNeverFade/meta.wm");
    getline(io,read);
    static uint8_t dim=stoi(read);
    getline(io,read);
    static uint32_t n_glimmers=stoi(read);
    getline(io,read);
    double t=stod(read);
    getline(io,read);
    static uint32_t n_observers=stoi(read);
    io.close();

    double wave_info[n_glimmers][3];//amplitude, frequency, phase


    io.open("MemoriesWillNeverFade/amplitudes.wm");
    for(uint32_t i=0;i<n_glimmers;i++)
    {
        getline(io,read);
        wave_info[i][0]=stod(read);
    }
     io.close();

    io.open("MemoriesWillNeverFade/frequencies.wm");
    for(uint32_t i=0;i<n_glimmers;i++)
    {
        getline(io,read);
        wave_info[i][1]=stod(read);
    }
     io.close();

    io.open("MemoriesWillNeverFade/phases.wm");
    for(uint32_t i=0;i<n_glimmers;i++)
    {
        getline(io,read);
        wave_info[i][2]=stod(read);
    }
     io.close();

    double sources[n_glimmers][dim];
    uint32_t __=dim+1;

    io.open("MemoriesWillNeverFade/locations.wm");
    for(uint32_t i=0;i<n_glimmers;i++)
    {
        getline(io,read);
        int16_t commas[__];
        
        commas[0]=-1;
        commas[dim]=read.length();
        uint32_t d=1;
        uint32_t j=0;

        while(d<dim)
        {
            if(read[j]==',')
            {
                commas[d]=j;
                
                d++;
            }
            j++;
        }
       
       for(int k=0;k<dim;k++)
       {
           sources[i][k]=stod(read.substr(commas[k]+1,commas[k+1]));
 
       }
    }
    io.close();

    double observers[n_observers][dim];
    
    io.open("MemoriesWillNeverFade/observers.wm");
    for(uint32_t i=0;i<n_observers;i++)
    {
        getline(io,read);
        int16_t commas[__];
        commas[0]=-1;
        commas[dim]=read.length();
        uint32_t d=1;
        uint32_t j=0;

        while(d<dim)
        {
            if(read[j]==',')
            {
                commas[d]=j;
                
                d++;
            }
            j++;
        }
       
       for(int k=0;k<dim;k++)
       {
            observers[i][k]=stod(read.substr(commas[k]+1,commas[k+1]));
       }
 
    }
    io.close();

    double results[n_observers];

    for(uint32_t i=0;i<n_observers;i++)
    {   
        double tmp=0;
        for(uint32_t j=0;j<n_glimmers;j++)
        {   double r=0;
            for(uint8_t k=0;k<dim;k++)
            {
                r+=pow(sources[j][k]-observers[i][k],2);
            }
            r=sqrt(r);
           tmp+=wave_info[j][0]/r*cos(PI_2M*wave_info[j][1]*(r/c-t)+wave_info[j][2]);

           
        }
        results[i]=tmp;

        
    }

    io.open("MemoriesWillNeverFade/result.wm");
    for(uint32_t i=0;i<n_observers-1;i++)
    {
        io<<to_string(results[i])<<";";

    }
    io<<to_string(results[n_observers]);

    io.close();
    return 0;
}
