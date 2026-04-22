CC = gcc
CFLAGS = -g -Wall
LIBS = -lpthread

all: echoclient echoserveri

echoclient: echoclient.o csapp.o
	$(CC) $(CFLAGS) -o echoclient echoclient.o csapp.o $(LIBS)

echoserveri: echoserveri.o csapp.o
	$(CC) $(CFLAGS) -o echoserveri echoserveri.o csapp.o $(LIBS)

echoclient.o: echoclient.c csapp.h
	$(CC) $(CFLAGS) -c echoclient.c

echoserveri.o: echoserveri.c csapp.h
	$(CC) $(CFLAGS) -c echoserveri.c

csapp.o: csapp.c csapp.h
	$(CC) $(CFLAGS) -c csapp.c

clean:
	rm -f *.o echoclient echoserveri *~
