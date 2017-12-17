// namespaces are used in packages generated for each langauge
namespace php adder
namespace py adder

// you can name your own types and rename the build-in ones
typedef i32 int

service AddService {
  // add method - returns results of sum of two integers
  int add(1:int number1, 2:int number2)
}