all: gui.py
	chmod +x gui.py
run:
	python gui.py

installer:
	sudo apt-get install python3-pip
	pip3 install tkinter

delete:
	pip uninstall tkinter