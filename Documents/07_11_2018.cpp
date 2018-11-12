#include <iostream>
#include <fstream>
using namespace std;

struct comand
{
	string com_name;
	int ok[];
	int score;
	int win;
	int lose;
	int sred;
};


int main()
{
	int n;
	cout<<"col-vo:"<<endl;

	cin>>n;
	comand mas[n];
	for (i=0;i<n;i++)
	{
		for (j=0;j<n;j++)
		{
			cin>>mas[i].ok[j]
		}
		cin>>mas[i].score;
		cin>>mas[i].win;
		cin>>mas[i].lose;
		cin>>mas[i].sred;
		
	}
	cout << s << endl;

}