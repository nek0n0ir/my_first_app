# For development use (simple logging, etc):
python jeu.py
# For production use: 
# gunicorn server:app -w 1 --log-file -