# Virtual Physics library and derivative program Makefile
# Brygg Ullmer, filtered from previous Makefile 06/19/93

HOME = /home/interval/ullmer
VPDIR = $(HOME)/code/vp

CCINCDIR= /usr/include/CC
#CFLAGS= -g -cckr -DSYSV -DIRIS_GL -I$(GFXINCDIR) -I$(TRAKINCDIR)
CFLAGS= -g -I$(TRAKINCDIR)

ILIBS = -lbsd -lgl_s -lc_s -lm

INVFLAGS= -cckr -Wab,-nofpdivfix -DFUNCPROTO -D__C_PLUS_PLUS_2 +p -Wf,-XNp10000
GINVFLAGS= -DFUNCPROTO -D__C_PLUS_PLUS_2 

INVLIBS= -lInventorXt -lInventor -lfm_s -limage -lgl_s  -lsun -lm \
	-lXirisw -lXm_s -lXt_s -lX11_s -lPW    -L -L/usr/lib   -lc_s
SINVLIBS= -lInventor
#SINVLIBS == Simple Inventor Libs; hopefully will speed up compilation

VIZFLAGS= $(CFLAGS) $(CGFLAGS)  -I$(CCINCDIR) -I/usr/include -lInventor \
	  $(INVFLAGS) 
GVIZFLAGS= $(CFLAGS) $(CGFLAGS)  -I$(CCINCDIR) -I/usr/include -lInventor \
	  $(GINVFLAGS) 
VIZLIBS= $(GLIBS) $(LIBS) $(INVLIBS) -lm  $(TRAKLIB)
IVIZLIBS= $(ILIBS) $(INVLIBS) -lm  

###Interval work

VPFLAGS = -v2 $(ICFLAGS) -I$(CCINCDIR) -I/usr/include -lInventor $(INVFLAGS) 

VPLIBS = $(IVIZLIBS) 

VPXLIBS = $(VPLIBS) -lXm -lXt

###

MYVIZLIBS = $(VIZLIBS) $(MYDIR)/container.o $(MYDIR)/VRhw.o

## Interval work

C++FLAGS = +p -DFUNCPROTO -v2 -DDEBUG

MOTIFLIBS = -lXirisw -lXm_s -lXt_s -lX11_s -lPW

INVENTOR_XT = -lInventorXt $(MOTIFLIBS) -lInventorDebug_s
INVENTORLIB = $(INVENTOR_XT)

IVPFLAGS= $(VPFLAGS) -DINVENTOR -DDEBUG -I$(VPDIR)
VPILIBS = $(INVENTORLIB) -limage -lfm_s -lgl_s -lsun -lm -lmalloc -lc_s

list.o: list.h list.C
	CC -g -c list.C

######

VPOBJECTS = vp.o vis.o forces.o objects.o sound.o dtm.o geom.o image.o \
  visenv.o visobj.o menu.o 


$(VPOBJECTS): #$*.C $*.h
	CC $(IVPFLAGS) -g -c $*.C


CLEANOBJECTS = doc.o orgrel.o

$(CLEANOBJECTS):
	CC -g -c $*.C

#######

TSTBINARIES = tst01 tst02 tst03 tst04 tst05 tst06 tst07 tst08 tstgeom tstctr \
  tstorg tst09 tst10 tst11 tst12 tst13 tst14 tst15 tst17 tst19 \
   tst20 tst21 tst22 tst23 tst24 tst25 tst26 tst28 tst29  tst31 tst32 tst33 \
   tst34 tst35 tst36

$(TSTBINARIES): #vis.o vp.o forces.o 
	CC $(IVPFLAGS) vis.o vp.o list.o forces.o objects.o doc.o sound.o geom.o image.o visobj.o visenv.o fader.o $@.C -o $@ $(VPLIBS)


TSTBINARIES2 = tst18 tst16 tst27 tst30 tstorg2

$(TSTBINARIES2): #vis.o vp.o forces.o 
	CC $(IVPFLAGS) vis.o vp.o list.o forces.o objects.o doc.o sound.o geom.o image.o visobj.o visenv.o menu.o $@.C -o $@ $(VPXLIBS)


#######

depend = vis.o vp.o list.o forces.o objects.o doc.o

tstdtm: tstdtm.C $(depend)
	CC $(IVPFLAGS) vis.o vp.o list.o forces.o objects.o dtm.o libdtm.a \
	sound.o doc.o \
	tstdtm.C -o tstdtm $(VPLIBS)

tstsnd: tstsnd.C
	CC $(IVPFLAGS) vis.o vp.o list.o forces.o objects.o sound.o doc.o geom.o visenv.o visobj.o image.o\
	tstsnd.C -o tstsnd $(VPLIBS)


sfh = tstsfh tstsfh2 tstsfh3 tstsfh4 tstsfh5 tstsfh6 tstsfh7 tstsfh8

$(sfh): 
	CC $(IVPFLAGS) vis.o vp.o list.o forces.o objects.o sound.o doc.o \
	news.o anews.o geom.o visenv.o visobj.o image.o menu.o\
	$@.C -o $@ $(VPXLIBS)

tstor: 
	CC tstor.C ../db.o ../list.o orgrel.o -o tstor

tstcd:
	CC tstcd.C -lcdaudio -lds -o tstcd
