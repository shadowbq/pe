import os
import sys
import hashlib
import ssdeep
import magic
import ntpath

from pe.plugins.base import Plugin

class PluginNonpe(Plugin):
    name = "nonpe"
    description = "Give Basic information about Non-PE file"

    def run(self, args, data):
            
        """Display md5, sha1 and sh256 of the data given"""
        for algo in ["md5", "sha1", "sha256"]:
            m = getattr(hashlib, algo)()
            m.update(data)
            print("%-14s %s" % (algo.upper()+":", m.hexdigest()))
        print("%-14s %s" % ("IMPHASH:", "(unavailable)"))
        print("%-14s %s" %("SSDEEP:", ssdeep.hash_from_file(args.PEFILE)))
        print("Size:          %d bytes" % len(data))
        print("Type:          %s" % magic.from_buffer(data))
        print("Compile Time:  %s" % "(unavailable)")
        print("Observered Path: %s" % os.path.abspath(args.PEFILE))
        print("Observered Filename: %s" % ntpath.basename(args.PEFILE))