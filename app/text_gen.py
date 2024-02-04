import os
import random
import string

def generate_text(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def main():
    file_path = '/serverdata/random.txt'

    if os.path.exists(file_path):
        with open(file_path, 'w') as f:
            existing_text = f.read()
            print(f'Existing text: {existing_text}')
    
    new_text = generate_text(100)
    print(f'New text: {new_text}')

    with open(file_path, 'w') as f:
        f.write(new_text)

if __name__ == '__main__':
    main()