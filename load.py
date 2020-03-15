import sys
import json
import requests
import threading
try:
    import Tkinter as tk # this is for python2
except:
    import tkinter as tk # this is for python3
from ttkHyperlinkLabel import HyperlinkLabel
import myNotebook as nb
from config import config

this = sys.modules[__name__]

def plugin_start3(plugin_dir):
    return plugin_start(plugin_dir)

def plugin_start(plugin_dir):
    """
    Load this plugin into EDMC
    """
    print("IDA-AX loaded! My plugin folder is " + format(plugin_dir))
    this.rememberkillcount = tk.IntVar(value=config.getint("RKC"))
    if this.rememberkillcount.get() == 0 :
        sys.stderr.write("Resetting IDA AX tally\n")
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
    print("Closing down")


def plugin_prefs(parent, cmdr, is_beta):
    """
    Return a TK Frame for adding to the EDMC settings dialog.
    """
    this.rememberkillcount = tk.IntVar(value=config.getint("RKC"))

    frame = nb.Frame(parent)

    plugin_label = nb.Label(frame, text="IDA-BGS AX plugin v0.31")
    plugin_label.grid(padx=10, row=0, column=0, sticky=tk.W)

    HyperlinkLabel(frame, text='Visit website', background=nb.Label().cget('background'), url='https://github.com/ZTiKnl/IDA-AX', underline=True).grid(padx=10, row=0, column=1, sticky=tk.W)

    empty_label = nb.Label(frame, text="")
    empty_label.grid(padx=10, row=1, column=0, columnspan=2, sticky=tk.W)

    remember_entry = nb.Checkbutton(frame, text=_('Remember kill count on EDMC restart'), variable=this.rememberkillcount)
    remember_entry.grid(padx=10, row=5, column=0, columnspan=2, sticky=tk.EW)

    return frame

def prefs_changed(cmdr, is_beta):
    """
    Save settings.
    """
    config.set('RKC', this.rememberkillcount.get())


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
    this.status = tk.Label(parent, text=statustext, anchor="w")

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