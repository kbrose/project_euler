all: dj

dj: utils.c main.c commands.c hash-table.c linked-list.c parse.c vert-edge.c dj.c commands.h dj.h linked-list.h hash-table.h main.h utils.h vert-edge.h
	gcc -o dj commands.c dj.c utils.c hash-table.c linked-list.c parse.c vert-edge.c main.c

clean:
	rm -f dj test-utils
