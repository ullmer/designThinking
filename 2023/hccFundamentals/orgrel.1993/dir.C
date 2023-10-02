int
GD_readDir(GD_Dir, path)

GopherDirObj *GD_Dir;
char *path;

{ DIR *dirp;
  struct dirent *dp;
  GopherStruct *tmpgs;
  char fp1[150], full_path[150];
  int number=1;

  tmpgs = GSnew();
  GSinit(tmpgs);
  GSsetHost(tmpgs,LOCALHOST);
  GSsetPort(tmpgs,GOPHER_PORT);
  strcpy(fp1,path); strcat(fp1,"\/");
	     
  dirp=opendir(path);
  for(dp=readdir(dirp); dp!=NULL; dp=readdir(dirp))
    {if (dp->d_name == NULL) {printf("ARG!\n"); exit(-1);}
     GSsetTitle(tmpgs,dp->d_name);
     strcpy(full_path,fp1); 
     strcat(full_path,dp->d_name);
     
     GSsetType(tmpgs,((is_dir(full_path))?'1':'0'));
     GSsetPath(tmpgs,full_path);

     if (number>2) GDaddGS(GD_Dir,tmpgs); /*Avoid "." and ".."*/
     number++;
    }
  closedir(dirp);
  GSdestroy(tmpgs);
}


