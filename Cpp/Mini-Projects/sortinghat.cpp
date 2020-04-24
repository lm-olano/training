#include <iostream>

static void question1(int *hufflepuff, int *slytherin, int *gryffindor, int *ravenclaw);
static void question2(int *hufflepuff, int *slytherin, int *gryffindor, int *ravenclaw);
static void question3(int *hufflepuff, int *slytherin, int *gryffindor, int *ravenclaw);
static void question4(int *hufflepuff, int *slytherin, int *gryffindor, int *ravenclaw);

int main(void) {
    int gryffindor, hufflepuff, ravenclaw, slytherin;
    int max;
    std::string house;

    // Initialization
    gryffindor = 0;
    hufflepuff = 0;
    ravenclaw = 0;
    slytherin = 0;
    max = 0;


    std::cout << "The Sorting Hat Quiz!\n";

    question1(&hufflepuff, &slytherin, &gryffindor, &ravenclaw);
    question2(&hufflepuff, &slytherin, &gryffindor, &ravenclaw);
    question3(&hufflepuff, &slytherin, &gryffindor, &ravenclaw);
    question4(&hufflepuff, &slytherin, &gryffindor, &ravenclaw);

    if (gryffindor > max) {

    max = gryffindor;
    house = "Gryffindor";

    }

    if (hufflepuff > max) {

    max = hufflepuff;
    house = "Hufflepuff";

    }

    if (ravenclaw > max) {

    max = ravenclaw;
    house = "Ravenclaw";

    }

    if (slytherin > max) {

    max = slytherin;
    house = "Slytherin";

    }

    std::cout << house << "!\n";

    return 0;
}

void question1(int *hufflepuff, int *slytherin, int *gryffindor, int *ravenclaw) {
    int answer;

    std::cout << "Q1) When I'm dead, I want people to remember me as:\n\n";

    std::cout << "1) The Good\n";
    std::cout << "2) The Great\n";
    std::cout << "3) The Wise\n";
    std::cout << "4) The Bold\n";
    std::cin >> answer;

    if (answer == 1) {
        *hufflepuff += 1;
    } 
    else if (answer == 2) {
        *slytherin += 1;
    }
    else if (answer == 3) {
        *ravenclaw += 1;
    }
    else if (answer == 4) {
        *gryffindor += 1;
    }
    else {
        std::cout << "Invalid input.\n\n";
        question1(hufflepuff, slytherin, gryffindor, ravenclaw);
    }

}

void question2(int *hufflepuff, int *slytherin, int *gryffindor, int *ravenclaw) {
    int answer;

    std::cout << "Q2) Dawn or Dusk?\n\n";

    std::cout << "1) Dawn\n";
    std::cout << "2) Dusk\n";
    std::cin >> answer;

    if (answer == 1) {
        *ravenclaw += 1;
        *gryffindor += 1;
    }
    else if (answer == 2) {
        *hufflepuff += 1;
        *slytherin += 1;
    }
    else {
        std::cout << "Invalid input.\n\n";
        question2(hufflepuff, slytherin, gryffindor, ravenclaw);
    }
}

void question3(int *hufflepuff, int *slytherin, int *gryffindor, int *ravenclaw) {
    int answer;

    std::cout << "Q3) Which kind of instrument most pleases your ear?\n\n";

    std::cout << "1) The violin\n";
    std::cout << "2) The trumpet\n";
    std::cout << "3) The piano\n";
    std::cout << "4) The drum\n";
    std::cin >> answer;

    if (answer == 1) {
        *slytherin += 1;
    } 
    else if (answer == 2) {
        *hufflepuff += 1;
    }
    else if (answer == 3) {
        *ravenclaw += 1;
    }
    else if (answer == 4) {
        *gryffindor += 1;
    }
    else {
        std::cout << "Invalid input.\n\n";
        question3(hufflepuff, slytherin, gryffindor, ravenclaw);
    }
}


void question4(int *hufflepuff, int *slytherin, int *gryffindor, int *ravenclaw) {
    int answer;

    std::cout << "Q4) Which road tempts you most?\n\n";

    std::cout << "1) The wide, sunny grassy lane\n";
    std::cout << "2) The narrow, dark, lantern-lit alley\n";
    std::cout << "3) The twisting, leaf-strewn path through woods\n";
    std::cout << "4) The cobbled street lined (ancient buildings)\n";
    std::cin >> answer;

    if (answer == 1) {
        *hufflepuff += 1;
    } 
    else if (answer == 2) {
        *slytherin += 1;
    }
    else if (answer == 3) {
        *gryffindor += 1;
    }
    else if (answer == 4) {
        *ravenclaw += 1;
    }
    else {
        std::cout << "Invalid input.\n\n";
        question4(hufflepuff, slytherin, gryffindor, ravenclaw);
    }
}