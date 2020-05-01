// SimpleCorridor.h
#pragma once
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <map>
#include <string>

using namespace std;

namespace rl {
    class SimpleCorridor {
        private:
            int end_pos;
            int cur_pos;
        public:
            SimpleCorridor(map<string, int>);
            int reset();
            tuple<int, int, bool> step(int action);
            // string action_space_descriptor;
            // string observation_space_descriptor;
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
        // .def_readwrite("action_space_descriptor", &rl::SimpleCorridor::action_space_descriptor)
        // .def_readwrite("observation_space_descriptor", &rl::SimpleCorridor::observation_space_descriptor)
        // .def_readwrite("action_space", &rl::SimpleCorridor::action_space)
        // .def_readwrite("observation_space", &rl::SimpleCorridor::observation_space);
}