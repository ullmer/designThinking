# Tcl wrappers for 3wish *NObj classes
# Brygg Ullmer, MIT Media Lab VLW
# Begun 01/28/96

############################ IvObj ###########################
# addObj works as in the following example
# IvObj strObj
# strObj addObjs {{Font -size 2.5} {Text2 -string "This is a test"}
# strObj assertIv

global __LIBIV__
if {[info exists __LIBIV__]} {return}
set __LIBIV__ 1

#source "~ullmer/pb/code/desk.1/base.tcl"
source "base.tcl"

itcl_class IvObj {
  inherit base

  constructor {config} {
    set members [concat $members $local_members]
  }

  proc translateObj {IvExpr} { ;#spits out Inventor text

   #setup 
    set node [lindex $IvExpr 0]
    set flags [lrange $IvExpr 1 end]
    set result [format {%s %s} $node "\{\n"]

   #parse flags
    set flag 1
    foreach el $flags {
      if {$flag} {
	if {![regexp {^-} $el]} { ;#error
	  puts "IvObj parse error on \"$flag\" in \"$IvExpr\"!"
	  return
	}
	regsub {^-} $el {} el
	append result "   " $el
	set flag 0
      } else {
	append result " " $el "\n"
	set flag 1
      }
    }

    append result "\}\n"

    return $result
  }

  proc translateObjs {IvExprList} {
    set result {}
    foreach obj $IvExprList {
      append result [translateObj $obj]
    }
    return $result
  }

  method addObj {IvExpr} {

    set result [translateObj $IvExpr]
    append ivtext $result
    lappend objlist [list Obj $IvExpr]
  }

  method laddNObj {name IvExpr} { ;# a bit of a hack; might be tweaked
    append ivtext "DEF " $name
    addObj $IvExpr
  }

  method addObjs {IvExprList} {
    foreach obj $IvExprList {
      addObj $obj
    }
  }

  method addIvObj {IvObj} { ;# prepend our own name to assertion
    append ivtext "\nDEF " $this ":" $IvObj " Separator \{\n" 
    append ivtext [$IvObj getIv] "\n\}\n"
    lappend objlist [list IvObj $IvObj]
  }

  method getIv {} {return $ivtext}
  method getObjList {} {return $objlist}

  method addIv {IvStr} {
    append ivtext "\n" $IvStr "\n"
    lappend objlist [list Iv $IvStr]
  }

  method assertIv {} {addNObj $this $ivtext}
  method retractIv {} {delNObj $this}

  public local_members {objlist ivtext}

  public objlist  {}
  public ivtext   {}
}

IvObj simpleplane 
simpleplane addObjs {{Coordinate3 -point 
			  {[-.5 .5 0, .5 .5 0, .5 -.5 0, -.5 -.5 0]}}
		     {NormalBinding -value PER_FACE}
		     {Normal -vector {[0 0 1]}}
		     {FaceSet -numVertices {[4]}}}

