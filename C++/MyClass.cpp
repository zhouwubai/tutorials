#include "MyClass.h"
#include <iostream>
using namespace std;

MyClass::MyClass(int a, int b)
:regVar(a), constVar(b)  // variable initilizer, must for const
{
  cout<<"Coustructor"<<endl;
  cout<<regVar<<endl;
  cout<<constVar<<endl;
}

MyClass::~MyClass(){
  cout<<"Destructor"<<endl;
}

/*
const object can only call const function
*/
void MyClass::myPrint() const{
  cout<<"Hello"<<endl;
}


void MyClass::printInfo()
{
  cout<<regVar<<endl;
  cout<<this->regVar<<endl; // this is a pointer to object itself, it has important role in operator overriding
  cout<<(*this).regVar<<endl;
}


// friend function
void someFunc(MyClass &obj)
{
  obj.regVar = 42;
  cout << obj.regVar << endl;
}


Birthday::Birthday(int m, int d, int y)
:month(m), day(d), year(y)
{
}

void Birthday::printDate()
{
  cout<<month<<"/"<<day<<"/"<<year<<endl;
}


Person::Person(string n, Birthday b)
:name(n), db(b)
{
}

void Person::printInfo()
{
  cout<<name<<endl;
  db.printDate();
}


Overrider::Overrider(){}
Overrider::Overrider(int a)
:var(a)
{
}

/*
Overrider Overrider::operator+(Overrider obj)  // &obj or obj
{

}
*/