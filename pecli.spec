# -*- mode: python -*-

block_cipher = None


a = Analysis(['pecli.py'],
             pathex=['C:\\tools\\pe'],
             binaries=[(r'C:\Program Files (x86)\Python36-32\Lib\site-packages\ssdeep\bin','.')],
             datas=[(r'.\pe\plugins','pe\plugins'),(r'.\pe\lib','pe\lib'),(r'.\pe\data','pe\data')],
             hiddenimports=['yara','pefile','json','ssdeep'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pecli',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
