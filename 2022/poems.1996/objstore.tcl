# Objstore for collab project
# Brygg Ullmer, ullmer@media.mit.edu
# Begun 04/24/96

global __OBJSTORE__
if {[info exists __OBJSTORE__]} {return}
set __OBJSTORE__ 1

source base.tcl
source libiv.tcl
source texture.tcl
source stack.tcl

####################### ObjStore ######################

itcl_class ObjStore {
  inherit base

  constructor {config} {
    set members [concat $members $local_members]

    foreach el $objlist {
      set tag [lindex $el 1]
      set profiles($tag) $el
    }
  }

  method getProfile {tag} {
    return $profiles($tag)
  }

  method getClass {tag} {
    return [lindex $profiles($tag) 0]
  }

  method getClassInst {class} {
    if {![info exists classes($class)]} {
      set classes($class) ze$class
      $class ze$class ;#invoke instance
    }

    return $classes($class)
  }

  method getImagefile {tag} {
    return [lindex $profiles($tag) 2]
  }

  method addProfile {tag profile} {
    set profiles($tag) $profile
    lappend objlist $profile
  }

  public local_members {objlist}
  public profiles 
  public classes 

  public objlist {
    {obPhoto room1 data/room1.h.ppm}
    {obPhoto room2 data/room2.h.ppm}
    {obPhoto room3 data/room3.h.ppm}
    {obPhoto room4 data/room4.h.ppm}
    {obPhoto room5 data/room5.h.ppm}
    {obPhoto room6 data/room6.h.ppm}
    {obPhoto room7 data/room7.h.ppm}
    {obPhoto room8 data/room8.h.ppm}
    {obPhoto roomMe data/room-me.h.ppm}
  }

}

####################### ObjBase ######################

itcl_class ObjBase {

  inherit base

  constructor {config} {
    set members [concat $members $local_members]
  }

  method genIv {} {
  }

  method moveObj {x y} {
  }

  method genPalette {frame {width 100}} {
    set parentframe $frame

    catch "destroy $parentframe"
    frame $parentframe

    set buttonList [extractSublist $pal_options 0] ;#extract button titles

    genButtonList $buttonList $parentframe $width
  }

  method genButtonList {buttonlist frame {width 100}} {
    set i 0
    set bwidth [expr $width / [llength $buttonlist]]

    foreach item $buttonlist {
      button $frame.b$i -text $item -width $bwidth
      pack   $frame.b$i -side left -fill both -expand 1

      incr i
    }
  }

  method extractSublist {list elnum} {
   #extract sublist of n'th subels of list

   set result {}
   foreach el $list {
     lappend result [lindex $el $elnum]
   }

   return $result
  }

  public local_members {parentframe pal_options objname 
       locationX locationY}

  public parentframe {}
  public pal_options {}
  public objname {}
  public imagename {}

  public locationX {}
  public locationY {}
  public locationZ {0}
} 

####################### Ob Placeholder ######################

itcl_class obPlaceholder {

  inherit ObjBase

  constructor {config} {
    set members [concat $members $local_members]

    set pal_options {
      {{Show streets}}
      {{Animate sdfsdf}}
      {{Something else}}
    }
  }

  public local_members {}
}

####################### Ob Actor ######################

itcl_class obActor {

  inherit ObjBase

  constructor {config} {
    set members [concat $members $local_members]

    set pal_options {
      {{Random movement}}
      {{Shuffle}}
      {{Hop}}
      {{Trot}}
    }
  }

  method genIv {} {

    set objname [format {%s_iv} $this]

    IvObj $objname
    $objname addObjs {
      {Scale -scaleFactor {6 6 6}}
      {Translation -translation {0 2 0}}
      {Material -diffuseColor {1 0 0}}
      {Cube -height 4 -width 3 -depth 2}
      {Translation -translation {0 3 0}}
      {Material -diffuseColor {.8 .2 .2}}
      {Cube -height 2 -width 1.5 -depth 1.5}
    }

    $objname assertIv
  }

  method moveObj {x y} {

    moveNObj $objname:trans [list $x 0 $y]
  }

  public local_members {}
}



####################### Ob Photo ######################

itcl_class obPhoto {

  inherit ObjBase

  constructor {config} {
    set members [concat $members $local_members]

    set pal_options {
      {{photo 1}}
      {{photo 2}}
    }
  }

  method genIv {} {

    regsub {ppm} $imagename {rgb} rgbimage
    set texturename [format {%s_texture} $this]

    texture $texturename -texture_name $rgbimage

    set size [$texturename getTextureSize]

    set objname [format {%s_iv} $this]
    texture_plane $objname -texture_name $rgbimage \
      -texture_size $size

    $objname assertIv
  }

  method moveObj {x y} {

    moveNObj $objname:trans [list $x $locationZ $y]
    set locationX $x
    set locationY $y
  }

  public local_members {orient}
  public orient {0 0 1}
}

