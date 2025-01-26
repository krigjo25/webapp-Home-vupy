
from cs50 import SQL


class DatabaseInteraction():

    def __init__(self):
        self.sql = SQL("sqlite:///birthdays.db")

    def InsertRecord(self, arg):
        pass

    def DeleteRecord(self, arg):

            # Removes a record from the database
            self.sql.execute(f"DELETE FROM birthdays WHERE id=?;", arg)
            return

    def OrderRecord(self, arg):
        pass
    def UpdateRecord(self, arg):
        try:
            bday = [i for i in arg['updated_bday']]
            if len(bday) != 3: raise Exception('Date must be formated day/month')
            if not str(arg['updated_name']).isalpha(): raise Exception('Name must contain only letters')

        except Exception as e: return e

        print(f"day {bday[0]}, month: {bday[2]}, id: {arg['id']}, name : {arg['updated_name']}")
        #   Update records
        self.sql.execute("UPDATE birthdays SET day = ? WHERE id=?;", bday[0], arg['id'])
        self.sql.execute("UPDATE birthdays SET month = ? WHERE id=?;", bday[2], arg['id'])
        self.sql.execute("UPDATE birthdays SET name = ? WHERE id=?;", arg['updated_name'], arg['id'])
        #   Clean up
        del arg
        del bday

        return
