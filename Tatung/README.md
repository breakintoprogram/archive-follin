# ARCHIVE-FOLLIN

## Introduction

I was donated a box of 3" floppy disks by Tim Follin a couple of years ago that contained backups of the music he wrote in the late 80s and early 90s whilst working at Software Creations in Manchester (UK).

The music was hand-coded by Tim and Geoff Follin in assembler as a series of DEFB's, with that data containing note pitch and duration, and control data.

This data was then played by a small driver, also written in assembly language, in the games.

The assembler/editor was a custom application written by Mike Webb / Ste Ruddy and ran on a Tatung Einstein TC-01. The resultant source code was saved out on said 3" floppy disks.

## The challenge

I used to work with Tim at Software Creations, so was reasonably familiar with the workflow.

I was hoping that:

1. The disks were still readable.
2. I could find a 3" disk drive and/or working Tatung Einstein to read the disks.
3. The disks contained a copy of the editor/assembler.
4. The source code was either saved as plain text, or easy to detokenise.

I ended up purchasing a Tatung Einstein TC-01 for a reasonable price off eBay. They don't come up very often and I got lucky both in terms of the condition unit (which is excellent) and the price paid.

## Reading the disks

For the most part the disks are fine.

One is physically damaged - it has a damaged shutter, which I need to repair, and there were the odd files that didn't read correctly.

There are a couple of disks that have unreadable sides - missing sector 0. I suspect that these are not formatted for the Einstein, maybe the Spectrum +3 or Amstrad CPC6128.

I've also noted that there are a handful of zero-byte files, which puzzled me at first. The working hypothesis is that as part of the workflow, disks were copied to a silicon RAM disk plugged into the Einstein at the start of the day, and edited/assembled from there as it was far quicker than working from floppy. The silicon disks were volatile, so at the end of the day, or at critical points during development, it was backed up to floppy. I suspect that this would sometimes result in a disk full error, with zero-byte files being written out for any files that didn't fit.

I've confirmed with Kevin Edwards, who is using GreaseWeazle / Kryoflux to copy another batch of 3" floppies authored on the Einstein and he's noticed the same.

## Transferring the data

Andy Toone had written [an excellent guide](https://feertech.com/legion/retro/computer/2021/06/08/connecting-over-serial.html) on transferring data from a Tatung Einstein to a PC, which proved invaluable.

I was able to procure a serial label from eBay for a reasonable price from [this seller](https://www.ebay.co.uk/str/avyork), though Andy's guide also contains a wiring diagram if you fancy wiring your own.

Files are sent as blocks over serial, each block on the disk being 256 bytes. So unless a file's length is an exact multiple of 256, there is a bit of junk at the end to pad it out. The files themselves use the character 0x1A as EOF, so can easily be trimmed.

## Detokenising the files

If you try to open some of the raw source files in a text editor, you will notice that the opcodes are missing.

This is because the 6502 assembler is tokenised. Thankfully on one of the disks there was a utility called DETOKEN.COM written in Z80. This is an Einstein utility that is designed to detokenise the 6502 source code. I was able to reverse engineer this and wrote a short Python script to successfully detokenise the 6502 source code into human-readable ASCII text.

The Z80 assembler does not tokenise its source code - it's plain ASCII text.

## Assembling and running

No attempts have been made (yet) to compile and run this code, though it is fairly standard Z80/6502 and should assemble, with perhaps some mollycoddling, using modern Z80/6502 assemblers, and run emulated or on actual hardware.

The code is provided as-is, with no warranty or guarantees.

## Etiquette

All pull requests and issues will be ignored.

## Credits

Thank you to Tim and Geoff Follin for permission to release their music source code, Ste Ruddy for permission to release the Z80 and SID music driver code, and Andy Toone for his excellent guide on transferring data over serial.