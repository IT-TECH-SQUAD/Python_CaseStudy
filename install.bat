@echo off
@setlocal DisableDelayedExpansion

color a
echo [SETTING UP]J05-Team-POS - For foodchain services
timeout /t 3 /nobreak > NUL
echo [STARTING]Prepare for installing dependencies
timeout /t 3 /nobreak > NUL
echo [INSTALLING]File is downloading
git clone https://github.com/Jamer05/Python_CS
echo [Project has been cloned]
cd Python_CS
echo [INSTALLIING]Downloading resources...
pip install -r requirements.txt
python main.py
