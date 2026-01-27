// commands for g++:
// debug:
// g++ -o playground wys_playground_cpp.cpp -Wall -Wextra -Wpedantic -g -march=native -std=c++11
// ./playground
// speed:
// g++ -o playground wys_playground_cpp.cpp -Wall -Wextra -Wpedantic -O3 -march=native -std=c++11
// ./playground
// note that the -std=c++11 can be changed to any newer version :)

#include <array>
#include <chrono>
#include <iostream>
#include <string>
#include "wys_lib.hpp"

template<size_t N>
bool end_check(std::array<unsigned, N> track, unsigned data_size, const std::vector<unsigned> &key) {
	unsigned key_index = 0;
	for (; data_size > 0;) {
		unsigned shift = key[key_index++ % key.size()] % data_size + 1;
		for (unsigned i = 0; i < N; i++) {
			if (track[i] != unsigned(-1)) {
				track[i] = (track[i] + data_size - shift) % data_size;
				if (track[i] == data_size - 1) {
					track[i] = unsigned(-1);
					if (data_size == 1)
						return true;
				}
			}
		}
		data_size--;
	}
	return false;
}

template<bool Accel>
void l4bf() {
	auto start = std::chrono::high_resolution_clock::now();
	std::string d4 = data4;
	std::cout << d4 << std::endl;
	std::cout << d4.size() << std::endl;
	std::array<unsigned, 3> track;
	unsigned ti = 0;
	for (unsigned i = 0; i < d4.size(); i++) {
		if (d4[i] == ')')
			track[ti++] = i;
	}
	if constexpr (Accel) {
		std::cout << "accel\n";
	} else {
		std::cout << "classic\n";
	}

	std::vector<unsigned> key(7);
	for (unsigned long long i = 0; i < 8'031'810'176ull; i++) {
		unsigned k = i;
		for (unsigned j = 0; j < 7; j++) {
			key[j] = k % 26 + 1;
			k /= 26;
		}
		if constexpr (Accel) {
			if (end_check(track, d4.size(), key)) {
				std::string r = humanscantsolvethis_decrypt(d4, std::string{{char(key[0]+64),char(key[1]+64),
					char(key[2]+64), char(key[3]+64),char(key[4]+64),char(key[5]+64),char(key[6]+64)}});
				if (r.find("DATA(") != std::string::npos)
					std::cout << "checked(')', 'data(')[" << r << "]\n";
			}
		} else {
			std::string r = humanscantsolvethis_decrypt(d4, std::string{{char(key[0]+64),char(key[1]+64),
				char(key[2]+64), char(key[3]+64),char(key[4]+64),char(key[5]+64),char(key[6]+64)}});
			if (r.back() == ')' && r.find("DATA(") != std::string::npos)
				std::cout << "checked('data(')[" << r << "]\n";
		}
		if (i % 1'000'000 == 0) {
			auto now = std::chrono::high_resolution_clock::now();
			long dur = std::chrono::duration_cast<std::chrono::milliseconds>(now - start).count();
			std::cout << i/1'000'000 << "m tests done in " << dur << "ms -> " << double(dur) / double(i / 1'000'000) << "ms/m" << std::endl;
		}
	}
}

int main(int argc, char **argv) {
	if (argc > 1) {
		l4bf<true>();
	} else {
		l4bf<false>();
	}
	return 0;
}
