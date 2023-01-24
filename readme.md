# Fireplace Audio
Feeling nostalgic for the fireplace of my youth, but not wanting to deal with the pain of a real fireplace
I recently bought an electric fireplace. It's good at giving me the feeling of a fireplace, but the one thing it was missing
was the calming noise of a crackling fire.

There are a couple of solutions available, but none of them met my requirements:
1. Used parts I have on hand.
2. Works with HomeKit.
3. Not sound terrible.

I decided to repurpose some old desktop pc speakers, a Raspberry Pi Zero W, and a USB soundcard for the hardware,
and some simple Python magic to handling playing the audio and controlling things via HTTP. Homebridge and 
the homebridge-http-lightbulb to control the audio playback and volume.

For the fireplace audio file, there are plenty of quality fireplace sound files on the Internet, or you can make your own.

### Hardware

* Raspberry Pi Zero W or Raspberry Pi Zero 2 W
* Compatible USB audio card
* External 3.5mm desktop speakers (check specs of USB audio Card for power requirements)
* 64GB or larger microSD card.
* MicroUSB adapter or hub

### Barely Organized Instructions

* Install raspberry pi os Lite on an SD card
* Configure username, wifi and timezone.
* Put the card in the pi zero and boot it up.

#### Update OS and Packages

* sudo apt update
* sudo apt full-upgrade
* reboot

#### Install Pip

* sudo apt-get install python3-pip
* python -m pip install --upgrade pip

#### Create Python environment

* mkdir ~/fireplaceaudio
* python -m venv venv
* cd ~/fireplaceaudio:wq/venv/bin
* source activate

#### Checkout the source from Github

* git clone ....

#### Install Requirements

* python -m pip install -r requirements.txt
* sudo apt install python3-sdl2

#### Install Supervisord

* sudo apt install supervisor
* Put fireplaceaudio.conf in /etc/supervisor/conf.d
* Update the file with the path and username
* sudo supervisorctl update

#### Configure Audio Output.

* Make sure the USB audio card is plugged into the Raspberry Pi
* sudo raspi-config
* System Options
* Audio
* Specify the usb audio card.

Get the sound card id sound usb sound card
* sudo aplay -l
* get sound card id

Edit sudo vi /usr/share/alsa/alsa.conf
* change from 0 to 1
* defaults.ctl.card
* defaults.pcm.card
* save file.

Confirm audio source is the usb device.
* sudo alsamixer

Test speaker
* speaker-test -c2

#### Install homebridge

https://github.com/homebridge/homebridge/wiki/Install-Homebridge-on-Raspbian
sudo apt-get install homebridge

Configure homebridge
install http-lightbulb
https://github.com/Supereg/homebridge-http-lightbulb
sudo npm install -g homebridge-http-lightbulb
Use the config.json to configure the plugin.


#### Future improvements

* Allow uploading of audio file.
* Running on microprocessor board.
* Dynamic audio based on fireplace activity.



MIT License Copyright (c) 2023 Ian Nobile

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice (including the next
paragraph) shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.