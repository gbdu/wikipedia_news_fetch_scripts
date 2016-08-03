#!/bin/bash
conky -c ~/.conky/fetchy/.conkyrc_clock &
conky -c ~/.conky/fetchy/.conkyrc_wiki &
conky -c ~/.conky/fetchy/.conkyrc_wiki2 &
conky -c ~/.conky/fetchy/.conkyrc_sys &
conky -c ~/.conky/fetchy/.conkyrc_net &
#conky -c ~/.conky/fetchy/.conkyrc_netusage &
conky -c ~/.conky/fetchy/.conkyrc_disk &
conky -c ~/.conky/fetchy/.conkyrc_mpd
 
