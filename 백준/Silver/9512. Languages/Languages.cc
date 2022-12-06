#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
using namespace std ;
const int BUFSIZE = 1024 ;
char sent[BUFSIZE] ;
vector<char *> parseline(char *s) {
   vector<char *> r ;
   char *ws = 0 ;
   char *end = s + strlen(s) ;
   for (char *p=s; p <= end; p++) {
      if (('a' <= *p && *p <= 'z') || ('A' <= *p && *p <= 'Z')
           || *p == '\'' || *p == '-') {
         if (ws == 0)
            ws = p ;
      } else {
         if (ws != 0) {
            *p = 0 ;
            r.push_back(strdup(ws)) ;
            ws = 0 ;
         }
      }
   }
   return r ;
}
int main(int argc, char *argv[]) {
   vector<vector<char *> > lines ;
   int nlang = 0 ;
   fgets(sent, BUFSIZE, stdin) ;
   int n = atol(sent) ;
   while (fgets(sent, BUFSIZE, stdin)) {
      vector<char *> parsed = parseline(sent) ;
      if (parsed.size() == 0) {
         nlang = lines.size() ;
         if (nlang != n)
            cerr << "Bad match of language count " << nlang << " " << n << endl ;
      } else if (nlang) {
         int matched = 0 ;
         for (int i=0; matched == 0 && i<nlang; i++)
            for (int j=0; matched == 0 && j<parsed.size(); j++)
               for (int k=1; matched == 0 && k<lines[i].size(); k++)
                  if (strcasecmp(parsed[j], lines[i][k]) == 0) {
                     cout << lines[i][0] << endl ;
                     matched = 1 ;
                  }
         if (!matched)
            cout << "Unknown" << endl ;
      } else
         lines.push_back(parsed) ;
   }
}