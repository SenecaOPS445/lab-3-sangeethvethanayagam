#!/usr/bin/env python3

# Author ID: 189353238

import subprocess



def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}' ")
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

free_space()