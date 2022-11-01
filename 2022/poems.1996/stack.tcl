#!3wish
# Stack of Image objects
# Brygg Ullmer, MIT Media Lab VLW/TMG
# March 4, 1996

#Change to net-sources off of true names (through proxy-structures)

global __STACK__
if {[info exists __STACK_]} {return}
set __STACK__ 1


#set host "~ullmer/pb/code/desk.1"
set host "."

source "$host/base.tcl"
source "$host/libiv.tcl"
#source "$host/text.tcl"

########################## Texture Plane ###########################

itcl_class texture_plane {

  inherit IvObj

  constructor {config} {
    set members [concat $members $local_members]
  }

  method assertIv {{orient xz}} {
    if {$texture_name == {}} {return} ;#default args don't work

    set hx [expr [lindex $texture_size 0] / 2.] ;#half x dim
    set hy [expr [lindex $texture_size 1] / 2.] ;#half y dim

    switch $orient {

      xz { set coords [format {
	     Coordinate3 -point {[-%s 0  %s,  %s 0  %s, 
				   %s 0 -%s, -%s 0 -%s, -%s 0 %s]}
	     } $hx $hy $hx $hy $hx $hy $hx $hy $hx $hy]
	   set normal {0 1 0}
	 }

      xy { set coords [format {
	     Coordinate3 -point {[-%s  %s 0,  %s  %s 0, 
				   %s -%s 0, -%s -%s 0, -%s %s 0]}
	     } $hx $hy $hx $hy $hx $hy $hx $hy $hx $hy]
	   set normal {0 0 1}
	 }
    }
    # spit out a textured plane of the right size in the x-z plane
    addObjs [format {
	     {TextureCoordinate2 -point {[1 1, 0 1, 0 0, 1 0]}}
	     {Texture2 -filename %s -model DECAL}
	     {NormalBinding -value PER_FACE}
	     {Normal -vector {%s}}
	     {%s}
	     {FaceSet -numVertices 4}} \
	     $texture_name $normal $coords]
    IvObj::assertIv

    addNInlineObj $this:transp [format {Material {transparency %s
	 diffuseColor %s}} $transp $color] pre

  }

  method changeTransp {newval} {

    set transp $newval
    delNObj $this:transp
    addNInlineObj $this:transp [format {Material {transparency %s
	 diffuseColor %s}} $transp $color] pre
  }

  public local_members {texture_name texture_size transp color}

  public color {1 1 1}
  public texture_name {}
  public texture_size {0 0}
  public transp {0.7}
}

########################## Texture Stack ###########################

itcl_class texture_stack {

  inherit IvObj

  constructor {config} {
    set members [concat $members $local_members]
  }

  method assertIv {{orient xz}} {
    if {$texture_names == {}} {return} ;#default args don't work
    set imnum 1

    puts "asserting $this"
    addNFrame $this

    foreach texture_name $texture_names {

      set name [format {%s:texture%s} $this $imnum]
      set name_trans [format {%s:trans%s} $this $imnum]

      texture_plane $name -texture_name $texture_name \
	-texture_size $texture_size -color $color

      $name assertIv $orient
      addNInlineObj $name_trans \
	[format {Translation {translation %s}} $img_offset]

      bindNObj $name [format {%s highlight %s} $this $imnum]
      $name changeTransp [lindex $highlights 0]

      incr imnum
    }

    highlight $popout
  }

  method highlight {layer} {
    if {$layer > [llength $texture_names] || $layer < 1}  {return} 
      ;#illegal layer number

    if {$last_highlighted != {}} {
      $last_highlighted changeTransp [lindex $highlights 0]
    }

    set last_highlighted $this:texture$layer
    $last_highlighted changeTransp [lindex $highlights 1]
  }

  public local_members {texture_names texture_size img_offset 
      last_highlighted highlights color popout}

  public texture_names {}
  public texture_size {0 0}
  public img_offset {0 2 0}
  public color {1 1 1}

  public last_highlighted {}
  public highlights {.7 .2}
  public popout {1}
}

