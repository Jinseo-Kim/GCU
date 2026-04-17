#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ============================================================
// 희소 행렬 구조체 (삼중쌍 표현)
// ============================================================
#define MAX_TERMS 100

typedef struct
{
    int row, col, value;
} Term;

typedef struct
{
    int rows, cols, num_terms;
    Term terms[MAX_TERMS];
} SparseMatrix;

// ============================================================
// 일반 전치 (Naive Transpose) - O(cols * num_terms)
// ============================================================
SparseMatrix naive_transpose(SparseMatrix a)
{
    SparseMatrix b;
    b.rows = a.cols;
    b.cols = a.rows;
    b.num_terms = a.num_terms;

    if (a.num_terms == 0)
        return b;

    int idx = 0;
    for (int c = 0; c < a.cols; c++)
    {
        for (int i = 0; i < a.num_terms; i++)
        {
            if (a.terms[i].col == c)
            {
                b.terms[idx].row = a.terms[i].col;
                b.terms[idx].col = a.terms[i].row;
                b.terms[idx].value = a.terms[i].value;
                idx++;
            }
        }
    }
    return b;
}

// ============================================================
// 빠른 전치 (Fast Transpose) - O(cols + num_terms)
// ============================================================
SparseMatrix fast_transpose(SparseMatrix a)
{
    SparseMatrix b;
    b.rows = a.cols;
    b.cols = a.rows;
    b.num_terms = a.num_terms;

    if (a.num_terms == 0)
        return b;

    // 1단계: 각 열의 원소 개수 계산
    int row_count[MAX_TERMS] = {0};
    for (int i = 0; i < a.num_terms; i++)
        row_count[a.terms[i].col]++;

    // 2단계: 시작 위치(offset) 계산
    int row_start[MAX_TERMS] = {0};
    for (int c = 1; c < a.cols; c++)
        row_start[c] = row_start[c - 1] + row_count[c - 1];

    // 3단계: 전치 행렬 채우기
    for (int i = 0; i < a.num_terms; i++)
    {
        int pos = row_start[a.terms[i].col]++; // 현재 위치 후 증가
        b.terms[pos].row = a.terms[i].col;
        b.terms[pos].col = a.terms[i].row;
        b.terms[pos].value = a.terms[i].value;
    }

    return b;
}

// ============================================================
// 일반 2D 배열 전치 (Dense Matrix) - O(n*m)
// ============================================================
void transpose_2d(int **src, int **dst, int rows, int cols)
{
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            dst[j][i] = src[i][j];
}

// ============================================================
// 출력 유틸리티
// ============================================================
void print_sparse(SparseMatrix m, const char *label)
{
    printf("\n[%s] (%d x %d, %d개 원소)\n", label, m.rows, m.cols, m.num_terms);
    printf("  row  col  value\n");
    printf("  ---  ---  -----\n");
    for (int i = 0; i < m.num_terms; i++)
        printf("  %3d  %3d  %5d\n", m.terms[i].row, m.terms[i].col, m.terms[i].value);
}

// ============================================================
// 메인 테스트
// ============================================================
int main(void)
{
    // 희소 행렬 예시 (4x5)
    // 위치: (0,0)=1, (0,3)=2, (1,1)=3, (2,3)=4, (3,4)=5
    SparseMatrix a = {
        .rows = 4, .cols = 5, .num_terms = 5, .terms = {{0, 0, 1}, {0, 3, 2}, {1, 1, 3}, {2, 3, 4}, {3, 4, 5}}};

    print_sparse(a, "원본 행렬 A");

    SparseMatrix t1 = naive_transpose(a);
    print_sparse(t1, "일반 전치 결과");

    SparseMatrix t2 = fast_transpose(a);
    print_sparse(t2, "빠른 전치 결과");

    // 결과 비교
    printf("\n[검증] 두 결과 일치 여부: ");
    int match = (memcmp(t1.terms, t2.terms, sizeof(Term) * t1.num_terms) == 0);
    printf("%s\n", match ? "✓ 일치" : "✗ 불일치");

    return 0;
}