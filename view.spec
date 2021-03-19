# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['view.py'],
             pathex=['/Users/yk/python_practice/study-03-desktop-01'],
             binaries=[],
             datas=[('/Users/yk/python_practice/venv/lib/python3.7/site-packages/eel/eel.js', 'eel'), ('html', 'html')],
             hiddenimports=['bottle_websocket'],
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
          name='view',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
