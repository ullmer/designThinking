# First explorations of book proxy-code
# In conjunction with Ishii/Ullmer Active Desk prototype
# Brygg Ullmer, ullmer@media.mit.edu
# Begun 01/11/95

if {[info exists __TEXTURE__]} {return}
set __TEXTURE__ 1

#The following should be net_source or equiv
source base.tcl

############################ Texture class #############################

itcl_class texture { #operates on RGB textures
  inherit base

  constructor {config} {
    set members [concat $members $local_members]
  }
  
  method getTextureSize {} {
    #find "size" file
    regsub {\.rgb$} $texture_name {.size} texture_size

    if {![file exists $texture_size]} {
      set texture_size {0 0}
      return $texture_size
    }

    set f [open $texture_size r]
    set size [gets $f]; close $f

    regsub {^.*[^0-9]([0-9]+) by ([0-9]+).*} $size {\1} x
    regsub {^.*[^0-9]([0-9]+) by ([0-9]+).*} $size {\2} y

    set texture_size [list $x $y]

    return $texture_size
  }

  public local_members {texture_name texture_size}

  public texture_name {}
  public texture_size {0 0}
}

