import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(BASE_DIR, 'FOCT/../foctapp/../statics/'))
print( os.path.join(os.path.dirname(__file__), '../static'))