if "%~1"==""  (
    python -m classgenerator "project-name" --path "./utils" --inline "classA/ classB : attr1/ attr2, attr3/ attr4 : methodA / methodB : -e / -t"
    exit /b
)
if %1 == inheritance (
    python -m classgenerator "project-name" --path "C://some//shit" --inline "Person1/ Person2 > Employee > Dish_washer, Short_Order_Cook/ Sous_Chef : P1A/ P1B, P2A/ P2B > E1/ E2/ E3 > D1/ D2, S1/ S2, SC1/ SC2 : P1method / P2method > SMmethod > CMmethod1 / SMmethod2 / SMmethod3 : -e / -e -t > -e > -e / -t / -et"
    exit /b
)
if %1 == file (
    echo file option selected. not implemented at this time
    exit /b
)
if %1 == interactive (
    python -m classgenerator "project-name" --path "C://some//shit" -i
    exit /b
)
