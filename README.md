
# pybind11 demo

Demonstrates how to call a C++ class from Python using pybind11.

## How to build this demo

```
git clone --recursive https://github.com/rusu24edward/pybind11-demo.git
cd pybind11-demo
mkdir build
cd build
cmake ..
make
```


## Example test run

1. Install the python libraries in requirements
2. Run `rllib_example.py` to see training entirely in python
3. Run `rllib_cpp_example.py` to see training with the cpp class



## Repository details:

`bind_wrapper.py` is just a helpful function for testing out the wrappings.

`build` is the directory that stores the built cpp objects

`cpp_wrapper.py` is the wrapper class that "tricks" the training library into thinking that the 
class is a gym.Env class.

`pybind11` is the submodule that contains pybind11, needed for the bindings between python and C++

`rllib_cpp_example.py` is a training example using the cpp env object

`rllib_example.py` is a training example using the python env object

`simple_corridor.*` is the cpp environment


## Timing results

The timing results between python and C++ environment show that for this simple environment there
is no gain from using cpp over python. However, we imagine that complicated step functions will
benefit from being written in cpp.


