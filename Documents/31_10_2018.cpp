#include <iostream>
using namespace std;

struct student
{
	string fname;
	int day;
	int month;
	int year;
};


int main()
{
	int n;
	cin>>n;
	student mas[n];
	for (int i=0;i<n;i++)
	{

		cin>>mas[i].fname;
		cin>>mas[i].day;
		cin>>mas[i].month;
		cin>>mas[i].year;
	}
	student max;
	max.fname=mas[0].fname;
	max.day=mas[0].day;
	max.month = mas[0].month;
	max.year = mas[0].year;
	for (int i=1;i<n;i++)
	{
		if (mas[i].year>max.year)
		{
			max.year = mas[i].year;
			max.fname = mas[i].fname;
		}
		if (mas[i].year == max.year){
			if (mas[i].month>max.month)
			{
				max.month = mas[i].month;
				max.fname = mas[i].fname;
			}
			if (mas[i].month == max.month)
			{
				if (mas[i].day>max.day)
					{
						max.day = mas[i].day;
						max.fname = mas[i].fname;
					}
			}
		}
	}
	cout<<max.fname<<endl;
	cout<<max.day<<endl;
	cout<<max.month<<endl;
	cout<<max.year<<endl;

}