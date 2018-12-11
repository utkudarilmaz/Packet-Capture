import os
import subprocess
import shlex
import time
import threading


class CaptureAndPost():

    def __init__(self, path="/root"):

        self.path = path
        os.chdir(self.path)

        self.captureCommand = "tshark -O icmp -T json -w log.pcap"

        self.convertPcapToTextCommand = "tshark -r log.pcap > log.txt"

        self.getSourcesCommand = "cat log.txt | grep ' request ' | cut -dI -f0 | cut -c 21-33 >> source"
        self.getTargetCommand = "cat log.txt | grep ' request ' | cut -dI -f0 | cut -c 36- >> target"

    def start(self):

        args = shlex.split(self.captureCommand)
        captureProcess = subprocess.Popen(args, cwd=self.path)
        self.capture()
        self.analyz() ## Thread


    def capture(self):
        while True:
            time.sleep(10)

            convertArgs = shlex.split(self.convertPcapToTextCommand)
            convertProc = subprocess.Popen(convertArgs, cwd=self.path)
            convertProc.wait()

            getSourcesArgs = shlex.split(self.getSourcesCommand)
            getSourcesProc = subprocess.Popen(getSourcesArgs, cwd=self.path)
            getSourcesProc.wait()

            getTargetArgs = shlex.split(self.getTargetCommand)
            getTargetProc = subprocess.Popen(getTargetArgs, cwd=self.path)
            getTargetProc.wait()
