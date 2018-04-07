#include <pybind11/pybind11.h>

namespace py = pybind11;

/**

Compiling command

c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup
`python3 -m pybind11 --includes` example.cpp -o example`python3-config --extension-suffix`

c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup
`python -m pybind11 --includes` example.cpp -o example.so


*/

int add(int i, int j) {
    return i + j;
}

struct Pet {
    Pet(const std::string &name) : name(name) { }
    void setName(const std::string &name_) { name = name_; }
    const std::string &getName() const { return name; }

    std::string name;
};


class Dog {
public:
    Dog(const std::string &name) : name(name) { }
    void setName(const std::string &name_) { name = name_; }
    const std::string &getName() const { return name; }
private:
    std::string name;
};


PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("add", &add, "A function which adds two numbers");

    py::class_<Pet>(m, "Pet")
        .def(py::init<const std::string &>())
        .def("setName", &Pet::setName)
        .def("getName", &Pet::getName)
        .def_readwrite("name", &Pet::name)  // expose instance fields
        .def("__repr__",
        [](const Pet &a) {
            return "<example.Pet named '" + a.name + "'>";
        });

    py::class_<Dog>(m, "Dog")
      .def(py::init<const std::string &>())
      .def_property("name", &Dog::getName, &Dog::setName);
}

