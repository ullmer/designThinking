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

    moveNObj $objname:trans [list $x 0 $y]
  }

  public local_members {orient}
  public orient {0 0 1}
}

