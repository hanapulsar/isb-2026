#include <iostream>
#include <fstream>
#include <random>

int main() {
	std::string filename = "cpp_random.txt";
	std::ofstream file(filename);

	if (!file.is_open()) {
		std::cerr << "Cant open txt to write in random sequence.\n";
		return 1;
	}

	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<> dis(0, 1);

	for (int i = 0; i < 128; ++i) {
		file << dis(gen);
	}

	file.close();
	std::cout << "Sequence was generated and written to " << filename << std::endl;

	return 0;
}
