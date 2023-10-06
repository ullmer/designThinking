# Simple behavior object

# Brygg Ullmer, ullmer@media.mit.edu
# Begun 04/29/96

global __BEHAV__
if {[info exists __BEHAV__]} {return}
set __BEHAV__ 1

source base.tcl
source libiv.tcl

itcl_class actor {

  inherit base

  constructor {config} {
     set members [concat $members $local_members]
  }

  method genIv {} {

    IvObj $objname
    $objname addObjs {
      {Translation -translation {0 2 0}}
      {Material -diffuseColor {1 0 0}}
      {Cube -height 4 -width 3 -depth 2}
      {Translation -translation {0 3 0}}
      {Material -diffuseColor {.8 .2 .2}}
      {Cube -height 2 -width 1.5 -depth 1.5}
    }

    $objname assertIv
  }

  method hop {} {

    shiftNObj $objname.hop {0 0 0} {0 3 0} .5 10
    tiAfter 0.51 [format {shiftNObj %s.hop {0 0 0} {0 -3 0} .5 10} $objname]

    tiAfter 1.1 [format {%s again hop} $this]
  }

  method shuffle {} {
    shiftNObj $objname.shuffle {0 0 0} {0 0 .4} .5 10
    tiAfter 0.51 [format {shiftNObj %s.shuffle {0 0 0} {0 0 2} .5 10} $objname]

    tiAfter 1.1 [format {%s again shuffle} $this]
  }

  method again {behavior} {
    if {[set $behavior]} {$behavior}
  }

  method genBehpal {} {

    button .shuffle -text Shuffle -command [format {
       %s shuffle; %s toggle shuffle} $this $this]
    button .hop     -text Hop     -command [format {
       %s hop; %s toggle hop} $this $this]

    pack .shuffle .hop -side top
  }

  method toggle {behavior} {
    if {[set $behavior] == 0} {
      set $behavior 1
      .$behavior configure -background gold2
    } else {
      set $behavior 0
      .$behavior configure -background gray
    }
  }

  public local_members {objname}
  public objname {ivActor}

  public shuffle {0}
  public hop     {0}
}

actor zeActor
zeActor genIv
zeActor genBehpal

