import sys
import json
import requests
import threading
import Tkinter as tk
import myNotebook as nb
from config import config

this = sys.modules[__name__]

def plugin_start(plugin_dir):
    """
    Load this plugin into EDMC
    """
    print "IDA-AX loaded! My plugin folder is {}".format(plugin_dir.encode("utf-8"))
    config.set('killtallys', 0)
    config.set('killtallyc', 0)
    config.set('killtallyb', 0)
    config.set('killtallym', 0)
    config.set('killtallyh', 0)
    return "IDA-AX"

def plugin_stop():
    """
    EDMC is closing
    """
    print "Closing down"

def plugin_app(parent):
    """
    Create a pair of TK widgets for the EDMC main window
    """
    this.kts = tk.IntVar(value=config.getint("killtallys"))
    this.ktc = tk.IntVar(value=config.getint("killtallyc"))
    this.ktb = tk.IntVar(value=config.getint("killtallyb"))
    this.ktm = tk.IntVar(value=config.getint("killtallym"))
    this.kth = tk.IntVar(value=config.getint("killtallyh"))

    label = tk.Label(parent, text="IDA AX:")
    statustext = 'S:' + str(this.kts.get()) + ' | C:' + str(this.ktc.get()) + ' | B:' + str(this.ktb.get()) + ' | M:' + str(this.ktm.get()) + ' | H:' + str(this.kth.get())
    this.status = tk.Label(parent, text=statustext)

    return (label, this.status)

def journal_entry(cmdr, is_beta, system, station, entry, state):
    """
    Evaluate data and transfer to https://ida-bgs.ztik.nl/api/input
    """
    this.kts = tk.IntVar(value=config.getint("killtallys"))
    this.ktc = tk.IntVar(value=config.getint("killtallyc"))
    this.ktb = tk.IntVar(value=config.getint("killtallyb"))
    this.ktm = tk.IntVar(value=config.getint("killtallym"))
    this.kth = tk.IntVar(value=config.getint("killtallyh"))

    if entry['event'] == 'FactionKillBond':
        # Bounty received
        if entry['VictimFaction'] == '$faction_Thargoid;':
            # Bounty received for Thargoid faction
            if entry['Reward'] == 10000:
                #Bounty received equals Scout value
                config.set('killtallys', (this.kts.get() + 1))
                this.kts = tk.IntVar(value=config.getint("killtallys"))
            if entry['Reward'] == 2000000:
                #Bounty received equals Cyclops value
                config.set('killtallyc', (this.ktc.get() + 1))
                this.ktc = tk.IntVar(value=config.getint("killtallyc"))
            if entry['Reward'] == 6000000:
                #Bounty received equals Basilisk value
                config.set('killtallyb', (this.ktb.get() + 1))
                this.ktb = tk.IntVar(value=config.getint("killtallyb"))
            if entry['Reward'] == 10000000:
                #Bounty received equals Medusa value
                config.set('killtallym', (this.ktm.get() + 1))
                this.ktm = tk.IntVar(value=config.getint("killtallym"))
            if entry['Reward'] == 15000000:
                #Bounty received equals Hydra value
                config.set('killtallyh', (this.kth.get() + 1))
                this.kth = tk.IntVar(value=config.getint("killtallyh"))

            statustext = 'S:' + str(this.kts.get()) + ' | C:' + str(this.ktc.get()) + ' | B:' + str(this.ktb.get()) + ' | M:' + str(this.ktm.get()) + ' | H:' + str(this.kth.get())
            this.status['text'] = statustext
            sys.stderr.write("IDA AX tally:\n")
            sys.stderr.write(str(statustext) + "\n")
            sys.stderr.write("-------------\n")