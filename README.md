# Voice assistance Sloth 
RMIT University VietNam _ Software Engineering Project Management _ Group14_

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

Programming Language:
Python version 3.7 to 3.8

Modules:
```
*If you could not install these modules on Window by Pip, install PipWin module to install by using "pipwin install" instead of "pip install" 

SpeechRecognition>=3.8.1;
PyAudio>=0.2.11;
pygame~=1.9.6;
gTTS~=2.2.2;
pynput~=1.7.3
pyAutoGUI~=0.9.52
playsound>=1.2.2
psutil>=5.8.0
pywinauto>=0.6.8
selenium>=3.141.0
webdriver_manager>=3.4.2

```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Step 1: Install modules from command line
 - pip install SpeechRecognition 
 - pip install pygame==1.9.6
 - pip install gTTS
 - pip install playsound
 - pip install pynput
 - pip install pyAutoGUI
 - pip install PyAudio
 - pip install pywinauto
 - pip install selenium
 - pip install webdriver_manager

```

## Current Functions/ Feature: 

Explain how to run the functions for this system

// All keywords to trigger functions in Process_respond.py file
1. Create New File/ Folder with voice: (Just create folder now)
   - Start Program
   - Speak "Create" + Name Folder want to create
2. Open Existing File/ Folder with voice: 
   - Start Program
   - Speak "Open" + Name App / File / Folder based on setup Path
3. Delete Existing File/ Folder with voice: 
   - Start Program
   - Speak "Delete" + Name App / File / Folder based on setup Path
   - Get List of apps/folders/files
   - Answer Yes if want to delete/ No if deny
4. Get Info of Existing/ Folder with voice: 
   - Start Program 
   - Click in File (Not done with cursor yet/ have to click specific file)
   - Speak Information/show to get info 

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Not doing any tests yet
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - SpeechRecognition to recognize speech
* [PyAudio](https://pypi.org/project/PyAudio/) - PyAudio control
* [PyGame](https://pypi.org/project/pygame/1.9.6/) - Support Music player / version 1.9.6 to stable mp3 file
* [gTTS](https://pypi.org/project/gTTS/) - Google Text to Speech api
* [pynput](https://pypi.org/project/pynput/) - Control and monitor keyboard/ mouse input devices
* [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) - programmatically control the mouse & keyboard
* [PyWinAuto](https://pypi.org/project/pywinauto/) - send mouse and keyboard actions to windows dialogs and controls, but has support for more complex controls also
* [selenium](https://pypi.org/project/selenium/) - automate web browser interaction from Python
* [webdriver_manager](https://pypi.org/project/webdriver-manager/) - simplify management of binary drivers for different browsers

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Version


## Authors

* **Quach Gia Vi** - *Scrum Master- Developer* - (https://github.com/s3757317)
* **Bui Manh Dai Duong** - *UI/UX Designer- Developer* - (https://github.com/koumi15cancer)
* **Ha Gia Bao** - *Leading Developer* - (https://github.com/baogia0912)
* **Nguyen Bao Tri** - *Tester - Documentation supervisor* - (https://github.com/nguyenbaotri)


See also the list of [contributors](https://github.com/LazySlobs/SEPM-Sloth/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

