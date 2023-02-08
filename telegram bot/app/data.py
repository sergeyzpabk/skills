import codecs
from app.derictory import get_path_to_dict
struct_files = {}

text_start = ''

def load_struct_files():
    global struct_files
    struct_files = get_path_to_dict()

def load_text():
    global text_start
    text_start = codecs.open('app\\settings\\text.txt' , "r", "utf-8").read()
    print('text start', text_start)