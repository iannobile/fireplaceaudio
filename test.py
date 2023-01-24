import unittest
import cherrypy
from main import HomeKitSpeaker
from contextlib import contextmanager
import requests
# Cherrypy unittest example from: https://schneide.blog/2017/02/06/integration-tests-with-cherrypy-and-requests/
# SPDX-FileCopyrightText: 2023 Ian Nobile
#
# SPDX-License-Identifier: MIT


@contextmanager
def run_server():
    cherrypy.engine.start()
    cherrypy.engine.wait(cherrypy.engine.states.STARTED)
    yield
    cherrypy.engine.exit()
    cherrypy.engine.block()


class TestEcho(unittest.TestCase):
    def test_index(self):
        cherrypy.tree.mount(HomeKitSpeaker(), '/api')
        with run_server():
            url = "http://127.0.0.1:8080/api"
            r = requests.get(url)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.text, "Fireplace Audio")

    def test_volumestatus(self):
        cherrypy.tree.mount(HomeKitSpeaker(), '/api')
        with run_server():
            url = "http://127.0.0.1:8080/api/volumestatus"
            r = requests.get(url)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.text, "19")

    def test_mutestatus(self):
        cherrypy.tree.mount(HomeKitSpeaker(), '/api')
        with run_server():
            url = "http://127.0.0.1:8080/api/mutestatus"
            r = requests.get(url)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.text, "1")

    def test_muteon(self):
        cherrypy.tree.mount(HomeKitSpeaker(), '/api')
        with run_server():
            url = "http://127.0.0.1:8080/api/muteon"
            r = requests.get(url)
            self.assertEqual(r.status_code, 200)
            url = "http://127.0.0.1:8080/api/mutestatus"
            r = requests.get(url)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.text, "0")

    def test_muteoff(self):
        cherrypy.tree.mount(HomeKitSpeaker(), '/api')
        with run_server():
            url = "http://127.0.0.1:8080/api/muteoff"
            r = requests.get(url)
            self.assertEqual(r.status_code, 200)
            url = "http://127.0.0.1:8080/api/mutestatus"
            r = requests.get(url)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.text, "1")

    def test_volumeupdate(self):
        cherrypy.tree.mount(HomeKitSpeaker(), '/api')
        with run_server():
            url = "http://127.0.0.1:8080/api/volumeupdate/50"
            r = requests.get(url)
            self.assertEqual(r.status_code, 200)
            url = "http://127.0.0.1:8080/api/volumestatus"
            r = requests.get(url)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.text, "50")


if __name__ == '__main__':
    unittest.main()
