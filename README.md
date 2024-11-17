# ARCHIVE-FOLLIN

![In aid of Pancreatic Cancer UK](Resources/Images/pancreatic_cancer_uk_in_aid_of.png)

Sadly Geoff Follin passed away in May 2024 after being diagnosed with pancreatic and liver cancer just three weeks before. I've been good friends with the Follin brothers since we worked together at Software Creations. His death has hit us all really hard. Pancreatic cancer is brutal.

I've decided to run the Manchester 10K next May in his memory and in aid of Pancreatic Cancer UK.

[Please visit my giving page for more details on this, and consider a small donation.](https://www.justgiving.com/page/dean-belfield-1719662311154)

## Introduction

I was donated a box of 3" floppy disks by Tim Follin a couple of years ago that contained backups of the music he wrote in the late 80s and early 90s whilst working at Software Creations in Manchester (UK).

The music and sound effects were hand-coded by Tim and Geoff Follin in assembler as a series of DEFB's representing note pitch and duration for each channel. This data can also contains commands, for example to loop a sequence, call a subroutine or switch on an effect.

Once completed, their music source was included in the intended game along with a small music driver, also written in assembler.

This could then be called from within the game for both in-game music and sound effects.

The assembler/editor was a custom application written by Mike Webb / Ste Ruddy and ran on a Tatung Einstein TC-01.

The resultant source code was saved out on said 3" floppy disks.

## The challenge

I used to work with Tim at Software Creations, so am reasonably familiar with the workflow.

I was hoping that:

1. The disks were still readable.
2. I could find a 3" disk drive and/or working Tatung Einstein to read the disks.
3. The disks contained a copy of the editor/assembler.
4. The source code was either saved as plain text, or easy to detokenise.

I ended up purchasing a Tatung Einstein TC-01 for a reasonable price off eBay. They don't come up very often and I got lucky both in terms of the condition unit (which is excellent) and the price paid.

## Reading the disks

For the most part the disks are fine.

The disks target the C64 (6502) and Amstrad CPC/Spectrum 128K (Z80).

One disk is physically damaged - it has a damaged shutter, which I need to repair, and there was the odd file that didn't read correctly.

There are a couple of disks that have unreadable sides - reporting a missing sector 0. I suspect that these are not formatted for the Einstein, maybe the Spectrum +3 or Amstrad CPC6128.

I've also noted that there are a handful of zero-byte files, which puzzled me at first. The working hypothesis is that as part of the workflow, disks were copied to a silicon RAM disk plugged into the Einstein at the start of the day, and edited/assembled from there as it was far quicker than working from floppy. The silicon disks were volatile, so at the end of the day, or at critical points during development, it was backed up to floppy. I suspect that this would sometimes result in a disk full error, with zero-byte files being written out for any files that didn't fit.

I've confirmed with Kevin Edwards, who is using GreaseWeazle / Kryoflux to copy another batch of 3" floppies authored on the Einstein and he's noticed the same.

## Transferring the data

Andy Toone had written [an excellent guide](https://feertech.com/legion/retro/computer/2021/06/08/connecting-over-serial.html) on transferring data from a Tatung Einstein to a PC, which proved invaluable.

I was able to procure a serial cable from eBay for a reasonable price from [this seller](https://www.ebay.co.uk/str/avyork), though Andy's guide also contains a wiring diagram if you fancy wiring your own.

Files are sent as blocks over serial, each block on the disk being 256 bytes. So unless a file's length is an exact multiple of 256, there is a bit of junk at the end to pad it out. The files themselves use the character 0x1A as EOF, so can easily be trimmed.

## Detokenising the files

If you try to open some of the raw source files in a text editor, you will notice that the opcodes are missing.

This is because the 6502 assembler is tokenised. Thankfully on one of the disks there was a utility called DETOKEN.COM written in Z80. This is an Einstein utility that is designed to detokenise the 6502 source code. I was able to reverse engineer this and wrote a short Python script to successfully detokenise the 6502 source code into human-readable ASCII text.

The Z80 assembler does not tokenise its source code - it's plain ASCII text.

## Assembling and running

I've started going through the files and making them assemble with modern tools. At the moment this is limited to the Z80 code targetting the AY-3-8912 as used in the Spectrum and Amstrad. The files can be found within the folder Examples.

The assembler I'm using is [sjasmplus](https://github.com/sjasmplus/sjasmplus), and in the .vscode folder there are launch and tasks files for building and running from VSCode.

To build, open any file that is prefixed with 'exec_' and in VSCode, select Terminal -> Run Build Task. This will make a '.sna' file. You can use this file in an emulator; I use ZEsarUX and simply drag the '.sna' file into the ZEsarUX emulator window to run.

For the AY tracker, pressing keys 0-9 will start the appropriate tune, and the letter keys to start sound effects. Pressing Space will exit the tracker.

The code is provided as-is, with no warranty or guarantees.

## Etiquette

All pull requests and issues will be ignored.

## Credits

Thank you to Tim and Geoff Follin for permission to release their music source code, Ste Ruddy for permission to release the Z80 and SID music driver code, Andy Toone for his excellent guide on transferring data over serial, and Kevin Edwards for the editor/assembler instructions and advice on 3" floppy formats.