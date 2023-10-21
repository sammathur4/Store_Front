import subprocess

# File to store the last commit message index
message_index_file = 'commit_message_index.txt'

# Function to read the last commit message index from the file
def read_message_index():
    try:
        with open(message_index_file, 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# Function to write the updated commit message index back to the file
def write_message_index(index):
    with open(message_index_file, 'w') as file:
        file.write(str(index))

# Function to generate the commit message based on the index
def generate_commit_message(index):
    return f"Commit {index}"

# Main function
def main():
    last_message_index = read_message_index()
    current_message_index = last_message_index + 1

    commit_message = generate_commit_message(current_message_index)

    # Perform 'git add', 'git commit', and 'git push'
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'push'])

    # Update the last commit message index in the file
    write_message_index(current_message_index)

if __name__ == '__main__':
    main()
