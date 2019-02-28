# Simply_Playlists
If you have issues with Youtube playlists repeating songs and overall not properly functioning then this is for you

## Before you run notes
This utilizes a light-weight chrome driver which can be used in conjuction to your main browser. If you use chrome as your browser of choice, then make sure that you have it open before running this program. Otherwise your mac will think that chrome is already open and use the light-weight chromedriver.
### Work-around
* Quit chrome and terminate the program. 
* Launch chrome, and re-run program.
* You should see a new instance of chrome open up, which you can place in a seperate window with terminal for cleanliness.
* Enjoy!
 

## Getting Started
MacOS Only for now
Verified to only work on python 3.7

### Prerequisites
* pip
* python 3.7

### Installing Dependencies
sudo pip install -r /path/to/Simply_Playlists/SimplyPlaylists/requirements.txt

### Running

#### set path  
cd /path/to/Simply_Playlists/SimplyPlaylists/

#### Run
./simply_playlists.py playlist1 playlist2

#### example of 2 playlists
./simply_playlists.py https://www.youtube.com/watch?v=_iGy3y9uW5Y&start_radio=1&list=RD_iGy3y9uW5Y https://www.youtube.com/watch?v=iI34LYmJ1Fs&list=PLuUrokoVSxlcHkpmmpa-RwKgPQMdbSvlb

#### example of 1 playlist
./simply_playlists.py https://www.youtube.com/watch?v=_iGy3y9uW5Y&start_radio=1&list=RD_iGy3y9uW5Y 
