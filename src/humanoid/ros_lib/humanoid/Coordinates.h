#ifndef _ROS_humanoid_Coordinates_h
#define _ROS_humanoid_Coordinates_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace humanoid
{

  class Coordinates : public ros::Msg
  {
    public:
      typedef float _y_type;
      _y_type y;
      typedef float _x_type;
      _x_type x;

    Coordinates():
      y(0),
      x(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      offset += serializeAvrFloat64(outbuffer + offset, this->y);
      offset += serializeAvrFloat64(outbuffer + offset, this->x);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->y));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->x));
     return offset;
    }

    virtual const char * getType() override { return "humanoid/Coordinates"; };
    virtual const char * getMD5() override { return "aedfd35910af15d9f768c14bffadd55d"; };

  };

}
#endif
