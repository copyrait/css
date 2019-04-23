sudo apt-get -y install splint

# Create new file 
echo "#include<stdio.h> int main(int a, char **b) { char pin[1024]; strcpy(pin, b[1]); }" > filename.c 

splint filename.c
