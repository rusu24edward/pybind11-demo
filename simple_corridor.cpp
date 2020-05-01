// SimpleCorridor.cpp

// #include "simple_corridor.h"

#include <pybind11/pybind11.h>

#include <iostream>
#include <map>
#include <string>
using namespace std;

class SimpleCorridor {
    private:
        int end_pos;
        int cur_pos;
        int action_space;
        int observation_space;

    public:
        SimpleCorridor(int corridor_length) {
            this->end_pos = corridor_length;
            this->cur_pos = 0;
            // this->action_space = 
            // this->observation_space = 
        }
        ~SimpleCorridor() {}

    int reset() {
        this->cur_pos = 0;
        return this->cur_pos;
    }

    tuple<int, int, map<string, int>> step(int action) {
        if (action == 0 && this->cur_pos > 0) {
            this->cur_pos--;
        }
        else if (action == 1) {
            this->cur_pos++;
        }
        bool done = this->cur_pos >= this->end_pos;
        auto result_tuple = make_tuple(this->cur_pos, done, map<string, int>());
        return result_tuple;
    }
};

namespace py = pybind11;

PYBIND11_MODULE(simple_corridor, m) {
    m.doc() = "pybind11 simple_corridor plugin";

    // Binding to SimpleCorridor
    py::class_<SimpleCorridor>(m, "SimpleCorridor")
        .def(py::init<int>())
        .def("reset", &SimpleCorridor::reset)
        .def("step", &SimpleCorridor::step);
}

