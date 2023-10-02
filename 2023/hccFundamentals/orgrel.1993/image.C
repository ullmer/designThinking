#include "image.h"

VpiBase::VpiBase()
{ filename=NULL; }

VpiBase::VpiBase(char *filename)
{ setFilename(filename); 
  bindImage();
}

////

void VpiTexture::bindImage()
{ if (filename == NULL) return;
  
  texture = new SoTexture2;
  texture->filename.setValue(filename);
  texture->component.setValue(SoTexture2::INTENSITY);
}

SoTexture2* VpiTexture::getBoundImage()
{ if (texture != NULL)
    return texture;
}

////


void VpiPixmap::readFile()
{ FILE *in = fopen(filename, "rb");
  char str[10];
  int dummy;
  unsigned char *lptr;
  unsigned char *fileData, *bptr;
  char a, b;
  int color;

  if (in == NULL)
    {printf("Can't find data file \"%s\"!\n",filename); exit(-1);}

  fscanf(in,"%c%c", &a, &b);

  if (a != 'P')
    { fprintf(stderr, "\"%s\" is not a PBMPLUS-type image!\nAborting...\n",
	      filename);
      exit(-1);
    }

  if (b == '6') color=1;
  else if (b == '5') color=0;
  else 
    { fprintf(stderr, "\"%s\" is of image type P%c; only P5 and P6 currently"
	      "understood!\nAborting...\n", filename, b);
      exit(-1);
    }

  fscanf(in,"%i %i\n%i\n", &dimX, &dimY, &dummy);

  image = new unsigned long[dimX*dimY];
  fileData = new unsigned char[dimX*dimY*(color?3:1)];
  fread(fileData, dimX*dimY, (color?3:1), in);
  fclose(in);

  lptr = (unsigned char *) image;

  //Image must be inverted to swap from Pixmap to SGI format...
  if (color)
    for(int j=(dimY-1); j>=0; j--)
      { bptr = fileData + j*dimX*3;
	
	for(int i=0; i<dimX; i++, lptr+=4, bptr+=3)
	  { lptr[1]=bptr[2]; lptr[2]=bptr[1]; lptr[3]=bptr[0];
	    lptr[0]=0; //255; //Alpha value
	  }
      }
  else //not color
    for(j=(dimY-1); j>=0; j--)
      { bptr = fileData + j*dimX;
	
	for(int i=0; i<dimX; i++, lptr+=4, bptr++)
	  { lptr[1]=lptr[2]=lptr[3] = *bptr;
	    lptr[0]=100; //255; //Alpha value
	  }
      }
    
  delete fileData;
}

VpiPixmap::VpiPixmap(VpiPixmap *base, float scale)
{ dimX = scale * base->getDimX();
  dimY = scale * base->getDimY();

  float scaleX = (float) base->getDimX() / getDimX();
  float scaleY = (float) base->getDimY() / getDimY();

  image = new unsigned long[dimX * dimY];

  int max = dimX * dimY;

  float fi=0;

  for(int i=0; i < max; i++, fi += scaleX)
    { image[i] = base->image[(int) fi];
      if (i % dimX == 0) fi = (int)(scaleY * i/dimX)*base->getDimX();
      //Second line necessary for dealing with incremental Y resolution
      //Sufficient error checking *may not* be present
    }

}  

void VpiPixmap::bindImage()
{ readFile(); }

////

VpiPixmapMS::VpiPixmapMS(char *filename, int nnumIncs, float nscaleIncs)
{ numIncs = nnumIncs; scaleIncs = nscaleIncs;

  if (numIncs < 1) { pixmaps = NULL; return; }

  pixmaps = new VpiPixmap*[numIncs];
  pixmaps[0] = new VpiPixmap(filename);
  
  dimX = pixmaps[0]->getDimX();
  dimY = pixmaps[0]->getDimY();
  image = pixmaps[0]->getImageData();
  
  for(int i=1; i<numIncs; i++)
    pixmaps[i] = new VpiPixmap(pixmaps[0], pow(scaleIncs, i));
} 


///Very evil things happen if you try to define the following as an inline
// function, due to the Virtuality of it all.

unsigned long* VpiPixmapMS::getImageData(int num)
{
  return pixmaps[num]->getImageData();
}

void VpiPixmapMS::setLevel(int num)
{ if (num < 0) num = 0;
  if (num >= numIncs) num = numIncs - 1;

  image = pixmaps[num]->getImageData();
  dimX = pixmaps[num]->getDimX();
  dimY = pixmaps[num]->getDimY();
}
