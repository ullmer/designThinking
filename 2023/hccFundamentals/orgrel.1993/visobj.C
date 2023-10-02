#include "visobj.h"

//////

VpvCoCube::VpvCoCube(SoSelection *selection)
{ cube = new SoCube;
  material = new SoMaterial;
  name = "Unnamed colored cube";
  setSelection(selection);
}

VpvCoCube::VpvCoCube(VpObject *object, SoSelection *selection)
{ cube = new SoCube;
  material = new SoMaterial;
  name = "Unnamed colored cube";
  setSelection(selection);

  bindObj(object);
}

VpvCoCube::VpvCoCube(VpObject *object, float r, float g, float b)
{ cube = new SoCube;
  material = new SoMaterial;
  name = "Unnamed colored cube";

  setColor(r,g,b);
  bindObj(object);
}

void VpvCoCube::setColor(float r, float g, float b)
{ if (material == NULL) return;
  
  material->diffuseColor.setValue(r,g,b);
}

void VpvCoCube::setSelection(SoSelection *nselect)
{selection = nselect;}

void VpvCoCube::bindObj(VpObject *object)
{ obj = object;
  transl->translation.setValue(obj->GetLoc());
  ObjSep->ref();
  ObjSep->addChild(transl);
  ObjSep->addChild(material);
  ObjSep->addChild(cube);

}

void VpvCoCube::dim()
{ material->diffuseColor.setValue(0,0,1);
}

void VpvCoCube::bright()
{ if (selection == NULL) return;

  SoPath *path = new SoPath(cube);
  selection->select(path);
  material->diffuseColor.setValue(1,1,1);
}

////////

void VpvSCube::selected()
{ play(); }

VpvICube::VpvICube(VpObject *object, char *filename)
{ VpiBase::setFilename(filename);
  VpiBase::bindImage();

  VpvCube::getShell()->addChild(VpiTexture::getBoundImage());
  VpvCube::bindObj(object);
}


////

VpvText::VpvText(VpoText *obj, int frontOnly)
{ init(obj, frontOnly); }

void VpvText::init(VpoText *obj, int frontOnly)
{ name = "Unnamed text";

  font = new SoFont;
  font->name.setValue("Times-Roman");
  font->size = 1.3;

//  obj->WrapText(20);

  text = new SoText3;
  if (frontOnly) text->parts.setValue(SoText3::FRONT); //Front only
  text->justification.setValue(SoText3::CENTER);

  bindObj(obj);
}

void VpvText::FixText() //reimplement in fuller form; this is just a test
{ char *str = ((VpoText *)obj)->GetText();
  char *nstr = new char[strlen(str) + 1];
  strcpy(nstr, str);

  int num=1; char *ptr=nstr;

  while (ptr = strchr(ptr,'\n'))
    {*ptr = 0; ptr++; num++;}

  char **strings = new char*[num];
//  char **strings = (char **) malloc(sizeof(char *) * num);

  ptr = nstr;

  for (int i=0; i<num; i++)
    { strings[i] = ptr;
      ptr += strlen(ptr) + 1;
    }

  text->string.setValues(0,num,strings);
}

void VpvText::bindObj(VpoText *nobj)
{ obj = nobj;
  transl->translation.setValue(obj->GetLoc());
  ObjSep->ref();
  ObjSep->addChild(transl);
  ObjSep->addChild(font);

  FixText();

  ObjSep->addChild(text);
}

VpvText2::VpvText2(VpoText *obj, float r, float b, float g)
{ init(obj,r,g,b); }

void VpvText2::init(VpoText *obj, float r, float b, float g)
{ name = "Unnamed text";

  font = new SoFont;
  font->name.setValue("Times-Roman");
  font->size = 14.;

  obj->WrapText(20);

  text = new SoText2;
  text->justification.setValue(SoText2::CENTER);
  text->spacing.setValue(1);

  material = new SoMaterial;
  material->diffuseColor.setValue(r,g,b);

  bindObj(obj);
}

void VpvText2::setColor(float r, float g, float b)
{ if (material != NULL)
    material->diffuseColor.setValue(r,g,b);
}

void VpvText2::setSize(float n)
{ if (font != NULL)
    font->size.setValue(n);
}

void VpvText2::bindObj(VpoText *nobj)
{ obj = nobj;
  transl->translation.setValue(obj->GetLoc());
  ObjSep->ref();
  ObjSep->addChild(transl);
  ObjSep->addChild(font);
  ObjSep->addChild(material);

  FixText();

  ObjSep->addChild(text);
}

void VpvText2::FixText() //reimplement in fuller form; this is just a test
{ char *str = ((VpoText *)obj)->GetText();
  char *nstr = new char[strlen(str)+1];
  strcpy(nstr, str);

  int num=1; char *ptr=nstr;

  while (ptr = strchr(ptr,'\n'))
    {*ptr = 0; ptr++; num++;}

//  char **strings = (char **)malloc(num*sizeof(char *));
  char **strings = new char*[num];

  ptr = nstr;

  for (int i=0; i<num; i++)
    { strings[i] = ptr;
      ptr += strlen(ptr) + 1;
    }

  text->string.setValues(0,num,strings);
}


//// VpvCoText ////

VpvCoText::VpvCoText(VpoText *obj)
{ material = new SoMaterial;

  init(obj);
}

VpvCoText::VpvCoText(VpoText *obj, float r, float g, float b)
{ material = new SoMaterial;

  init(obj);
  setColor(r,g,b);
}

void VpvCoText::bindObj(VpoText *nobj)
{
  obj = nobj;
  transl->translation.setValue(obj->GetLoc());
  ObjSep->ref();
  ObjSep->addChild(transl);
  ObjSep->addChild(material);
  ObjSep->addChild(font);

  FixText();

  printf("Text to bind: \"%s\"\n", nobj->GetText());
  ObjSep->addChild(text);
}

void VpvCoText::setColor(float r, float g, float b)
{ if (material != NULL)
    material->diffuseColor.setValue(r,g,b);
}


//// PosBlender ////

PosBlender::PosBlender(int windowSize)
{ WindowSize = windowSize;
  vecList = new VpVecList;
}

void PosBlender::setSize(int windowSize)
{ if (vecList->length() > windowSize)
    while (vecList->length() > windowSize) delete vecList->get();

  WindowSize = windowSize;
}

void PosBlender::setVec(VpVec p)
{ VpVec *newV = new VpVec;
  *newV = p;

  vecList->append(newV);
  if (vecList->length() > WindowSize) delete vecList->get();

}

VpVec PosBlender::getVec()
{ VpVec total, *ptr;
  int num=0;

//*******
//*******
  total.setValue(0,0,0); //The necessity for this line (imperically verified)
   //may suggest that my usage of implicit "Zero" vecs is dangerous!!!

  if (vecList->length() == 0) return total;

  vecList->resetMarker();
  ptr = vecList->first(); vecList->next();

  while (ptr != NULL)
    { total += *ptr; num++;
      ptr = vecList->next();
    }

  total /= num;

//  printf("%i <%f %f %f>\n", num, total[0], total[1], total[2]);

  return total;
}


//// VpvSpiral ////
/*
VpvSpiral::VpvSpiral(VpVec loc, int num, float distance)
{ setNum(num); setDist(distance); }

SoNode* VpvSpiral::constructSpiral(int number, float dist) 
  //use number*4 for complete revs
{ SoSeparator *result = new SoSeparator;

  result->ref();

  SoLightModel *lmodel = new SoLightModel;
  SoDrawStyle *drawStyle = new SoDrawStyle;

  lmodel->model = SoLightModel::BASE_COLOR;
  drawStyle->lineWidth = 2;

  result->addChild(lmodel);
  result->addChild(drawStyle);

  SoComplexity *complexity =  new SoComplexity;
  SoCoordinate3 *controlPtr = new Socoordinate3;
  SoNurbsCurve *curve =        new SoNurbsCurve;

  complexity->value = 0.8;

  genPoints(number, dist);

  controlPts->point.setValues(0,number, points);
  curve->numControlPoints = number;
  curve->knotVector.setValues(0,number+3, knots);

  result->addChild(complexity);
  result->addChild(controlPts);
  result->addChild(curve);

  return result;
}



void VpvSpiral::genPoints(int number, float dist)
{ points = new (float *)[number];
  knots  = new float[number+3];
  float level = 0; 

  for(int i=0; i < number; i++, level+=dist) 
    { points[i] = new float[3];
      points[i][0] = i%2;
      points[i][1] = (i+1)%2;
      points[i][2] = level; 
    }

  for(i=0; i < number+3;) knots[i]=i++;
}
   */ 


//// VpvImage ////

VpvImage::VpvImage(VpObject *object, VpiPixmap *npixmap, SoCamera *ncamera,
		   VpvSimpleEnv *nenv) : VpvBase(object)
{ pixmap = npixmap;
  camera = ncamera;
  env = nenv;
  
  CB = new SoCallback;
  CB->setCallback(&VpvImage::callback, this);
  ObjSep->addChild(CB);
}

void VpvImage::show(int x, int y, float scale)
{ rectzoom(scale, scale);

  int xoff, yoff;
  
  //lsetdepth(
  //printf("Show called %i, %i, %f\n", x,y, scale);
  xoff = (int)((float)pixmap->getDimX() * scale / 2);
  yoff = (int)((float)pixmap->getDimY() * scale / 2);

  int blx = x-xoff, bly = y-yoff;

  unsigned long *data = pixmap->getImageData();

  lrectwrite(blx,bly,
	     blx+pixmap->getDimX()-1,
	     bly+pixmap->getDimY()-1,
	     data);
}

//Note:  the following sequence (my test of SoGetMatrixAction) works
// just dandy!

/*
void printv(VpVec a)
{ float x,y,z;
  a.getValue(x,y,z);
  printf("<%f %f %f>\n", x,y,z);
}
*/

//  printv(ptr->getObj()->getLoc());
//  SoGetMatrixAction GMA;
//  GMA.apply(ptr->transl);
//  GMA.getMatrix().print(stdout);


VpVec* getTransFromMatrix(SbMatrix matrx)
{ VpVec *a = new VpVec;

  for(int i=0; i<3; i++)
    (*a)[i] = matrx[3][i];
  
  return a;
}

void VpvImage::callback(void *data, SoAction *)
{ VpvImage *ptr = (VpvImage *) data; //this

  VpVec screenLoc, tmpVec = ptr->getObj()->GetLoc();;
  SbViewVolume vv;
  ptr->camera->getViewVolume(vv);

  vv.projectToScreen(tmpVec, screenLoc);
  
  for(int i=0; i<2; i++)
    if (screenLoc[i] < -1 || screenLoc[i] > 1) return;

  //The above should be adjusted to account for image size; meanwhile, it
  //allows for a bit of overlap

  //Here's some slightly hacked Growing Images stuff

  if (ptr->pixmap->scalingAvailable()) //We have a MS (for the moment)
    { int level = tmpVec[2] / -7;

      ((VpiPixmapMS *)ptr->pixmap)->setLevel(level);
    }


  SbVec2s windowSize = ptr->env->getWindowSize() / 2;
//  printf("{{%f %f %f}}\n", screenLoc[0], screenLoc[1], screenLoc[2]);

  ptr->show((int)(windowSize[0] * screenLoc[0]) + windowSize[0], 
	    (int)(windowSize[1] * screenLoc[1]) + windowSize[1], 0.5);

}

/// ImageD ///

VpvImageD::VpvImageD(VpObject *nobject, VpiPixmap *npixmap)
{ pixmap = npixmap; obj = nobject; 
}

/// ImageBank ///

VpvImageBank::VpvImageBank(SoCamera *ncamera, VpvSimpleEnv *nenv)
{ camera = ncamera; env = nenv;
  imageList = new ImageDList;
  sep = new SoSeparator;

  CB = new SoCallback;
  CB->setCallback(&VpvImageBank::callback, this);
  sep->addChild(CB);
}


void VpvImageBank::AddImage(VpvImageD *newImage)
{ imageList->prepend(newImage); }


void VpvImageBank::show(VpiPixmap *pixmap, int x, int y)
{
  int xoff, yoff;
  
  xoff = pixmap->getDimX() >> 1; // div 2
  yoff = pixmap->getDimY() >> 1;

  int blx = x-xoff, bly = y-yoff;

  unsigned long *data = pixmap->getImageData();

  lrectwrite(blx,bly,
	     blx+pixmap->getDimX()-1,
	     bly+pixmap->getDimY()-1,
	     data);
}


void VpvImageBank::callback(void *data, SoAction *)
{ VpvImageBank *t = (VpvImageBank *) data; //this
  SbViewVolume vv;

  if (t->imageList->length() < 1) return;

  if (t->camera == NULL)
    if (t->env->getCamera() != NULL)
      t->camera = t->env->getCamera();
    else return;

  //Of course, with this support, why ask for camera in the 
  //first place?  I'll assume that some day you might have multiple
  //cameras worked in somehow, so will leave this intact
  
  t->camera->getViewVolume(vv);

  t->imageList->resetMarker();
  VpvImageD *ptr = t->imageList->next();

  while (ptr != NULL)
    {      
      VpVec screenLoc, worldLoc = ptr->getObj()->GetLoc();;
      vv.projectToScreen(worldLoc, screenLoc);

      if (screenLoc[0] < -1 || screenLoc[0] > 1 ||
	  screenLoc[1] < -1 || screenLoc[1] > 1) 
	{ ptr = t->imageList->next(); continue; }

  //The above should be adjusted to account for image size; meanwhile, it
  //allows for a bit of overlap

  //Here's some slightly hacked Growing Images stuff

      if (ptr->getPixmap()->scalingAvailable()) //We have a MS (for the moment)
	{ int level = worldLoc[2] / -7;
	  
	  ((VpiPixmapMS *)ptr->getPixmap())->setLevel(level);
	}

      SbVec2s windowSize = t->env->getWindowSize() / 2;
      
      t->show(ptr->getPixmap(), 
	      (int)(windowSize[0] * screenLoc[0]) + windowSize[0], 
	      (int)(windowSize[1] * screenLoc[1]) + windowSize[1]);

      ptr = t->imageList->next();
    }
}

/// VpvSquare ////

VpvsSquare::VpvsSquare(VpVec loc, SoScale *nscale, float r, float g, float b)
{ material = new SoMaterial;
  ObjSep = new SoSeparator;
  scale = nscale;
  transl = new SoTranslation;

  setColor(r,g,b);
  bindLoc(loc);
}

void VpvsSquare::setColor(float r, float g, float b)
{ material->diffuseColor.setValue(r,g,b);
}

void VpvsSquare::makeSquare()
{
   static float verts[5][3] = {
     {-1,-1,0},
     { 1,-1,0},
     { 1, 1,0},
     {-1, 1,0},
     {-1,-1,0}};

   SoLineSet *ls = new SoLineSet();

   ls->startIndex.setValue(0);
   ls->numVertices.setValue(5);

   SoCoordinate3 *coord = new SoCoordinate3;
   coord->point.setValues(0, 5, verts);

   ObjSep->addChild(coord);
   ObjSep->addChild(ls);

}

void VpvsSquare::bindLoc(VpVec nloc)
{ loc = nloc;
  transl->translation.setValue(loc);

  ObjSep->ref();
  ObjSep->addChild(transl);
  ObjSep->addChild(material);
  ObjSep->addChild(scale);

  makeSquare();
}

//// VpvSquareArray ////

VpvSquareArray::VpvSquareArray(VpObject *obj, int numSubDivs, 
			       float ndist, float nscale)
{ numDivs = numSubDivs;
  squares = new VpvsSquare*[numDivs];
  scale = new SoScale;

  VpVec lscale(nscale, nscale, nscale);
  scale->scaleFactor.setValue(lscale);
  distance = ndist;

  bindObj(obj);
}


void VpvSquareArray::bindObj(VpObject *nobj)
{ obj = nobj;
  ObjSep->ref();

  ObjSep->addChild(transl);

  VpVec scanner = obj->getLoc();
  scanner[2] -= (distance * numDivs / 2);

  for(int i=0; i < numDivs; i++)
    { squares[i] = new VpvsSquare(scanner, scale);
      ObjSep->addChild(squares[i]->getShell());
      scanner[2] += distance;
    }
}

//// VpvPresenceIndicator ////

VpvPresenceIndicator::VpvPresenceIndicator(VpObject *obj, int numSubDivs, 
					   float distance,
					   float scale, VpVec orientation)
: VpvSquareArray(obj, numSubDivs, distance, scale)
{ VpVec FinalPoint = obj->getLoc() - numSubDivs/2 * distance * orientation;
  planar = new VpgPlane(FinalPoint, orientation);

  headCount = new int[numSubDivs];

  printf("Finalpoint: %f %f %f\n", FinalPoint[0], FinalPoint[1], 
	 FinalPoint[2]);

}


void VpvPresenceIndicator::activateProcessing(VpObjects *nobjects,
					      float timeBetweenUpdates)
{ objects = nobjects;

  scheduler = new VpTime;
  scheduler->AssertCallback(&VpvPresenceIndicator::update, this);
  scheduler->SetFrequency(1/timeBetweenUpdates);
  scheduler->StartTime();
}

void VpvPresenceIndicator::setColorBounds(float a[3], float b[3], 
					  int maxCount)
{ headMax = maxCount;

  for(int i=0; i<3; i++)
    { colorA[i] = a[i];
      colorB[i] = b[i];
      incremental[i] = (b[i] - a[i])/(float)maxCount;
    }
}

void VpvPresenceIndicator::update(void *data, VpSchedulerBase *)
{ VpvPresenceIndicator *t = (VpvPresenceIndicator *)data;
  //We need to prefix all internal references with the t because of the
  // static callback status
  
  //Clear old data
  for(int i=0; i<t->numDivs; i++)
    t->headCount[i]=0;

  if (t->objects->length() < 1) return;
  t->objects->resetMarker();
  VpObject *ptr = t->objects->first(); t->objects->next();

  //calculate headcount results

  while (ptr != NULL)
    { float dist = t->planar->dist(ptr->getLoc());
      dist /= t->distance;
      if (dist < 0 || dist > t->numDivs) return;
      t->headCount[(int) dist]++;

      ptr = t->objects->next();
    }

  //Update the color values

  for(i=0; i<t->numDivs; i++)
    { VpVec colorVal;

      if (t->headCount[i] >= t->headMax) colorVal = t->colorB;
      else colorVal = t->colorA + t->headCount[i] * t->incremental;

      t->squares[i]->setColor(colorVal[0], colorVal[1], colorVal[2]);
    }
}

/////////////////// VpvPulsingShape ////////////////////////


VpvPulsingShape::VpvPulsingShape(VpObject *newObj, SoNode *newShape, 
			 float npulseFreq, float ncallbackFreq) 
{ node = newShape;
  pulseFrequency = npulseFreq; callbackFrequency = ncallbackFreq;
  
  material = new SoMaterial;

  baseColor[0] = 0.9; baseColor[1]=baseColor[2]=0.1; 
     //Hardwire; make this passable

  selectedColor[0] = selectedColor[1] = 0.4; selectedColor[2] = 1.0;
  selectCount=0;

  material->diffuseColor.setValue(baseColor[0], baseColor[1], baseColor[2]);

  cycleInc = pulseFrequency*2 / callbackFrequency; //multiply by 2 for 2*pi*tau
  cycleState = 0;

  bindObj(newObj);
}

void VpvPulsingShape::bindObj(VpObject *nobj)
{ obj = nobj;

  transl->translation.setValue(obj->GetLoc());
  
  ObjSep->ref();
  ObjSep->addChild(transl);
  ObjSep->addChild(material);
  ObjSep->addChild(node);

  ///Execute self-scheduling part;

  scheduler = new VpTime;
  scheduler->AssertCallback(&VpvPulsingShape::callback, this);
  scheduler->SetFrequency(callbackFrequency);
  scheduler->StartTime();
} 

void VpvPulsingShape::callback(void *data, SoSensor *)
{ VpvPulsingShape *p = (VpvPulsingShape *) data;

  float transColor[3];

  if (p->selectCount % 2 == 0)
    for(int i=0; i<3; i++)
      transColor[i] = cos(M_PI*p->cycleState) * p->baseColor[i];
  else
    for(i=0; i<3; i++)
      transColor[i] = cos(M_PI*p->cycleState) * 2 * p->selectedColor[i];
    

  p->material->diffuseColor.setValue(transColor[0], transColor[1], 
				     transColor[2]);

  p->cycleState += p->cycleInc;
} 

void VpvPulsingShape::selected()
{ selectCount++; printf(" Pulsing Selected, count %i\n", selectCount); 
  cycleState = 0;
}
