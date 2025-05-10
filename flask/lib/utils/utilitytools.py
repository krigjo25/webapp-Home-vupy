#   Utility tools for the application

class UtilityTools(object):

    def Announcements(self, now):
        match (now):

            case _ if now.month == 2 and now.day > 9 and now.day < 15:
                message ="💖 Happy Valentines Day 💖"

            case _ if now.month == 2 and now.day == 25:
                message ="🎂 Happy Birthday @krigjo25 🎁"

            case _ if now.month == 5 and now.day < 18 and now.month == 5 and now.day > 9:
                message ="🇳🇴 Happy Independence Day Norway 🇳🇴"

            case _ if now.month == 10 and now.day > 20 and now.month == 11 and now.day < 1:
                message ="👻 Happy Halloween 👻"

            case _ if now.month == 12 and now.day > 10 and now.day < 26:
                message ="🎅 Merry Christmas ! 🎅"

            case _ if now.month == 12 and now.day == 30 and now.month == 1 and now.day < 10:
                message ="🎉 Happy New Year 🎉"

            case _: 
                message = None

        return message
