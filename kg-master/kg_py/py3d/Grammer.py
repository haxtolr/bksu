
from sevenSegment import getSevSegStr

# (!) Change this to any number of seconds:
secondsLeft = 25

try:
    while secondsLeft >= 0:
        # Clear the output cell
        clear_output(wait=True)

        # 남은 시간/분/초 형식으로 기록하기
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)

        # sevenSegments 모듈 사용하기
        hDigits = getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # 남은 시간 표시하기
        print(hTopRow + '     ' + mTopRow + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        if secondsLeft == 0:
            print()
            print('    * * * * 완료! * * * *')
            break

        print('\nPress Ctrl-C to quit.')

        time.sleep(1)  # 1초 단위로 카운트 다운하기
        secondsLeft -= 1
except KeyboardInterrupt:
    pass  # Ctrl-C 를 누르면 끝내기