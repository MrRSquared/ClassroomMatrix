//This is my first attempt at making a pixel mapper.
#include "pixel-mapper.h"

RegisterPixelMapper(new MyOwnPixelMapper());
   RGBMatrix *matrix = rgb_matrix::CreateMatrixFromFlags(...);