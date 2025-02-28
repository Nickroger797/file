echo "Cloning Repo..."
git clone https://github.com/Nickroger797/file /file
cd /file

pip3 install -r requirements.txt

echo "Starting Server..."
gunicorn --bind 0.0.0.0:8080 server:app &  # Run Flask using Gunicorn

echo "Starting Bot..."
python3 bot.py  # Run bot normally

