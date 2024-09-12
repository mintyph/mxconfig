import os
import time
import subprocess
import sys

def print_banner():
    banner = """
⠄⠄⠄⠄⢠⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⣿⣿⣆⠄⠄⠄
⠄⠄⣼⢀⣿⣿⣿⣿⣏⡏⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣧⢻⣿⣿⣿⣿⡆⠄⠄
⠄⠄⡟⣼⣿⣿⣿⣿⣿⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣇⢻⣿⣿⣿⣿⠄⠄
⠄⢰⠃⣿⣿⠿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠙⠿⣿⣿⣿⣿⣿⠄⢿⣿⣿⣿⡄⠄
⠄⢸⢠⣿⣿⣧⡙⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠈⠛⢿⣿⣿⡇⠸⣿⡿⣸⡇⠄
⠄⠈⡆⣿⣿⣿⣿⣦⡙⠳⠄⠄⠄⠄⠄⠄⢀⣠⣤⣀⣈⠙⠃⠄⠄⠿⢇⣿⡇⠄
⠄⠄⡇⢿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⣠⣶⣿⣿⣿⣿⣿⣿⣷⣆⡀⣼⣿⡇⠄
⠄⠄⢹⡘⣿⣿⣿⢿⣷⡀⠄⢀⣴⣾⣟⠉⠉⠉⠉⣽⣿⣿⣿⣿⠇⢹⣿⠃⠄
⠄⠄⠄⢷⡘⢿⣿⣎⢻⣷⠰⣿⣿⣿⣿⣦⣀⣀⣴⣿⣿⣿⠟⢫⡾⢸⡟⠄.
⠄⠄⠄⠄⠻⣦⡙⠿⣧⠙⢷⠙⠻⠿⢿⡿⠿⠿⠛⠋⠉⠄⠂⠘⠁⠞⠄⠄⠄
⠄⠄⠄⠄⠄⠈⠙⠑⣠⣤⣴⡖⠄⠿⣋⣉⣉⡁⠄⢾⣦⠄⠄⠄⠄⠄⠄⠄⠄
    MXNT ParrotOS Settings.
    """
    print(banner)
    time.sleep(3)

def check_sudo():
    if os.geteuid() != 0:
        print("This script must be run as root.")
        sys.exit(1)

def install_vscodium():
    print("Installing VSCodium...")
    subprocess.run(["wget", "https://github.com/VSCodium/vscodium/releases/download/1.71.0.0/codium_1.71.0.0_amd64.deb"], check=True)
    subprocess.run(["sudo", "dpkg", "-i", "codium_1.71.0.0_amd64.deb"], check=True)
    subprocess.run(["sudo", "apt", "-f", "install", "-y"], check=True)

def install_packages():
    home_dir = os.path.expanduser("~")

    print("Installing tmux...")
    subprocess.run(["sudo", "apt", "install", "-y", "tmux"], check=True)

    print("Configuring tmux...")
    tmux_config = """
    # ~/.tmux.conf
    bind d split-window -h
    bind w split-window -v
    bind c copy-mode
    bind v paste-buffer
    """
    with open(f"{home_dir}/.tmux.conf", "w") as f:
        f.write(tmux_config)

    print("Setting up tmux to start automatically...")
    if not os.system("grep -qxF 'tmux' ~/.bashrc"):
        with open(f"{home_dir}/.bashrc", "a") as f:
            f.write("tmux\n")

    print("Updating and upgrading system...")
    subprocess.run(["sudo", "apt", "update", "-y"], check=True)
    subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)

    print("Installing burpsuite...")
    subprocess.run(["sudo", "apt", "install", "-y", "burpsuite"], check=True)

    install_vscodium()

    print("All tasks completed!")

def main():
    check_sudo()
    print_banner()
    install_packages()

if __name__ == "__main__":
    main()
