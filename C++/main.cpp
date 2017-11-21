#include <iostream>
#include "MyClass.h"
#include "MyClass.cpp"
using namespace std;

int main(){

  // pointer, dynamic memory
  cout <<"\n=====Pointer, Dynamic Memory=====\n"<<endl;
  int *p = new int;
  *p = 5;
  cout << *p << endl;
  delete p;  // becomes a dangle pointer
  cout << p << endl;  // output the address, *p still equal to 5
  int *tmpP = p;
  p = new int;
  cout << p << endl;
  cout << (tmpP == p) << endl;  // this might be equal, but not 100% sure

  // dynamic memory for array
  int *arrP = NULL;
  arrP = new int[20];
  delete [] arrP; // delete array pointed to the array


  // class
  cout <<"\n=====Class=====\n"<<endl;
  const MyClass obj(42, 33);
  obj.myPrint();
  //obj.printInfo(); it is illegal

  MyClass obj2(12, 24);
  someFunc(obj2);
  obj2.printInfo(); // this pointer

  // class composition
  cout <<"\n=====Composition=====\n"<<endl;
  Birthday bd(5, 55, 5555);
  Person person("Wubai Zhou", bd);
  person.printInfo();

  /*
  operator overriding, not including :: | .* | . | ?:
  */
  cout <<"\n=====Overriding=====\n"<<endl;
  Overrider over1(12), over2(23);
  Overrider res = over1 + over2;
  cout<<res.var<<endl;


  // Inheritance
  cout << "\n=====Inheritance=====\n"<<endl;
  Daughter daughter;
  daughter.sayHi();


  // Polymorphism
  cout << "\n=====Polymorphism=====\n"<<endl;
  Ninja ninja;
  Monster monster;
  Enemy *e1 = &ninja;
  Enemy *e2 = &monster;

  e1->setAttackPower(5);
  e2->setAttackPower(55);

  ninja.attack(); //e1->attack() is not working, abstract function comes here
  monster.attack();
}