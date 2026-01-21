@echo off
cd /d "C:\Users\admin\Desktop\CryptoStream_Pipeline"
call venv\Scripts\activate.bat
python main.py
echo Pipeline finished at %date% %time% >> etl_log.txt
pause
