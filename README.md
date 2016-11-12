# RGB Github Stats
Show 7 weeks of github contributions on a Raspberry Pi [RGB LED Matrix Display](https://www.adafruit.com/product/2345).

## Install
`sudo apt-get install python-dev python-imaging openssl libssl-dev ruby-full libcurl3-dev`

`sudo gem install githubstats`

`git clone https://blerchin/rgb-githubstats.git`

NOTE: This repo uses a precompiled binary `rgbmatrix.so` for Raspbian on a Pi 3. If using another platform, please compile this by following [Adafruit's instructions](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices) and copy `rgbmatrix.so` into the project directory.

## Configure
In `config.json`, set your github username, and optionally change the refresh interval (in seconds):
```
{
  "github_user": "blerchin",
  "refresh_interval": 3600
}
```

## Run
Simply run `sudo ./draw.py`

To run on startup, add this line to the end of `~/.bashrc` (you could also do this with `init.d`, but mehhh...)
```
sudo PATH_TO_DIR/rgb-githubstats/service.py start
```



