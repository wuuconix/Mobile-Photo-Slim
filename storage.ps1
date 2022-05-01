chcp 65001
$exist = test-path D:\Origin\
if ($exist -eq $true) {
Write-Output "HardDrive Detected Successfully"
Copy-Item slim/* D:\Slim\
Write-Output "Slim copy to HDD successfully"
Copy-Item origin/* D:\Origin\
Write-Output "Origin copy to HDD successfully"
$data = Get-Content path.txt -Encoding utf8
Copy-Item origin/* $data
Write-Output "Origin copy to OneDrive successfully"
Clear-Content files.txt
Write-Output "Cleat Contet of files.txt successfully"
Clear-Content log.txt
Write-Output "Clear Content of log.txt successfully"
} else {
    Write-Output "Please Connect your HDD"
}
