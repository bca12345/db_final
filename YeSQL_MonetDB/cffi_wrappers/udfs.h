extern int cleancode_wrapped(char* input, int size, char** result);
extern int cancelledbool_wrapped(double* input, int size, uint8_t * result);
extern int divertedmap_wrapped(double * input1, char* input2,  int size, char** result);
extern int fillInTimesUDF_wrapped(double* input1, char** input2, char** input3, int size, double* result);
extern int gettime_wrapped(int* input, int size, char** result);
extern int getcity_wrapped(char** input, int size, char** result);
extern int getstate_wrapped(char** input, int size, char** result);
extern int defunctyear_wrapped(char** input, int size, int* result);
extern int getairlinename_wrapped(char** input, int size, char** result);
extern int getairlineyear_wrapped(char** input, int size, int* result);
extern int extractbd_wrapped(char** input, int size, int* result);
extern int extracttype_wrapped(char** input, int size, char** result);
extern int extractpcode_wrapped(char** input, int size, char** result);
extern int extractba_wrapped(char** input, int size, int* result);
extern int extractsqfeet_wrapped(char** input, int size, int* result);
extern int extractprice_sell_wrapped(char** input, int size, int* result);

