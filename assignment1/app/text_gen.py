import os
import random
import string


def generate_text(length):
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))


def main():
    # Directory to mount volume
    volume_path = "/serverdata"

    # Create the directory if it doesn't exist
    if not os.path.exists(volume_path):
        os.makedirs(volume_path)

    # File path within the mounted volume
    file_path = os.path.join(volume_path, "random.txt")

    if os.path.exists(file_path):
        # If file exists, read and print existing text
        with open(file_path, "r") as f:
            existing_text = f.read()
            print(f"Existing text: {existing_text}")

    # Generate new text
    new_text = generate_text(100)
    print(f"New text: {new_text}")

    # Write new text to the file
    with open(file_path, "w") as f:
        f.write(new_text)


if __name__ == "__main__":
    main()
