pool_name = "tcp://localhost/grObjPool" #graphical object pool
hose = plasma.Pool.Participate(pool_name)
if hose is None:
  print(f"Failed to connect to pool: {pool_name}")
  return 1
 
try:
  pscope = plasma.create.string("sharedCanvas")
  objName   = "sq1"
  objAction = "move"
  objCoords = [10, 10]
 
  x, y = objCoords
  psObjName, psObjAction    = plasma.create.string(objName), plasma.create.string(objAction)
  psObjLoc                  = plasma.create.v2int32(x,y)
  psObjUpdates              = plasma.create.list([psObjName, psObjAction, psObjLoc])
 
  protein = plasma.Protein(pscope, psObjUpdates)
 
  print(f"depositing in {pool_name}")
  print(protein.ToSlaw().ToString())
 
  ret = hose.Deposit(protein)
  if ret.IsError():
    print(f"no luck on the deposit: {ret}")
    return 1
finally:
  hose.Withdraw()
 
 if __name__ == "__main__":
main()
 
 ### end ###
