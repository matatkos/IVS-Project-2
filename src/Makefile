.PHONY: all initialization pack clean test doc run install
all: initialization run
	chmod +x gui.py

initialization:
	sudo apt-get install python3-tk
	sudo apt-get install python3-pytest
	sudo apt-get install doxygen

pack: doc clean
	mkdir ../../doc
	mv ../doc/html ../../doc
	mkdir ../../install
	mkdir ../../repo
	cp -r ../* ../../repo
	mkdir ../../xbuchm02_xsnope04_xjokay00_xspace39
	mv ../../repo ../../doc ../../install ../../xbuchm02_xsnope04_xjokay00_xspace39
	cd ../.. && zip -r xbuchm02_xsnope04_xjokay00_xspace39.zip xbuchm02_xsnope04_xjokay00_xspace39

clean:
	rm -rf ../installer/tmp
	rm -rf ../installer/usr
	rm -rf ../../xbuchm02_xsnope04_xjokay00_xspace39/

run:
	python3 gui.py
doc:
	rm -rf ../doc
	mkdir ../doc
	cd ../doc && doxygen ../src/Doxyfile

test: test_mathlib.py
	pytest test_mathlib.py

