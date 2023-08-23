# ArkUtil | v0.1 | Limited
- Created to quickly mock up multiple servers
- Mainly created to do +4 on ports for each servers
    - Server    (GamePort, RawPort, QueryPort, RCONPort)
    - TheIsland (7777, 7778, 7779, 7780)
    - RagnaRock (7781, 7782, 7783, 7784)
    - etc..
- Copies everything as a profile into [Ark Server Manager](https://arkservermanager.freeforums.net/thread/5193/downloads)
- Copies `Game.ini` & `GameUserSettings.ini` to the installation folders.
- Best way to utilize this tool is to configure your server manually via ASM, then copy the generated `.ini` & `.profile` files into this tool data folder and start from there.
---
### Requirements
- Windows
- Python
---
### Install
`pip install requirements.txt`
---
### Setup
- Use & fill `.env.example`
- Make a copy of the file and name it `.env`
- Fill the paths and your settings
---
### Usage
`"C:/Program Files/Python311/python.exe" d:/ArkUtil/src/app.py`
