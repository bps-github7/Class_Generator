REM simple script for facilitating testing of class generator program. facilitates calling the various options for invoking the program with cmd line.
if "%~1"==""  (
    if %2 == "verbose" (
        python -m classgenerator "project name" --path "C://some//shit" --inline "classA, classB : attr1, attr2 / attr3, attr4 : methodA / methodB -e{vsc}" -v
        exit /b        
    )
    python -m classgenerator "project name" --path "C://some//shit" --inline "classA, classB : attr1, attr2 / attr3, attr4 : methodA / methodB -e{vsc}"
    exit /b
)
if %1 == inheritance (
    if %2 == "verbose" (
        python -m classgenerator "project name" --path "C://some//shit" --inline "Person1, Person2 > Employee > Dish_washer, Short_Order_Cook, Sous_Chef : P1A, P1B / P2A, P2B > E1, E2, E3 > D1, D2 / S1, S2 / SC1, SC2 : P1method / P2method > SMmethod > CMmethod / SMmethod / method" -v
        exit /b        
    )
    python -m classgenerator "project name" --path "C://some//shit" --inline "Person1, Person2 > Employee > Dish_washer, Short_Order_Cook, Sous_Chef : P1A, P1B / P2A, P2B > E1, E2, E3 > D1, D2 / S1, S2 / SC1, SC2 : P1method / P2method > SMmethod > CMmethod / SMmethod / method"
    exit /b
)
if %1 == file (
    echo file option selected. not implemented at this time
    exit /b
)
if %1 == interactive (
    python -m classgenerator "project name" --path "C://some//shit" -i
    exit /b
)
