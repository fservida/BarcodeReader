# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\francesco.HOGWARTS\\PycharmProjects\\BarcodeReader'],
             binaries=[
             ('C:\\tools\\miniconda3\\envs\\BarcodeReader\\Lib\\site-packages\\pyzbar\\libiconv.dll', 'pyzbar'),
             ('C:\\tools\\miniconda3\\envs\\BarcodeReader\\Lib\\site-packages\\pyzbar\\libzbar-64.dll', 'pyzbar'),
             ],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='BarcodeReader',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
