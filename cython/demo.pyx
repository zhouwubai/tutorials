from libc.stdlib cimport atoi
from libc.math cimport sin

cdef parse_charptr_to_py_int(char* s):
    assert s is not NULL, "byte string value is NULL"
    return atoi(s)   # note: atoi() has no error detection!

cdef double f(double x):
    return sin(x*x)

cdef extern from "math.h":
    double sin(double x)

cdef extern from "math.h":
    cpdef double sin(double x)