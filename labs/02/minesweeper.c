#include <stdio.h>
#include <stdlib.h>

int increment_adjacent(int **field, int curr_r, int curr_c);

int main(int charc, char *argv[])
{

    int rows, cols;
    char mine = '*';

    scanf("%d %d", &rows, &cols);

    char **arr = (char **)calloc(rows, sizeof(char *));
    for (size_t i = 0; i < rows; i++)
        arr[i] = (char *)calloc(cols, sizeof(char));

    for (size_t i = 0; i < rows; i++)
        for (size_t j = 0; j < cols; j++)
        {
            char curr_char = getchar();
            if (curr_char == mine)
            {
                arr[i][j] =
            }
        }

    for (i = 0; i < r; i++)
        for (j = 0; j < c; j++)
            printf("%d ", arr[i][j]);

    for (int i = 0; i < r; i++)
        free(arr[i]);

    free(arr);

    return 0;
}

int increment_adjacent(int **field, int curr_r, int curr_c)
{
}
