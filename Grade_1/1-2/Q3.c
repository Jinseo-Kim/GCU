#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main ()
{
    printf("202533713 김진서\n");

    int human, com;
    int win_human = 0, win_com = 0;
    int scis = 0, rock = 1, paper = 2;

    srand(time(NULL));

    printf("가위바위보 게임\n");
    printf("컴퓨터 : 0승 0패, 당신 : 0승 0패\n");

    for (int cnt = 1; cnt <= 5; cnt++)
    {
        printf("라운드 %d\n", cnt);

        while (1)
        {
            com = rand();

            if (com == 0 || com == 1 || com == 2)
            {
                printf("컴퓨터가 결정했습니다.\n");

                printf("무엇을 내시겠습니까? (가위: 0, 바위: 1, 보: 2)");
                scnaf(" %d", &human);

                if (human == com)
                    printf("무승부입니다. 다시 시작합니다.\n");
                else
                    break;
            }
        
        if (human > com)
        {
            printf("컴퓨터는 %s, 당신은 %s, 당신이 이겼습니다.\n");
            win_human += 1;
        }
        else
        {
            printf("컴퓨터는 %s, 당신은 %s, 컴퓨터가 이겼습니다.\n");
            win_com += 1;
        }
        
        printf("컴퓨터 : %d승 %d패, 당신 : %d승 %d패\n", win_human, cnt - win_human, win_com, cnt - win_com);
            
    }
    


}

