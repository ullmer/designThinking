#include "w3err.h"

////////////////////////// w3_error //////////////////////////

 /*
  * From SGI Irix vprintf man pages
  *
  *   error should be called as:
  *   error(function_name, format, arg1, arg2 ...);
  */

void
w3_error(char *function_name, char *format, ...)
 {

      char errstr[200];
      va_list args;

      va_start(args, format);
      /* print out remainder of message */
      vsprintf(errstr, format, args);

#ifdef WIN32
      WinMessage(errstr);
#else
      fprintf(stderr, "%s\n", errstr);
#endif

      va_end(args);
 }

////// END ////////

