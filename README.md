python -m PyQt6.uic.pyuic -x gui_fb.ui -o gui.py
import pip
pip.main(["install", "pygetwindow"])

pyinstaller --onefile -w --paths ./GenZalo_v1/ven-gen-zalo/Lib/site-packages --icon=./img/logo.ico main.py

    datas=[["C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\autoit\lib\\AutoItX3_x64.dll", "autoit\\lib"]],
    hiddenimports=["autoit.init", "autoit.autoit", "autoit.control", "autoit.process", "autoit.win" ],

pyinstaller main.spec

"autoit.init", "autoit.autoit", "autoit.control", "autoit.process", "autoit.win" 

a = Analysis(
    ['main.py'],
    pathex=['./GenZalo_v1/ven-gen-zalo/Lib/site-packages'],
    binaries=[],
    datas=[("C:\\Users\\ADMIN\\OneDrive\\Máy tính\\GenZalo_v1\\ven-gen-zalo\\Lib\site-packages\\autoit\\lib\\AutoItX3_x64.dll", "autoit\\lib"),("C:\\Users\\ADMIN\\OneDrive\\Máy tính\\GenZalo_v1\\ven-gen-zalo\\Lib\\site-packages\\selenium_stealth\\js\\utils.js", "selenium_stealth\\js")],
    hiddenimports=["autoit.init", "autoit.autoit", "autoit.control", "autoit.process", "autoit.win" ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=True,
    bootloader_ignore_signals=False,
    strip=None,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['img\\logo.ico'],
)