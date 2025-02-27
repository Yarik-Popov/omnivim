python -m venv venv
call venv\Scripts\activate && ^
pip install -r requirements.txt && ^
python -c "from PIL import Image; Image.open('Images/omnivim.png').save('Images/omnivim.ico')" && ^
pyinstaller --onefile --windowed --name Omnivim --icon="Images/omnivim.ico" --add-data "Images;Images" --add-data "Ibm.ttf;." --add-data "style.css;." --add-data "Images/omnivim.png;Images" --add-data "Images/omnivimi.png;Images" --add-data "Images/omnivimm.png;Images" --add-data "Images/omnivimn.png;Images" --add-data "Images/omnivimv.png;Images" --add-data "Windows_Mouse_Movments;Windows_Mouse_Movments" main.py
