#include <iostream>
#include <cmath>
using namespace std;



double chet(double y)
{
	double result = y*y + 4*y - 3;
	return result;
}

double proizvod_1(double y)
{
	double result=3*y+4;
	return result;
}



double first(double (*f)(double),double eps)
{
	double c,a,b;
	int n;
	a=0;
	b=1;
	while((b-a)/2>eps){
		c=(a+b)/2;
		n++;
		if((f(a)*f(c))>0) 
			a=c;
		else 
			b=c;
	}
	cout<<n;
	return c;
}
double second (double sas)
{
	double a,b,c,pas,n;
	a=0;
	pas=sas;
	b=1;
	c=0;
	n=0;
	while ((pas<1)&&(chet(b)>0))
	{
		c=b-abs(chet(b)/proizvod_1(b));
		b=c;
		pas=pas*10;
		n++;
	}
	cout<<n;
	return c;
}
double third (double x,double eps)
{
	double tmp;
	int N=0;
	tmp=x+2*eps;
	while(abs(x-tmp)>eps) { 
		tmp=x;
		x=x-chet(x)/proizvod_1(x);
		N++;
	}
	cout<<N;
	return x;
}
int main()
{
	double error;
	double good;
	cout<<"Введите погрешность:"<<endl;
	cin>>error;
	good=error*10;
	cout<<"Выбирете метод нахождения(1-Деление ,2-Касательная ,3-Хорды ,4-Все)"<<endl;
	int what_method;
	cin>>what_method;
	if ((what_method==1)||(what_method==4)) {
		cout<<"Методом деления: "<<first(chet,error);
		cout<<endl;
	}
	if ((what_method==2)||(what_method==4)) {
		cout<<"Методом касательной: "<<second(error); 
		cout<<endl;
	}
	if ((what_method==3)||(what_method==4)) {
		cout<<"Методом хорд: "<<third(error,good); 
		cout<<endl;
	}
	return 0;
}