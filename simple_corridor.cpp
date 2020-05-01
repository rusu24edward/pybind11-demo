// SimpleCorridor.cpp

#include "simple_corridor.h"

#include <map>
#include <string>
using namespace std;

rl::SimpleCorridor::SimpleCorridor(int corridor_length) {
    this->end_pos = corridor_length;
    this->cur_pos = 0;
    // this->action_space = 
    // this->observation_space = 
}

int rl::SimpleCorridor::reset() {
    this->cur_pos = 0;
    return this->cur_pos;
}

tuple<int, int, bool> rl::SimpleCorridor::step(int action) {
    if (action == 0 && this->cur_pos > 0) {
        this->cur_pos--;
    }
    else if (action == 1) {
        this->cur_pos++;
    }
    bool done = this->cur_pos >= this->end_pos;
    int reward = done ? 1 : 0;
    auto result_tuple = make_tuple(this->cur_pos, reward, done);
    return result_tuple;
}


