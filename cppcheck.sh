sudo apt-get install cppcheck

# Make a new file 
echo "#include<stdio.h> int main(int a, char **b) { char pin[1024]; strcpy(pin, b[1]); }" > filename.cpp 

cppcheck filename.cpp
