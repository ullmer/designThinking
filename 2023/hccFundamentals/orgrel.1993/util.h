//// Utility routines for VP Environment ////

#ifndef _VP_UTIL_
#define _VP_UTIL_

#include "vp.h"
#include <signal.h>

class VpSysScheduler //Make arguments compatible with Inventor SoTimerSensor
{ public:
    VpSysScheduler(void (*func)(), void *data);
    void schedule(timeporter.translate(UserCallBackInterval));
    void unschedule();
  protected:

}



#endif
