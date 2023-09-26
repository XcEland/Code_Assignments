"""
Registration Number:R213273B
Name:    Courtney Ganyiwa
Program: DAH
Module : Health Records
njabulobass@gmail.com
"""


import datetime


class HealthRecord:
    def __init__(self, record_id, name, date_of_birth, gender, condition, blood_pressure, heart_rate, respiratory_rate, temperature, record_date, prescription, bills):
        self.record_id = record_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.condition = condition
        self.blood_pressure = blood_pressure
        self.heart_rate = heart_rate
        self.respiratory_rate = respiratory_rate
        self.temperature = temperature
        self.record_date = record_date
        self.prescription = prescription
        self.bills = bills

    def display(self):
        """
        Displays the details of the health record.
        """
        print("Record ID:", self.record_id)
        print("Name:", self.name)
        print("Date of Birth:", self.date_of_birth)
        print("Gender:", self.gender)
        print("Condition:", self.condition)
        print("Blood Pressure:", self.blood_pressure)
        print("Heart Rate:", self.heart_rate)
        print("Respiratory Rate:", self.respiratory_rate)
        print("Temperature:", self.temperature)
        print("Record Date:", self.record_date)
        print("Prescription:", self.prescription)
        print("Bills:", self.bills)

    def update(self, field, value):
        """
        Updates the specified field with the given value.

        Args:
            field (str): The field to update.
            value: The new value for the field.
        """
        
        if field == "name":
            self.name = value
        elif field == "date_of_birth":
            self.date_of_birth = value
        elif field == "gender":
            self.gender = value
        elif field == "condition":
            self.condition = value
        elif field == "blood_pressure":
            self.blood_pressure = value
        elif field == "heart_rate":
            self.heart_rate = value
        elif field == "respiratory_rate":
            self.respiratory_rate = value
        elif field == "temperature":
            self.temperature = value
        elif field == "record_date":
            self.record_date = value
        elif field == "prescription":
            self.prescription = value
        elif field == "bills":
            self.bills = value
        else:
            print("Invalid field!")

    def delete(self):
        """
        Deletes the health record.
        """
        del self


def create_record(records):
    """
    Creates a new health record and adds it to the list of records.

    Args:
        records (list): The list of existing health records.

    Returns:
        HealthRecord: The newly created health record.
    """
    record_id = len(records) + 1
    name = input("Enter name: ")
    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
    gender = input("Enter gender: ")
    condition = input("Enter condition: ")
    blood_pressure = input("Enter blood pressure: ")
    heart_rate = input("Enter heart rate: ")
    respiratory_rate = input("Enter respiratory rate: ")
    temperature = input("Enter temperature: ")
    record_date = datetime.datetime.now()
    prescription = input("Enter prescription: ")
    bills = input("Enter bills: ")
    record = HealthRecord(record_id, name, date_of_birth, gender, condition, blood_pressure, heart_rate, respiratory_rate, temperature, record_date, prescription, bills)
    records.append(record)
    return record


def read_record(records):
    """
    Reads and displays the details of a specific health record.

    Args:
        records (list): The list of existing health records.
    """
    record_id = int(input("Enter record ID: "))
    found = False
    for record in records:
        if record.record_id == record_id:
            record.display()
            found = True
            break
    if not found:
        print("Record not found!")


def update_record(records):
    """
    Updatesthe details of a specific health record.

    Args:
        records (list): The list of existing health records.
    """
    record_id = int(input("Enter record ID: "))
    found = False
    for record in records:
        if record.record_id == record_id:
            field = input("Enter field to update: ")
            value = input("Enter new value: ")
            record.update(field, value)
            found = True
            print("Record updated successfully!")
            break
    if not found:
        print("Record not found!")


def delete_record(records):
    """
    Deletes a specific health record.

    Args:
        records (list): The list of existing health records.
    """
    record_id = int(input("Enter record ID: "))
    found = False
    for record in records:
        if record.record_id == record_id:
            record.delete()
            records.remove(record)
            found = True
            print("Record deleted successfully!")
            break
    if not found:
        print("Record not found!")


def main():
    """
    The main function that controls the flow of the program.
    """
    records = []

    while True:
        print("\n--- Health Record CRUD ---")
        print("1. Create Record")
        print("2. Read Record")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            record = create_record(records)
            print("Record created successfully!")

        elif choice == 2:
            if not records:
                print("No records found!")
            else:
                read_record(records)

        elif choice == 3:
            if not records:
                print("No records found!")
            else:
                update_record(records)

        elif choice == 4:
            if not records:
                print("No records found!")
            else:
                delete_record(records)

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()