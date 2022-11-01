# Simple plane object

# Brygg Ullmer, ullmer@media.mit.edu
# Begun 04/29/96

global __PLANE__
if {[info exists __PLANE__]} {return}
set __PLANE__ 1

source base.tcl
source libiv.tcl

itcl_class wireframe_plane {
  inherit IvObj

  constructor {config} {
    set members [concat $members $local_members]
  }

  method assertIv {} {

    set xincr [expr ($maxx - $minx) / ($xdivs - 1)]
    set yincr [expr ($maxy - $miny) / ($ydivs - 1)]

    addNFrame $this

    addNInlineObj   $this:color [IvObj :: translateObj [format \
      {Material -diffuseColor {%s}} $color]]

    addNInlineObj $this:xlines [IvObj :: translateObj [format \
      {Array -numElements1 %s -separation1 {%s 0 0} -origin FIRST} \
      $xdivs $xincr]]

    addNInlineObj $this:ylines [IvObj :: translateObj [format \
      {Array -numElements1 %s -separation1 {0 0 %s} -origin FIRST} \
      $ydivs $yincr]]


    addNObj $this:xlines:xline [IvObj :: translateObjs [format {
      {Coordinate3 -point {[%s 0 %s, %s 0 %s]}}
      {LineSet -numVertices {2} -startIndex {0}}} \
       $minx $miny $minx $maxy]]

    addNObj $this:ylines:yline [IvObj :: translateObjs [format {
      {Coordinate3 -point {[%s 0 %s, %s 0 %s]}}
      {LineSet -numVertices {2} -startIndex {0}}} \
       $minx $miny $maxx $miny $ydivs $yincr]]
  }

  public local_members {xdivs ydivs minx maxx miny maxy color}

  public color {.1 .1 .6}
  
  public xdivs {10}
  public ydivs {10}

  public  minx {-10}
  public  maxx { 10}

  public  miny {-10}
  public  maxy { 10}
}

#wireframe_plane zePlane
#zePlane assertIv

#puts [getNObj root]

