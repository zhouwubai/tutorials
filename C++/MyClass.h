#ifndef MYCLASS_H
#define MYCLASS_H

using namespace std;

class MyClass{
public:
  MyClass(int a, int b);
  ~MyClass();
  void myPrint() const;
  void printInfo();
protected:
private:
  int regVar;
  const int constVar;

friend void someFunc(MyClass &obj); // friend function can access private members, must passing by references.
};


class Birthday{
public:
  Birthday(int m, int d, int y);
  void printDate();
private:
  int month;
  int day;
  int year;
};


class Person{
public:
  Person(string n, Birthday b);
  void printInfo();
private:
  string name;
  Birthday db;
};


class Overrider{
public:
  Overrider();
  Overrider(int a);

  Overrider operator+(Overrider &obj) // both &obj and obj works
  {
    Overrider res;
    res.var = this->var + obj.var;
    return res;
  }
public:
  int var;
};



//inheritance
class Mother{
public:
  Mother();
  ~Mother();
  void sayHi();
private:
};


class Daughter: public Mother{
public:
  Daughter();
  ~Daughter();
};


//Polymorphism

class Enemy{
protected:
  int attackPower;
public:
  void setAttackPower(int a);
};

class Ninja: public Enemy{
public:
  void attack();
};

class Monster: public Enemy{
public:
  void attack();
};

#endif // MYCLASS_H