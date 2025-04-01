# onrobot-rg6

Controller for OnRobot RG2 and RG6 grippers.

# Requirements

- Python 3.7.3
  - pymodbus==2.5.3

# Installation

	$ git clone https://github.com/Kazuma-Onishi/onrobot-rg.git; cd onrobot-rg
	$ pip install -r requirements.txt

# Usage

1. Connect the cable between Compute Box and Tool Changer.
2. Connect an ethernet cable between Compute Box and your computer.
3. Execute demo script as below  
    `$ rosrun onrobot-rg gripper_controller.py`

# Author / Contributor

<!-- Originaly: [Takuya Kiyokawa](https://takuya-ki.github.io/) -->
Maintain: Kazuma Onishi

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
