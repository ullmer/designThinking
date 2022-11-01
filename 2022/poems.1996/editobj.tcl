## General object editing code
## Brygg Ullmer
## Begun 12/05/95

############################ Generic object config #########################

proc gen_obj_config {obj} {

  set top [format {.%s-config} $obj]

  toplevel $top 
  wm title $top  [format {Obj Configuration for "%s"} $obj]

## Find available variables
  set Ovars [$obj info public]
  set vars {}
  foreach var $Ovars {

    regsub {^.*::} $var {} var
    lappend vars $var
  }

  set butlist {}
  foreach var $vars {
    if {[lsearch $butlist $var] == -1} {
      lappend butlist $var
    }
  }

## Build the screen rep
  foreach var $butlist {

    frame $top.$var
    label $top.$var.label -text $var
    entry $top.$var.entry -width 20

    $top.$var.entry insert 0 [$obj get $var]
    
    pack $top.$var.label $top.$var.entry -side left
    pack $top.$var -side top -anchor ne
  }

## Save/Close

  frame $top.base
  pack $top.base -side bottom

  button $top.base.save -text "Save"  -command \
    [format {
      global canvas

      foreach var {%s} {
	%s config -$var [%s.$var.entry get]
      }

      # set id [UrbObj :: getIdFromObj %s]
      # $canvas delete $id
      # %s genCanvasRep $canvas
      
    } $vars $obj $top $obj $obj]

  button $top.base.close -text "Close" -command "destroy $top"
  pack $top.base.save $top.base.close -side left

}

