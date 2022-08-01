██████╗░██╗░░░██╗████████╗██╗░░░██╗██████╗░███████╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░░██║██╔══██╗██╔════╝
██████╔╝░╚████╔╝░░░░██║░░░██║░░░██║██████╦╝█████╗░░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░
██║░░░░░░░░██║░░░░░░██║░░░╚██████╔╝██████╦╝███████╗
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░░╚═════╝░╚═════╝░╚══════╝


Download YouTube videos and music using pytube library!

#### Folder
This is the folder where the files are stored.
```
├── Download # These are the outputs what you've download
|    ├── YouTube Audio
|    ├── YouTube Video
├── pytb.py #This is our pytube downloader
```
#### Installation
- We need a virtual environment for our project to build up the environment. [click here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) docs virtual environment
```
virtualenv env
```
- Activating virtual environment
```
source env/bin/activate
``` 
- Installing requirements
```
pip install -r requirements.txt
```

#### Bulk Download
- Download all the videos in a playlist, insert your urls inside the ```bulk.txt``` file.
