// SimpleCorridor.h
#pragma once
#include <pybind11/pybind11.h>
#include <iostream>
#include <map>
#include <string>

using namespace std;

namespace rl {
    class SimpleCorridor {
        private:
            int end_pos;
            int cur_pos;
            // int action_space;
            // int observation_space;
        public:
            SimpleCorridor(map<string, int>);
            int reset();
            tuple<int, int, bool> step(int action);
    };
}

namespace py = pybind11;

PYBIND11_MODULE(simple_corridor, m) {
    m.doc() = "pybind11 simple_corridor plugin";

    // Binding to SimpleCorridor
    py::class_<rl::SimpleCorridor>(m, "SimpleCorridor")
        .def(py::init<map<string, int>>())
        .def("reset", &rl::SimpleCorridor::reset)
        .def("step", &rl::SimpleCorridor::step);
}