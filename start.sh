echo "Cloning Repo..."
git clone https://github.com/Nickroger797/file /file
cd /file

pip3 install -r requirements.txt

echo "Starting Server..."
python3 server.py &  # Run server.py in the background

echo "Starting Bot..."
python3 bot.py       # Run bot.py normally
