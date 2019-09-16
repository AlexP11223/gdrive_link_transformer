# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['gdrive_link_transformer/gdrive_direct_link.py'],
             binaries=[],
             datas=[('resources', './resources')],
             hiddenimports=['plyer.platforms.win.notification', 'plyer.platforms.linux.notification', 'plyer.platforms.macosx.notification'],
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
          [],
          exclude_binaries=True,
          name='gdrive_direct_link',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
		  icon='resources/icon.ico',
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='gdrive_direct_link')
