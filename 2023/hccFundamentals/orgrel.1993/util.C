//// Code for Vp Utility functions

#include "util.h"

VpSysScheduler::VpSysScheduler(void (*func)(), void *data)
{ (*signal)(SIGALRM,func);
