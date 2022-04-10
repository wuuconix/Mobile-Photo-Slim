# ./storage.ps1 ????
$exist = test-path D:\Origin\
if ($exist -eq $true) {
    echo "HardDrive Detected Successfully"
    cp slim/* D:\Slim\
    echo "Slim copy to HDD successfully"
    cp origin/* D:\Origin\
    echo "Origin copy to HDD successfully"
    # ignore this fucking code. it is ok
    cp origin/* "C:\Users\15219\OneDrive - uconix\夕頭\返字�牴�"
    echo "Origin copy to OneDrive successfully"
    clc files.txt
    echo "Cleat Contet of ilest.txt successfully"
    clc log.txt
    echo "Clear Content of log.txt successfully"
} else {
    echo "Pleast conect you HDD"
}