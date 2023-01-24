# SPDX-FileCopyrightText: 2023 Ian Nobile
#
# SPDX-License-Identifier: MIT
import cherrypy
import portend
from pygame import mixer

filename = 'fireplace.wav'


class HomeKitSpeaker(object):
    """
    Homebridge HomeKit Speaker API class.
    Plays the passed filename on loop and can be controlled via http or integrated into Homebridge using the
    https://github.com/Supereg/homebridge-http-lightbulb Homebridge plugin.

    """
    mute_status = 1

    def __init__(self):
        # Load audio file
        mixer.init()
        mixer.music.load(filename)
        mixer.music.set_volume(0.2)
        # Loop audio file
        mixer.music.play(-1)

    @cherrypy.expose
    def index(self):
        return "Fireplace Audio"

    @cherrypy.expose
    def muteon(self):
        """
        Mute audio
        :return:
        """
        mixer.music.pause()
        self.mute_status = 0

    @cherrypy.expose
    def muteoff(self):
        """
        Unmute audio
        :return:
        """
        mixer.music.unpause()
        self.mute_status = 1

    @cherrypy.expose
    def mutestatus(self):
        """
        Returns mute status.
        :return:
        """
        return str(self.mute_status)

    @cherrypy.expose
    def volumestatus(self):
        """
        Returns volume level.
        :return:
        """
        volume_scale = (int(mixer.music.get_volume() * 100))
        return str(volume_scale)

    @cherrypy.expose
    def volumeupdate(self, volume):
        """
        Sets the volume level.
        :return:
        """
        if 0 < int(volume) <= 100:
            new_volume = int(volume) / 100
            # print(f'volume {new_volume}')
            mixer.music.stop()
            mixer.music.set_volume(new_volume)
            # Restart audio
            mixer.music.play(-1)


if __name__ == '__main__':
    """
    Main function
    """
    try:
        # Bind to every address, NOTE: You should specify what address you're going to use outside of development.
        cherrypy.config.update({'server.socket_host': '0.0.0.0',
                                'server.socket_port': 8080,
                                })
        cherrypy.quickstart(HomeKitSpeaker(), '/api')
    except (portend.Timeout, TypeError):
        pass
