## Install
`sudo apt-get install python-dev python-imaging openssl libssl-dev ruby-full libcurl3-dev`
`sudo gem install githubstats`

NOTE: This repo uses a precompiled binary `rgbmatrix.so` for Raspbian on a Pi 3. If using another platform, please compile this by following (Adafruit's instructions)[https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices] and copy `rgbmatrix.so` into the project directory.

##CONFIGURATION
In `config.json`, set your github username, and optionally change the refresh interval (in seconds):
```
{
  "github_user": "blerchin",
  "refresh_interval": 3600
}
```

##RUNNING
Simply run `sudo ./draw.py`

To run on startup



