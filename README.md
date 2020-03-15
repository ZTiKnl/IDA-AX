# IDA-AX
An EDMC plugin that displays AX kill count

## Version  
Version 0.31  

## What it does:  
Count each type of Thargoid kill, Scout, Cyclops, Basilisk, Medusa & Hydra.  
The number is displayed in the EDMC main window.  

There is an extra row in the main window of EDMC, labeled `IDA-AX` with the counts: `S:0 | C:0 | B:0 | M:0 | H:0`  
  S = Scout  
  C = Cyclops  
  B = Basilisk  
  M = Medusa  
  H = Hydra  

It displays the killcounts ~~for as long as EDMC is open, all stats are deleted on restart of EDMC~~.  
It is NOT affected by game client closure/crash, it will remember the stats as long as EDMC remains open.  
If you place a checkmark in the settings tab, it will remember counts also on EDMC restart.  
*In case of an EDMC crash, you can always read back the killcounts in the log file `%TMP%\EDMarketConnector.log` (this file is cleared on EDMC startup)*  

Warning: It does NOT trigger AX kills made in wing it appears, further testing is required.  
It is possible that only the wingmember who makes the first or last hit on target gets the journal entry that is required for the counter add a kill.  

## How to use:  
1. Clone the repo to the EDMC plugin folder, or download and unzip to the EDMC plugin folder  
   (default: `c:\Users\%USERNAME%\AppData\Local\EDMarketConnector\plugins`)  
2. Start up EDMC  

## Disclaimer
This plugin is still under construction, ~~bugs~~ new features WILL appear unexpectedly.  
Patches are always welcome.  

## Thanks
VVaves, TOPBLAZER85, CrazyGolm & Chuckination, devnull, Plusran  