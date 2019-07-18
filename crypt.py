from Crypto.Cipher import AES
import os
import struct
from tkinter import filedialog
from getpass import getuser
from Crypto import Random
from tkinter import *


def key_generator():
    key = Random.new().read(32)
    save_path = filedialog.asksaveasfilename(initialdir=f"/Users/{getuser()}/", title="Save Key",
                                             filetypes=(("malza", "*.malza"), ("all files", "*.*")),
                                             confirmoverwrite=True)
    ekey = open(save_path, "wb")
    ekey.write(key)
    ekey.close()


def load_key():
    file_path = filedialog.askopenfilename(initialdir=f"/Users/{getuser()}/", title="Select KEY",
                                           filetypes=(("malza", "*.malza"), ("all files", "*.*")))
    key = open(file_path, "rb")
    key = key.read()
    return key


def encrypt(chunksize=2048):
    in_filename = filedialog.askopenfilename(initialdir=f"/Users/{getuser()}/", title="Select file")
    out_filename = in_filename + '.enc'
    file_size = os.path.getsize(in_filename)
    iv = os.urandom(16)
    key = load_key()
    aes = AES.new(key, AES.MODE_CBC, iv)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', file_size))
            outfile.write(iv)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(aes.encrypt(chunk))
    os.remove(in_filename)


def decrypt(chunksize=2048):
    in_filename = filedialog.askopenfilename(initialdir=f"/Users/{getuser()}/", title="Select file")
    out_filename = os.path.splitext(in_filename)[0]
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        key = load_key()
        aes = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(aes.decrypt(chunk))
            outfile.truncate(origsize)
    os.remove(in_filename)
