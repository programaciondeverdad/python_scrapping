Errores:

Error 1
>pip3 install requests
Collecting requests
  Downloading requests-2.25.1-py2.py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 3.8 MB/s
Collecting certifi>=2017.4.17
  Downloading certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
     |████████████████████████████████| 147 kB 6.4 MB/s
Collecting idna<3,>=2.5
  Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 3.0 MB/s
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.2-py2.py3-none-any.whl (136 kB)
     |████████████████████████████████| 136 kB ...
Collecting chardet<5,>=3.0.2
  Downloading chardet-4.0.0-py2.py3-none-any.whl (178 kB)
     |████████████████████████████████| 178 kB 6.8 MB/s
Installing collected packages: certifi, idna, urllib3, chardet, requests
  WARNING: Failed to write executable - trying to use .deleteme logic
ERROR: Could not install packages due to an EnvironmentError: [WinError 2] El sistema no puede encontrar el archivo especificado: 'c:\\python39\\Scripts\\chardetect.exe' -> 'c:\\python39\\Scripts\\chardetect.exe.deleteme'

WARNING: You are using pip version 20.2.3; however, version 20.3.3 is available.
You should consider upgrading via the 'c:\python39\python.exe -m pip install --upgrade pip' command.


Resolución: Ejecutar cmd como Administrador

---------------------------------
