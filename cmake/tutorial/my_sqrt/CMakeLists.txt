add_library(my_sqrt my_sqrt.c)
#add_library(MathFunctions mysqrt.cxx)
install (TARGETS my_sqrt DESTINATION lib)
install (FILES my_sqrt.h DESTINATION include)
