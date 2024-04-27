// #include<bits/stdc++.h>
// using namespace std;

// struct Frame {
//     string type;
//     string color;
// };

// struct Wheel {
//     string brand;
//     int size;  
// };

// struct Brake {
//     string type;
//     string model;
// };

// class BicycleAssembly {
// private:
//     Frame frame;
//     vector<Wheel> wheels;
//     Brake brake;

// public:
//     BicycleAssembly(const Frame& f, const vector<Wheel>& ws, const Brake& b) 
//         : frame(f), wheels(ws), brake(b) {}

//     void display() const {
//         cout << "Bicycle Assembly Details:" << endl;
//         cout << "Frame: " << frame.color << " " << frame.type << endl;
//         cout << "Wheels: "<<endl;
//         int idx = 1;
//         for (const auto& wheel : wheels) {
//             cout<<"Your Wheel "<<idx++<<" is: ";
//             cout << wheel.brand << " " << wheel.size << " inch " <<endl;
//         }
//         cout << endl;
//         cout << "Brake: " << brake.type << " " << brake.model << endl;
//     }
// };

// int main() {

//     Frame myFrame = {"Mountain", "Red"};
//     vector<Wheel> myWheels = {{"Raleigh", 26}, {"Raleigh", 26}}; 
//     Brake myBrake = {"Disc", "Shimano"};

//     BicycleAssembly myBicycle(myFrame, myWheels, myBrake);

//     myBicycle.display();

//     return 0;
// }



#include <bits/stdc++.h>
#include <unordered_map>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

unordered_map<string, vector<string>> assembly = {
    {"aeroplane", {"fuselage", "wings", "landing_gear", "cockpit"}},
    {"fuselage", {"seats", "cargo_hold"}},
    {"wings", {"flaps", "ailerons", "engines"}},
    {"engines", {"jet_engines", "propellers"}},
    {"landing_gear", {"wheels", "struts"}},
    {"cockpit", {"control_panel", "seats", "windshield"}}
};

vector<string> processQuery(const string& query) {
    vector<string> components;

    istringstream iss(query);
    string part;
    iss >> part; 

    if (assembly.count(part)) {
        components = assembly[part];
        components.insert(components.begin(), part); 
    }

    return components;
}


int main() {
    cout << "Welcome to the Aeroplane Component Query System!" << endl;

    while (true) {
        cout << "Enter a query (e.g., 'components aeroplane'): ";
        string input;
        getline(cin, input);

        vector<string> result = processQuery(input);

        if (!result.empty()) {
            cout << "Components of " << result[0] << ":" << endl;
            for (size_t i = 1; i < result.size(); ++i) {
                cout << "- " << result[i] << endl;
            }
        } else {
            cout << "Invalid query. Please try again." << endl;
        }

        cout << endl;
    }

return 0;
}