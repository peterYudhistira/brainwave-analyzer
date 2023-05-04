Things worth taking note of :
- Run main.py, if anything comes up just pip install whatever's missing.
- The loading function makes use of QThread -- that is, it is run as another thread so as not to freeze the GUI.
- The UI is made with Qt Designer and saved in the directory 'ui'. The command `pyuic6 -x -o [.ui file name] [.py file name ]` is used to generate a python file based on the established design.
- I promised 30 minutes. I delivered within +/- 45 minutes. TIme well spent. 