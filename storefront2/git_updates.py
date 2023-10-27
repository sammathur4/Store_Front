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


# Function to get the list of changed files
def get_changed_files():
    result = subprocess.check_output(['git', 'diff', '--name-only']).decode('utf-8')
    return result.splitlines()


# Main function
def main():
    last_message_index = read_message_index()
    current_message_index = last_message_index + 1

    commit_message = generate_commit_message(current_message_index)
    changed_files = get_changed_files()

    if changed_files:
        print("Changed files:")
        names = ''
        for file in changed_files:
            print(file)
            names += ": " + f'{file}'

        # Perform 'git add', 'git commit', and 'git push'
        subprocess.run(['git', 'add', '.'])
        commit_message += f'{names}'
        subprocess.run(['git', 'commit', '-m', commit_message])
        subprocess.run(['git', 'push'])

        # Update the last commit message index in the file
        write_message_index(current_message_index)
    else:
        print("No changes to commit.")


if __name__ == '__main__':
    main()
    