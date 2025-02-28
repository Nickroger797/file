echo "Cloning Repo..."
if [ -d "/file" ]; then
    rm -rf /file  # Remove old repo if exists
fi
git clone https://github.com/Nickroger797/file /file
cd /file

pip3 install -r requirements.txt

echo "Starting Server..."
gunicorn --bind 0.0.0.0:$PORT server:app &

echo "Starting Bot..."
python3 bot.py  # Run bot normally
