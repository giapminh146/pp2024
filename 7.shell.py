import subprocess


def execute_command(command):
    try:
        command_list = command.split()
        if '>' in command_list:
            index = command_list.index('>')
            output_file = command_list[index + 1]
            output = subprocess.run(command_list[:index], capture_output=True, text=True)
            with open(output_file, 'w') as file:
                file.write(output.stdout)
        elif '<' in command_list:
            index = command_list.index('<')
            input_file = command_list[index + 1]
            with open(input_file, 'r') as file:
                output = subprocess.run(command_list[:index], input=file.read(), capture_output=True, text=True)
                print(output.stdout)
        else:
            output = subprocess.run(command_list, capture_output=True, text=True)
            print(output.stdout)
    except FileNotFoundError:
        print("Command not found")
    except Exception:
        print(f"An error has occurred: {Exception}")

def main():
    while True:
        command = input("~:$ ")
        if command.lower() == "exit":
            break
        execute_command(command)


if __name__ == "__main__":
    main()
