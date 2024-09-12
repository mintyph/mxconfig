# MXNT ParrotOS Setup Script

This Python script automates the setup of a Parrot OS environment by updating/upgrading the system and configuring it according to my personal standards (currently i use the HTB edition). The script is a work in progress and may be extended with additional features in the future.

## Features

- **Package Installation:** Installs and configures essential tools including tmux, Burp Suite, and VSCodium.
- **Configuration Management:** Sets up tmux with custom key bindings and ensures tmux starts automatically in the terminal.
- **System Updates:** Performs system updates and upgrades to keep your environment up-to-date.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mintyph/mxconfig.git
   cd mxconfig
   sudo python3 main.py
