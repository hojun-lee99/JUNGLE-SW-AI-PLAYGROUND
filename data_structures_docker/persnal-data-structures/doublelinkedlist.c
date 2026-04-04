#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct USERDATA
{
  int age;
  char name[32];
  char phone[32];
  struct USERDATA* pNext;
  struct USERDATA* pPrev;
} USERDATA;

// USERDATA *g_HeadNode = NULL;
USERDATA g_HeadNode = {0, "__dummy Head Node__"};
USERDATA g_TailNode = {0, "__dummy Tail Node__"};

void appendNewNode(int age, const char *pszName, const char *pszPhone) {
  USERDATA *NewNode = (USERDATA*)malloc(sizeof(USERDATA));
  NewNode->age = age;
  strlcpy(NewNode->name, pszName, sizeof(NewNode->name));
  strlcpy(NewNode->phone, pszPhone, sizeof(NewNode->phone));
  NewNode->pPrev = NULL;
  NewNode->pNext = NULL;

  USERDATA* PrevNode = g_TailNode.pPrev;
  NewNode->pPrev = PrevNode;
  NewNode->pNext = &g_TailNode;
  PrevNode->pNext = NewNode;
  g_TailNode.pPrev = NewNode;
}

void InitList() {
  g_HeadNode.pNext = &g_TailNode;
  g_TailNode.pPrev = &g_HeadNode;
}

void releaseList() {
  USERDATA* pTmp = g_HeadNode.pNext;
  USERDATA* pDelete = NULL;

  while (pTmp != NULL && pTmp != &g_TailNode)
  {
    pDelete = pTmp;
    pTmp = pTmp->pNext;

    printf("Delete: [%p] %d, %s, %s [%p]\n", pDelete, pDelete->age, pDelete->name, pDelete->phone, pDelete->pNext);

    free(pDelete);
  }

  InitList();
}

USERDATA* searchByName(const char* pszName) {
  USERDATA* pTmp = &g_HeadNode;

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

USERDATA* searchRemoveNode(char *pszName) {
  USERDATA *pCurNode = &g_HeadNode;

  while (pCurNode->pNext != NULL)
  {
    if(strcmp(pCurNode->name, pszName) == 0) {
      printf("\"%s\": Found\n", pszName);
      return pCurNode;
    }
    pCurNode = pCurNode->pNext;
  }
  
  printf("\"%s\": Not found\n", pszName);
  return NULL;
}

//todo prev 포인터 정리 필요
void removeNodeByPrev(USERDATA *pRemove) {
  USERDATA *pPrevNode = pRemove->pPrev;
  USERDATA *pNextNode = pRemove->pNext;

  pPrevNode->pNext = pRemove->pNext;
  pNextNode->pPrev = pRemove->pPrev;

  if (pRemove == NULL) {
    return;
  }

  free(pRemove);
}

void PrintList(void) {
  USERDATA* pTmp = &g_HeadNode;

  while (pTmp != NULL)
  {
    printf("[%p] %d, %s, %s [%p]\n", pTmp, pTmp->age, pTmp->name, pTmp->phone, pTmp->pNext);
    pTmp = pTmp->pNext;
  }
  putchar('\n');
}

// reverse로 변경
void PrintListReverse(void) {
  USERDATA* pTmp = &g_TailNode;

  while (pTmp != NULL)
  {
    printf("[%p] %d, %s, %s [%p]\n", pTmp, pTmp->age, pTmp->name, pTmp->phone, pTmp->pNext);
    pTmp = pTmp->pPrev;
  }
  putchar('\n');
}

void TestStep01(void) {
  puts("TestStep01-------------------------");
  appendNewNode(28, "lee", "010-1111-1111");
  appendNewNode(28, "ho", "010-2222-2222");
  appendNewNode(20, "jun", "010-3333-3333");

  PrintList();

  USERDATA *pPrev = searchRemoveNode("lee");

  if(pPrev) {
    removeNodeByPrev(pPrev);
  }

  PrintList();  
  PrintListReverse();
  
  releaseList();

  putchar('\n');
}

void TestStep02(void) {
  puts("TestStep02-------------------------");
  appendNewNode(28, "lee", "010-1111-1111");
  appendNewNode(28, "ho", "010-2222-2222");
  appendNewNode(20, "jun", "010-3333-3333");

  PrintList();
  PrintListReverse();

  USERDATA *pPrev = searchRemoveNode("ho");

  if(pPrev) {
    removeNodeByPrev(pPrev);
  }

  PrintList();  
  PrintListReverse();  
  
  releaseList();

  putchar('\n');
}

void TestStep03(void) {
  puts("TestStep03-------------------------");
  appendNewNode(28, "lee", "010-1111-1111");
  appendNewNode(28, "ho", "010-2222-2222");
  appendNewNode(20, "jun", "010-3333-3333");

  PrintList();

  USERDATA *pPrev = searchRemoveNode("jun");

  if(pPrev) {
    removeNodeByPrev(pPrev);
  }

  PrintList();  
  PrintListReverse();  
  
  releaseList();

  putchar('\n');
}


void TestStep04(void) {
  puts("TestStep04-------------------------");
  appendNewNode(28, "lee", "010-1111-1111");
  appendNewNode(28, "ho", "010-2222-2222");
  appendNewNode(20, "jun", "010-3333-3333");

  PrintList();

  USERDATA *pPrev = searchRemoveNode("kim");

  if(pPrev) {
    removeNodeByPrev(pPrev);
  }

  PrintList();  
  PrintListReverse();  
  
  releaseList();

  putchar('\n');
}



int main(void) {
  InitList();
  TestStep01();
  TestStep02();
  TestStep03();
  TestStep04();

  return 0;
}