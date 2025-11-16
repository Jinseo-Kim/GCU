#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main ()
{
    printf("202533713 김진서\n");

    int human, com; // 사람과 컴퓨터가 낸 가위, 바위, 보를 저장할 변수
    int diff; // human - com을 통해 승리자를 가려내기 위한 변수
    int win_human = 0, win_com = 0; // 승리 횟수를 저장할 변수

    srand(time(NULL));

    printf("가위바위보 게임\n");
    printf("컴퓨터 : 0승 0패, 당신 : 0승 0패\n");

    for (int cnt = 1; cnt <= 5; cnt++)
    {
        printf("(라운드 %d)\n", cnt);

        while (1)
        {
            com = rand(); // 랜덤한 0 ~ 32767까지의 값이 들어옴

            if (com == 0 || com == 1 || com == 2) // 0, 1, 2 값이 나왔을 때만 사용하기 위함
            {
                printf("컴퓨터가 결정했습니다.\n");

                printf("무엇을 내시겠습니까? (가위: 0, 바위: 1, 보: 2)");
                scanf("%d", &human);

                if (human == com)
                    printf("무승부입니다. 다시 시작합니다.\n");
                else
                    break;
            }
        }

        diff = human - com; // 결과값: 1, -1, 2, -2

        // 사람이 이겼을 때 (바위 - 가위, 보 - 바위: 1)
        if (diff == 1)
        {
            if (human == 2)
                printf("컴퓨터는 바위, 당신은 보, 당신이 이겼습니다.\n");
            else
                printf("컴퓨터는 가위, 당신은 바위, 당신이 이겼습니다.\n");
            win_human += 1;
        }

        // 컴퓨터가 이겼을 때 (바위 - 가위, 보 - 바위: -1)
        if (diff == -1)
        {
            if (com == 2)
                printf("컴퓨터는 보, 당신은 바위, 컴퓨터가 이겼습니다.\n");
            else
                printf("컴퓨터는 바위, 당신은 가위, 컴퓨터가 이겼습니다.\n");
            win_com += 1;
        }

        // 가위가 보를 이겼을 때 (2 또는 -2)
        if (diff == 2 || diff == -2)
        {
            if (human == 2)
            {
                printf("컴퓨터는 가위, 당신은 보, 컴퓨터가 이겼습니다.\n");
                win_com += 1;
            }

            if (com == 2)
            {
                printf("컴퓨터는 보, 당신은 가위, 당신이 이겼습니다.\n");
                win_human += 1;
            }
        }
        
        // 승 = win_humanm, win_com     패 = 진행된 라운드 - 승리 횟수
        printf("컴퓨터 : %d승 %d패, 당신 : %d승 %d패\n\n", win_com, (cnt - win_com), win_human, (cnt - win_human));
            
    }
}

