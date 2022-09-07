# Skrypty bash

## Jak sprawdzić w bash czy mysql wymaga hasła
Warunek $? == 0 potwierdza że polecenie wykonało się poprawnie. 
```sh
#!/bin/bash

PASS="toor"

# sudo mysql -u root -p$PASS -e "SHOW VARIABLES LIKE '%ca%';"

sudo mysql -u root -p$PASS -e "QUIT" > 2&>1
if [ "$?" -eq 0 ]; 
then
  echo "Done. Mysql need password"
  
  # Remove mysql user password
  mysql -u root -p$PASS -e "
  ALTER USER 'root'@'localhost' IDENTIFIED BY '';
  ALTER USER 'root'@'127.0.0.1' IDENTIFIED BY '';
  FLUSH PRIVILEGES;
  "
else
  echo "Failed. Mysql do not need password."
fi
```

## Funkcje warunkowe
```sh
if [ foo ]; then ...       # "if the string 'foo' is non-empty, return true"
if foo; then ...           # "if the command foo succeeds, return true"

if [ "$foo" = "$bar" ]     # true if the string values of $foo and $bar are equal
if [ "$foo" -eq "$bar" ]   # true if the integer values of $foo and $bar are equal
if [ -f "$foo" ]           # true if $foo is a file that exists (by path)
if [ -d "/path/to/dir" ]   # true if directory exists
if [ ! -d "/path/to/dir" ] # true if directory not exists
if [ "$foo" ]              # true if $foo evaluates to a non-empty string
if foo                     # true if foo, as a command/subroutine, evaluates to true/success (returns 0 or null)
if [ "$#" -eq 0 ] ;        # true if script has no arguments 
if [ "$#" -gt 1 ] ;        # true if script has more than 1 arguments 

# Errors
Exit code 0        Success
Exit code 1        General errors, Miscellaneous errors, such as "divide by zero" and other impermissible operations
Exit code 2        Misuse of shell builtins (according to Bash documentation) Example: empty_function() {}

# Read input
read -p 'Username: ' uservar
read -sp 'Password: ' passvar
echo
echo Thankyou $uservar we now have your login details

# Sample
if [ "$foo" = "$bar" ]; then
  echo "Hello"
fi

# Arguments
while getopts u:a:f: flag
do
    case "${flag}" in
        u) username=${OPTARG};;
        a) age=${OPTARG};;
        f) fullname=${OPTARG};;
    esac
done
echo "Username: $username";
echo "Age: $age";
echo "Full Name: $fullname";

# Use
sh script.sh -f 'John Smith' -a 30 -u alice
```

### Katalogi
```bash
if [ -d "/path/to/dir" ]
then
    echo "Directory /path/to/dir exists." 
else
    echo "Error: Directory /path/to/dir does not exists."
fi

# Średnik oznacza koniec linji skryptu
if [ -d "/path/to/dir" ]; then
    echo "Directory /path/to/dir exists." 
else
    echo "Error: Directory /path/to/dir does not exists."
fi

# Wersja któtka
[[ -d <directory> ]] && echo "This directory exists!"
```

### Pętla po argumentach skryptu
script.sh file1, file2 ...
```sh
#!/bin/bash

for FILE in ${@}
do
  if [ ! -f $FILE ]
  then
    echo "The file ${FILE} does not exist!"
  fi
done
```
