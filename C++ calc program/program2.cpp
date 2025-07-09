

#include <iostream>
using namespace std;

int main() {
	string Number;
	int baseNum;
	int i; // number loop
	int y;
	int DecimalNumber = 0;
	cout << "Enter Number: ";
	cin >> Number;
	cout << "Enter base number:";
	cin >> baseNum;
	for (i = 0; i < Number.length(); ++i) {
		 y = Number[i] - '0'; // convert charater to integer
		 DecimalNumber += y * pow(baseNum, Number.length() - 1 - i);
		
	}
	cout << "Decimal Value: " << DecimalNumber << endl;
		


	return 0;
}