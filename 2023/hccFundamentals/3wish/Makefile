# Base Inventor Makefile
# Brygg Ullmer, 9/30/95

CC = CC
cc = cc

#### LIBRARIES ####

INVLIBS = $(LIBS) -lInventorXt -lInventor -lGL -limage \
                  -lXirisw -lXm_s -lXt_s -lX11_s -lm 

FLOCKLIB = /usr/lib/Performer1.2/libpf-g.a \
   -limage /u/dave/libFlock/libFlock.a -lgl 

LEGOLIB  = /u/dave/libControlLab/libControlLab.a  \
   -rpath /usr/lib/Performer1.2 /usr/lib/Performer1.2/libpf.so \
   /usr/lib/Performer1.2/libpr.so /usr/lib/Performer1.2/libpfutil.so 


APPLIBS       = $(FONTULIB) $(FONTLIB) 

LIBS         = -lm -lInventorXt -lm 

TCL_DIR = /vlw/pkg/tcl.installs/tcllib
TCL_INCLUDE = -I$(TCL_DIR)/include
TCL_LIB = -lX11 -L$(TCL_DIR) -ltkx -ltk -ltclx -ltcl7.4 -litcl

LIBTK        = -ltk
LIBTCL       = -ltcl7.4
LIBTCLX      = -ltclx

TCLLIBS = $(TCL_LIB)

#### FLAGS ####

INVFLAGS     = $(FLAGS) -cckr -DINVENTOR -DUSTRACE 

FLOCKFLAGS   = -DOPENGL -I/u/dave/libFlock -I/usr/include/Performer1.2 \
	-Olimit 2000 

#IFLAGS       = -I$(EARL_TOPDIR)/include -I/usr/local/include \
#	-I/vlw/pkg/tcl.installs/tcllib/include      

IFLAGS       = -I/usr/local/include

### Libs

tkXAppInit.o: tkXAppInit.cc
	$(CC) -I /usr/local/include -c tkXAppInit.cxx

### Individual compiles

PROGRAMS = test-fonts inventor_examp tcl_examp

$(PROGRAMS): $(APPLIBS) $$@.cxx
	$(CC) $(INVFLAGS) $(IFLAGS) -o $@ $@.cxx \
	$(INVLIBS) $(APPLIBS) $(TCLLIBS) $(TOOLS)

#####

OBJS = 3wish.o w3shift.o w3core.o w3text.o w3bind.o w3textureobj.o w3rot.o\
	w3term.o w3flock.o w3kit.o w3lego.o

# Use gmake to successfully resolve the following

#$(OBJS): $*.cxx $*.h

$(OBJS): 
	$(CC) $(INVFLAGS) $(IFLAGS) -c $*.cxx
#	$(CC) $(INVFLAGS) $(FLOCKFLAGS) $(IFLAGS) -c $*.cxx

3wish: 3wish.o 
	$(CC) $(INVFLAGS) 3wish.o \
	$(TCLLIBS) $(INVLIBS) $(APPLIBS) -o 3wish
#	$(TCLLIBS) $(INVLIBS) $(APPLIBS) $(FLOCKLIB) $(LEGOLIB) -o 3wish


###
