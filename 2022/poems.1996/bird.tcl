set x_max 76.2
set y_max 61

set x_offset [expr $x_max/2 + 7]
set y_offset [expr $y_max + 5]
set z_offset -10 

#signs
set xs -1
set ys -1
set zs +1

#set h_offset 90
#set p_offset 0
#set r_offset 0

#after 4:15 3/10 
set h_offset 116
set p_offset 15
set r_offset 17


####################### Map Adjusted Position ######################

proc mapAPos {pos} {

  global x_offset y_offset z_offset
  global xs ys zs

  set x [lindex $pos 0]
  set y [lindex $pos 1]
  set z [lindex $pos 2]

  set xa [expr $x_offset + $xs * $x/10]
  set ya [expr $y_offset + $ys * $y/10] 
  set za [expr $z_offset + $zs * $z/10]

  return [list $xa $ya $za] 
}

####################### Map Adjusted Orientation ######################

proc mapAOrient {orient} {

  global h_offset p_offset r_offset

  set h [lindex $orient 0]
  set p [lindex $orient 1]
  set r [lindex $orient 2]

  set ha [expr $p_offset + $p]
  set pa [expr $r_offset - $r]
  set ra [expr $h_offset + $h] ;#right

## adjust back to 0..360 degrees
  foreach el {ha pa ra} {

    if {[expr $$el > 360]} {set $el [expr $$el-360]}
    if {[expr $$el < 0]} {set $el [expr $$el+360]}
  }

  return [list $ha $pa $ra] 
}

####################### Idle Loop ######################

#Start flock
initFlock  "/dev/ttyd2"


set origv [getFlockVecOrient 1]

tiIdle {

  set pos [getFlockPos 1]
  set orient [getFlockOrient 1]
  set vorient [getFlockVecOrient 1]

  set diff [dist3D $origv $vorient]

  puts "dist $diff"
  puts "vorient $vorient"

 #adjust from mm to cm units

  set x [lindex $pos 0]
  set y [lindex $pos 1]
  set z [lindex $pos 2]

  set adjpos    [list [expr $x/10] [expr $y/10] [expr $z/10]] 

  set apos    [mapAPos $pos]
  set aorient [mapAOrient $orient]

 #puts "cam $adjpos $orient // $apos $aorient"

####move camera

  moveTo $apos
  rotTo  $aorient
}

#END

