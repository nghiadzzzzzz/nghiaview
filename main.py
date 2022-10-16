import datetime
import random
import time
import inquirer
from colorama import init, Fore
from src import process


def main():
    init(autoreset=True)
    inject = process.ZefoyViews()
    print(
        Fore.GREEN + """
      _____ _ _  __   ___
     |_   _(_) |_\ \ / (_)_____ __ _____
       | | | | / /\ V /| / -_) V  V (_-<
       |_| |_|_\_\ \_/ |_\___|\_/\_//__/
       make with ❤️️ by @Nghĩa dzaiiii
    """
    )
    print(Fore.LIGHTYELLOW_EX + "Example: đéo có demo đâu haha")
    url_video = input("Ném link video vô đây đi ku: ")

    questions = [
        inquirer.List('type',
                      message="What services do you need?",
                      choices=['Lượt xem', 'Chia sẻ', 'Yêu thich'],
                      ),
    ]
    answers = inquirer.prompt(questions)

    inject.get_session_captcha()
    time.sleep(1)

    if inject.post_solve_captcha(captcha_result=inject.captcha_solver()):

        print("\n[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + "vượt captcha thành công" + "\n")

        if answers['type'] == 'Lượt xem':

            while True:
                inject_views = inject.send_views(
                    url_video=url_video
                )

                if inject_views:

                    if inject_views['message'] == "Please try again later":
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_views['message'])
                        exit()

                    elif inject_views['message'] == 'Another State':
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + "Tổng số view: " +
                              inject_views['data'], end="\n\n")


                    elif inject_views['message'] == "Gửi view thành công.":
                        print("[ " + str(
                            datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + inject_views[
                                  'message'] + " to " + Fore.LIGHTYELLOW_EX + "" + url_video,
                              end="\n\n")

                    elif inject_views['message'] == "Session Expired. Please Re Login!":
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_views['message'])
                        exit()

                    # elif inject_views['message'] == "Please try again later. Server too busy.":
                    #     print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_views['message'])
                    #     exit()

                    else:
                        for i in range(int(inject_views['message']), 0, -1):
                            print("[ " + str(
                                datetime.datetime.now()) + " ] " + Fore.LIGHTYELLOW_EX + "Mày phải chờ " + str(
                                i) + " giây để gửi lại lượt xem.", end="\r")
                            time.sleep(1)

                    time.sleep(random.randint(1, 5))

                else:
                    pass

        elif answers['type'] == 'Chia sẻ':

            while True:
                inject_shares = inject.send_shares(
                    url_video=url_video
                )

                if inject_shares:

                    if inject_shares['message'] == "Please try again later":
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_shares['message'])
                        exit()

                    elif inject_shares['message'] == 'Another State':
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + "Tổng lượt chia sẻ : " +
                              inject_shares['data'], end="\n\n")


                    elif inject_shares['message'] == "Gửi thành công lượt chia sẻ.":
                        print("[ " + str(
                            datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + inject_shares[
                                  'message'] + " to " + Fore.LIGHTYELLOW_EX + "" + url_video,
                              end="\n\n")

                    elif inject_shares['message'] == "Session Expired. Please Re Login!":
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_shares['message'])
                        exit()

                    # elif inject_shares['message'] == "Please try again later. Server too busy.":
                    #     print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_shares['message'])
                    #     exit()

                    else:
                        for i in range(int(inject_shares['message']), 0, -1):
                            print("[ " + str(
                                datetime.datetime.now()) + " ] " + Fore.LIGHTYELLOW_EX + "Mày chờ " + str(
                                i) + " giây để gửi lại lượt chia sẻ.", end="\r")
                            time.sleep(1)

                    time.sleep(random.randint(1, 5))

                else:
                    pass

        elif answers['type'] == 'Yêu Thích':

            while True:
                inject_favorites = inject.send_favorites(
                    url_video=url_video
                )

                if inject_favorites:

                    if inject_favorites['message'] == "Please try again later":
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_favorites[
                            'message'])
                        exit()

                    elif inject_favorites['message'] == 'Another State':
                        print(
                            "[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + "Tổng lượt yêu thích : " +
                            inject_favorites['data'], end="\n\n")

                    elif inject_favorites['message'] == "Gửi lượt yêu thích thành công.":
                        print("[ " + str(
                            datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + inject_favorites[
                                  'message'] + " to " + Fore.LIGHTYELLOW_EX + "" + url_video,
                              end="\n\n")

                    elif inject_favorites['message'] == "Session Expired. Please Re Login!":
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_favorites[
                            'message'])
                        exit()

                    # elif inject_favorites['message'] == "Please try again later. Server too busy.":
                    #     print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_favorites[
                    #         'message'])
                    #     exit()

                    else:
                        for i in range(int(inject_favorites['message']), 0, -1):
                            print("[ " + str(
                                datetime.datetime.now()) + " ] " + Fore.LIGHTYELLOW_EX + "Mày chờ " + str(
                                i) + " giây để gửi lại lượt yêu thích.", end="\r")
                            time.sleep(1)

                    time.sleep(random.randint(1, 5))

                else:
                    pass

    else:
        print(Fore.RED + "Không giải được captcha.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "Exit")
        exit()
