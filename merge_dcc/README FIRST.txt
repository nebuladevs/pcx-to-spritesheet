MERGE_DCC freeware 1.5, by Paul SIRAMY, 5 November 2002
DCC Decoder made with the precious help of Bilian BELCHEV
=========================================================


What is it ?
------------
This tool makes an animation from a multi-part monster. Give
it a try : launch Merge_dcc.exe, and you'll have several pcx
of a Fallen attacking. It's ready to use in a gif animator.
It's usefull if you want to transform a multi-part monster
(or player) into a torso-only animation for instance, or if
you're interested by the animations of the game for using
them in a Mod of another game.



How does it works ?
-------------------

>>> Download the Allegro library <<<

from either

   http://paul.siramy.free.fr/_divers/ds1/alleg40.zip

or from

   http://dynamic2.gamespy.com/~phrozenkeep/site/filecenter/filecenter-1-tools-8-0008.php

and put the Alleg40.dll in the directory of this program or in the
'system' directory of your Windows.


It takes parameters from the Merge_dcc.ini, you can't use
another file than this one, so make copy/paste from another
file into this one. You must extract cof/dcc/palshift.dat
from a mpq into this directory, and you MUST keep the
original directory structure, starting from the token of
the monster. Just follow the FA model there's in this zip.
It then use this ini to choose 1 cof, and the dcc it needs
for this animation. Folowing the layer priority table
there's in the cof, it makes all the frames of each
directions, then it save them. An interesting option is
that you can use the colormaps that are in the palshift.dat
and you can even set a different colormap number to each
dcc. So you can make a Brown Fallen with a Pink Club
(as in the exemple).



How do I use it ?
-----------------
Extract all the monster data into this directory, and don't
forget to keeps its original directory structure. Then edit
the Merge_dcc.ini.

The 1st line is the format of the final images. It can be
either PCX or BMP.

The 2nd line is the name of the COF to use, it's one of the
<monster token>\cof\*.cof files. The other lines are for
each parts of this animation you want to draw (you can choose
to not use all the necessay animations, so you can make a
Fallen with no shield but a weapon, or a shield and a club but
without the fallen itself etc).

If you don't know what are the layers that are in the COF, just
launch the Merge_dcc.exe now. It'll create 2 files : stderr.txt
and stdout.txt. stderr.txt is the file to check for error
description if something didn't work as you wanted. stdout.txt is
a sort of a report, it tells you some interesting informations
that are in the cof, as the layers list you were searching. If
you want to make a complete animation, just make a line in the
Merge_dcc.ini for each layer, like :

   tr=lit:4

It means that for this cof, you ask to use a TR layer, and for
this Torso it'll be the LIT armor (fa\TR\faTRLITa1hth.dcc).
The ':4' is the way to use a colormap. The number is between 0
and 7, inclusive. The 0 and 1 have usually no effect, and most
of the time the number 2 neither. Just try it.

Note : the " tr=lit:4 " format ask the program to check the
palshift.dat of the monster, but such files are not
interesting for characters (like amazon, sorceress...). So you
can also use another format :

   tr=med:grey.dat:12

where after the 1st ':' you put the path to the file, then
another ':' and you put the colormap number. You may want to
check http://dynamic2.gamespy.com/~phrozenkeep/site/colormaps.php
for a comprehensive doc on how colormaps are working in Diablo II.
In this exemple, the Grey parts of the Torso will be Crystal Green.



You can add an optional line in the merge_dcc.ini. This is the line

   box=-100,-150,100,20

This line, if present, must be placed after the 'cof=' line. What
is it ? It gives you controls on the final image. Decode an
animation and open stdout.txt. You'll see at the end something like

   box = (-53, -79) - (54, 11) = 108 * 91 pixels

Imagine that each parts of a monster is a box in a virtual space.
The area in that space that the box is using is defined by 2
coordinates, the upper/left corner and the bottom/right corner.
In this exemple, the 4 numbers are xmin = -53, ymin = -79, xmax = 54,
ymax = 11. So the width of the box is 1 + xmax - xmin =
1 + 54 - (-53) = 108. Same logic for the height. This has something
to do with the offsets you might have heard about.

By default, the programm makes the animation in the smaller box
it found that can contain all of the box of each parts. That means
that there won't be any borders in the final animation. But by
adding this 'box=...' line in the merge_dcc.ini you force the programm
to use * your * box. Just try to make 2 animations with the same
'box=...' line, and you'll see that your animations will have the exact
same size, and that you can superpose the animations between them.

This is an 'advanced' option, that you probably won't need, but it can
be usefull for advanced users, if they need it one day. So it's there.



I have a layer which is sometimes a mess !
------------------------------------------
It's surely a bug in my decoder of the dcc. you better have to
NOT use this layer, so either delete the corresponding line in the
Merge_dcc.ini, or use another dcc (MED instead of HVY for
instance). Instead of deleting the line in the ini, you can also
just comment it :

   ;s2=hvy   it's buggy :(

the ';' character in the 1st column tells the prog this line is a
comment, so it won't use it.

Also, it would be nice to tells me the dcc you were using, this way
I'll be able to analyse my decoder. My email is siramy_paul@yahoo.com




What is the name of a pcx ?
---------------------------
They're name after this model :

   D <direction in COF> - <direction in DCC> - F <frame> . PCX

Let's take the Fallen. In the DCC here are the direction numbers
and their orientation :

1    6   2
  \  |  /
   \ | /
    \|/
5 ---*--- 7
    /|\
   / | \
  /  |  \
0    4   3

That's a strange pattern. But in the COF, the layer priority table
is NOT in the same order. It start at the bottom, then bottom-left,
then left, then upper-left and so on, like a watch. In a DCC we have
the directions in the order 0 1 2 3 4 5 6 7, but in the COF we have
them in the 4 0 5 1 6 2 7 3 order. And since I decode the frames
folowing the COF order (more natural), I name them in the 'natural'
order, from 0 to 7, while still indicate in the name the original
order in the dcc. 

Of course, it's too easy. That's why it only works for monsters
in 8 directions. For animations in 16 directions (player characters)
or 32 directions (missiles) that's another patterns :P but you
might figure them with the name of the pcx.

You can view the 'dcc_dir.gif' that's in this zip. You'll understand
better how the directions are ordered in a DCC.




Are there known problems ?
--------------------------

* It's not easy to handle the transparency of some layer. Take the
Fallen, give it a Torch (sh=tch) instead of a shield, and you'll see
what I mean : this layer is alpha-blended, that means the darkest a
pixels of this layer is, the more transparent it'll be draw in
the game, the lightest it is, the more opaque it'll be. I don't
handle transparency at all, I just draw them as they are.
