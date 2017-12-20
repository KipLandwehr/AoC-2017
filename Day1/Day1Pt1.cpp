#include <fstream>
#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int ctoi(char num);

int main() {
	ifstream infile("Day1Input.txt");
	if(infile.fail()) {
		exit(1);
	}
	string line;
	getline(infile, line);

	int count = 0;
	int prev = line.length() - 1;
	for (int curr = 0; curr < line.length(); curr++) {
		if(line[prev] == line[curr])
			count += ctoi(line[curr]);
		prev = curr;
	}
	cout << count << endl;
}

int ctoi(char num) {
	return (num - '0');
}