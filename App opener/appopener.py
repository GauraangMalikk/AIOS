import subprocess
import re

def ask_llm(prompt):
    result = subprocess.run(
        ['ollama', 'run', 'llama3'],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode().strip()

def extract_command(text):
    # Prefer code block first
    code_block = re.search(r"```(?:bash)?\n(.+?)\n```", text, re.DOTALL)
    if code_block:
        return code_block.group(1).strip()
    
    # Fallback: try to get first line starting with a command
    for line in text.splitlines():
        if line.strip().startswith(("/", ".", "mkdir", "ls", "cd", "mv", "cp", "sudo", "touch", "echo", "cat","find", "grep")):
            return line.strip()
    
    return None  # No command found

while True:
    user_input = input("Ask the LLM (or type 'exit'): ")
    if user_input.strip().lower() == 'exit':
        break

    prompt = f"I am using ubuntu, Translate this into a Linux shell command on how to :\n{user_input}"
    response = ask_llm(prompt)
    command = extract_command(response)

    if not command:
        print("⚠️ Could not extract a valid command from LLM response.")
        continue

    print(f"\nLLM Suggests:\n{command}\n")
    confirm = input("Do you want to run this? [y/N]: ")
    if confirm.lower() == 'y':
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"Error executing command: {e}")

