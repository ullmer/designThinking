source libiv.tcl

IvObj Button
Button addObjs {
  {Translation -translation {0 10 0}}
  {Cube}
  {Text3 -string {"Hello, World"}}}
Button assertIv


addNObj button {Cube {}}
bindNObj button {
  puts "Hello"; shiftNObj button.trans {0 0 0} {0 3 0} 1 15
}

puts [getNObj root]

