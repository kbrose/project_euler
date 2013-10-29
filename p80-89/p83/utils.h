/* utils.h */

#ifndef _UTILS_H
#define _UTILS_H

/* allocate space for new string, initialize all chars to '\0' */
char *string_init(int sz);

/* return new string stripped of leading and trailing spaces */
/*   (including \n and \t) */
char *trim(char *s);

#endif /* _UTILS_H */
