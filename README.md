# PE / PECLI

Tool to analyze PE files in python 3. Current features :
* Show information about the file (import, exports, resources)
* Calculate Hashes (md5, sha, ssdeep, imphash)
* Search for interesting information in the file (abnormal resources, peid...)
* Dump sections or resources
* Check size
* Search for a string in the file

## Binary Release

The main purpose of the fork from Te-k/pe was to provide a Windows 32-bit ready PyInstaller based single binary that includes the `libmagic` and` ssdeep` precompiled windows dlls

https://github.com/shadowbq/pecli/releases

## `Pip` local Installation

```
git clone git@github.com:shadowbq/pecli.git
cd pecli
pip install .
```

## How to

PE works with plugin, like `pe PLUGIN FILE`

Current plugins includes :
* **info** : Extract info from the PE file
* **dump** : Dump resource or section of the file
* **search** : Search for a string in a PE file
* **checksize** : Check size of the PE file
* **check** :  Check for weird stuff in the PE file
* **nonpe** : Provide Basic information about Non-PE files

Example :
```
C:\tools\pe>dist\pecli.exe info c:\Windows\system32\calc.exe
Metadata
================================================================================
MD5:           0975ee4bd09e87c94861f69e4aa44b7a
SHA1:          64029e26a179b64951ca580a155288b6ff002a55
SHA256:        7f8aa55beae4aee0da0f32b8d67b3d600103fedd99c6e114625f82de8d14d5c7
IMPHASH:       ba072a972fe6c47c8cf7a0347bb0af7a
SSDEEP:        384:B53k8oXcm/s0WSQYWXiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiLiiiiiriiii9:rTAs16
Size:          26112 bytes
Type:          PE32 executable (GUI) Intel 80386, for MS Windows
Compile Time:  2044-11-19 02:16:00 (UTC - 0x8CDA9260)
Observered Path: c:\Windows\system32\calc.exe
Observered Filename: calc.exe
Entry point:   0x401b60 (section .text)
Debug Information: calc.pdb

Sections
================================================================================
Name       VirtSize  VirtAddr  RawSize   RawAddr   Entropy  md5
.text      0xf44     0x1000    0x400     0x1000    5.6966   0a3a95a484c82943ee7438dc68d75840
.data      0x3a4     0x2000    0x1400    0x200     0.2404   5e315964688a25f9be590eed9857822a
.idata     0x4a8     0x3000    0x1600    0x600     4.0631   571af6070a6f29e2124544d91cd59469
.rsrc      0x4708    0x4000    0x1c00    0x4800    2.8124   ee1cd8d1270fb17cdda278ce4cb1ee9c
.reloc     0x16c     0x9000    0x6400    0x200     4.9277   507df10404b6bfdc0debcbc5f356e174


Imports
================================================================================
SHELL32.dll
        0x403038 ShellExecuteW
KERNEL32.dll
        0x403010 SetUnhandledExceptionFilter
        0x403014 GetCurrentProcess
        0x403018 TerminateProcess
        0x40301c UnhandledExceptionFilter
        0x403020 GetCurrentProcessId
        0x403024 GetCurrentThreadId
        0x403028 GetSystemTimeAsFileTime
        0x40302c GetTickCount
        0x403030 QueryPerformanceCounter
msvcrt.dll
        0x403058 _amsg_exit
        0x40305c __p__fmode
        0x403060 __setusermatherr
        0x403064 _initterm
        0x403068 _wcmdln
        0x40306c ?terminate@@YAXXZ
        0x403070 _controlfp
        0x403074 _exit
        0x403078 exit
        0x40307c __p__commode
        0x403080 _XcptFilter
        0x403084 __set_app_type
        0x403088 _except_handler4_common
        0x40308c __wgetmainargs
        0x403090 _cexit
ADVAPI32.dll
        0x403000 EventSetInformation
        0x403004 EventWriteTransfer
        0x403008 EventRegister
api-ms-win-core-synch-l1-2-0.dll
        0x403050 Sleep
api-ms-win-core-processthreads-l1-1-0.dll
        0x403048 GetStartupInfoW
api-ms-win-core-libraryloader-l1-2-0.dll
        0x403040 GetModuleHandleW


Resources:
================================================================================
Id           Name    Size      Lang           Sublang           Type           MD5
3-1-1033     None    1128 B    LANG_ENGLISH   SUBLANG_ENGLISH_US GLS_BINARY_LSB_FIRST 339d6ef766e3e959cb6a80c5a0006077
3-2-1033     None    536 B     LANG_ENGLISH   SUBLANG_ENGLISH_US PNG image data, 256 x 256, 8-bit grayscale, non-interlaced 84ae61b758be82a627ebbd846f988d34
3-3-1033     None    4264 B    LANG_ENGLISH   SUBLANG_ENGLISH_US dBase IV DBT of @.DBF, block length 4096, next free block index 40, next free block 4282795590, next used block 4282795590 762ddcf4fb3a4f57a4a1849b47324a2c
3-4-1033     None    9640 B    LANG_ENGLISH   SUBLANG_ENGLISH_US dBase IV DBT of `.DBF, block length 9216, next free block index 40, next free block 4282795590, next used block 4282795590 9ee2a3afd25682b394fe54b6db182103
14-IDI_CALC_ICON-1033 None    62 B      LANG_ENGLISH   SUBLANG_ENGLISH_US data           0a3aabb4ec6e9901a7e2d57c8b6407c2
16-1-1033    None    900 B     LANG_ENGLISH   SUBLANG_ENGLISH_US data           724b434dc387788cabe519629212f7a8
24-1-1033    None    1167 B    LANG_ENGLISH   SUBLANG_ENGLISH_US XML 1.0 document, ASCII text, with CRLF line terminators 84e38f8bb6e3c6f35380f3373050c013

```
## yara scanning
```
$ pecli.py check playlib.exe
Running checks on playlib.exe:
[+] Abnormal section names: .enigma1 .enigma2
[+] Suspicious section's entropy: .enigma1 - 7.931
[+] Known malicious sections
	-.enigma1: Enigma Virtual Box protector
	-.enigma2: Enigma Virtual Box protector
[+] 200 extra bytes in the file
[+] TLS Callback: 0x446bb0
[+] PE header in sections .enigma2
[+] Known suspicious import hash: Enigma VirtualBox
```
## Non PE support
```
pecli.py nonpe pecli.py
MD5:           eed4773af2db23c9cad9315e987f2de3
SHA1:          1d37a439e16321d7b10d2ac094d26aececee14b0
SHA256:        a0976723c83fecda0bb580a558e7401d74341ae8bbef0be429d2994208fde88b
IMPHASH:       (unavailable)
SSDEEP:        3:TFKL9PANGeGFUIVBXILuXZQRteJXBCSLYKedLWBXFHQMTbZVFKXBckHhAj5EMCCR:J07ecUIVOyXceJXBCQ0KXFHQMTNVQxbe
Size:          190 bytes
Type:          a /usr/bin/env python script, ASCII text executable, with CRLF line terminators
Compile Time:  (unavailable)
Observered Path: C:\tools\pe\pecli.py
Observered Filename: pecli.py
```

## License

This tool is published under MIT License

## Similar tools

* [PEScanner](https://github.com/Te-k/analyst-scripts/blob/master/pe/pescanner.py) published by Michael Ligh for the [Malware Analyst's Cookbook](https://www.wiley.com/en-us/Malware+Analyst%27s+Cookbook+and+DVD%3A+Tools+and+Techniques+for+Fighting+Malicious+Code-p-9780470613030) (python2 only)
* [Manalyze](https://github.com/JusticeRage/Manalyze)
* On Windows, [PeStudio](https://www.winitor.com/), [PEView](http://wjradburn.com/software/) and [Resource Hacker](http://www.angusj.com/resourcehacker/)
