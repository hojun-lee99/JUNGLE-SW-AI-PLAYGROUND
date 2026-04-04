#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct USERDATA
{
  int age;
  char name[32];
  char phone[32];
  struct USERDATA* pNext;
} USERDATA;

USERDATA *g_HeadNode = NULL;

void appendNewNode(int age, const char *pszName, const char *pszPhone) {
  USERDATA *pNewNode = (USERDATA*)malloc(sizeof(USERDATA));
  pNewNode->age = age;
  strlcpy(pNewNode->name, pszName, sizeof(pNewNode->name));
  strlcpy(pNewNode->phone, pszPhone, sizeof(pNewNode->phone));
  pNewNode->pNext = NULL;

  if(g_HeadNode == NULL) {
    g_HeadNode = pNewNode;
  }
  else {
    // stack 구조
    // pNewNode->pNext = g_HeadNode;
    // g_HeadNode = pNewNode;

    // queue 구조
    USERDATA *pTail = g_HeadNode;

    while (pTail->pNext != NULL)
    {
      pTail = pTail->pNext;
    }

    pTail->pNext = pNewNode;
  }
}

void releaseList() {
  USERDATA* pTmp = g_HeadNode;
  USERDATA* pDelete;

  while (pTmp != NULL)
  {
    pDelete = pTmp;
    pTmp = pTmp->pNext;

    printf("Delete: [%p] %d, %s, %s [%p]\n", pDelete, pDelete->age, pDelete->name, pDelete->phone, pDelete->pNext);

    free(pDelete);
  }

  g_HeadNode = NULL;
}

USERDATA* searchByName(const char* pszName) {
  USERDATA* pTmp = g_HeadNode;

  while (pTmp != NULL)
  {
    if(strcmp(pTmp->name, pszName) == 0) {
      printf("\"%s\": Found\n", pszName);
      return pTmp;
    }
    pTmp = pTmp->pNext;
  }

  printf("\"%s\": Not found\n", pszName);
  return NULL;
}

USERDATA* searchRemoveNode(USERDATA **ppPrev, char *pszName) {
  USERDATA *pCur = g_HeadNode;
  USERDATA *pPrev = NULL;

  while (pCur != NULL)
  {
    if(strcmp(pCur->name, pszName) == 0) {
      printf("\"%s\": Found\n", pszName);
      *ppPrev = pPrev;
      return pCur;
    }
    pPrev = pCur;
    pCur = pCur->pNext;
  }
  
  printf("\"%s\": Not found\n", pszName);
  return NULL;
}

void removeNode(USERDATA *pPrev) {
  USERDATA *pRemove = NULL;

  if (pPrev == NULL) {
    if (g_HeadNode != NULL){
      pRemove = g_HeadNode;
      g_HeadNode = g_HeadNode->pNext;
      free(pRemove);
    }

    return;
  }

  pRemove = pPrev->pNext;
  pPrev->pNext = pRemove->pNext;
  free(pRemove);
}

void PrintList(void) {
  USERDATA* pTmp = g_HeadNode;

  while (pTmp != NULL)
  {
    printf("[%p] %d, %s, %s [%p]\n", pTmp, pTmp->age, pTmp->name, pTmp->phone, pTmp->pNext);
    pTmp = pTmp->pNext;
  }
  putchar('\n');
}


void TestStep02(void) {
  puts("TestStep02-------------------------");
  appendNewNode(28, "lee", "010-1111-1111");
  appendNewNode(28, "ho", "010-2222-2222");
  appendNewNode(20, "jun", "010-3333-3333");

  PrintList();

  USERDATA *pPrev = NULL;

  if(searchRemoveNode(&pPrev, "ho")) {
    removeNode(pPrev);
  }

  PrintList();  
  
  releaseList();

  putchar('\n');
}

void TestStep03(void) {
  puts("TestStep03-------------------------");
  appendNewNode(28, "lee", "010-1111-1111");
  appendNewNode(28, "ho", "010-2222-2222");
  appendNewNode(20, "jun", "010-3333-3333");

  PrintList();

  USERDATA *pPrev = NULL;

  if(searchRemoveNode(&pPrev, "jun")) {
    removeNode(pPrev);
  }

  PrintList();  
  
  releaseList();

  putchar('\n');
}

void TestStep01(void) {
  puts("TestStep01-------------------------");
  appendNewNode(28, "lee", "010-1111-1111");
  appendNewNode(28, "ho", "010-2222-2222");
  appendNewNode(20, "jun", "010-3333-3333");

  PrintList();

  USERDATA *pPrev = NULL;

  if(searchRemoveNode(&pPrev, "lee")) {
    removeNode(pPrev);
  }

  PrintList();  
  
  releaseList();

  putchar('\n');
}

void TestStep04(void) {
  puts("TestStep01-------------------------");
  appendNewNode(28, "lee", "010-1111-1111");
  appendNewNode(28, "ho", "010-2222-2222");
  appendNewNode(20, "jun", "010-3333-3333");

  PrintList();

  USERDATA *pPrev = NULL;

  if(searchRemoveNode(&pPrev, "kim")) {
    removeNode(pPrev);
  }

  PrintList();  
  
  releaseList();

  putchar('\n');
}



int main(void) {  
  TestStep01();
  TestStep02();
  TestStep03();
  TestStep04();

  return 0;
}