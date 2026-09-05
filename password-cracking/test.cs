#include <stdio.h>
#include <unistd.h>
#include <crypt.h>
int main() {
    const char *password = "password";  
    const char *salt = "$y$j9T$t4HYYraTPjT8AtgercDbi.";
    char *hash = crypt(password, salt);
    printf("Hash: %s\n", hash); 

    return 0;
}