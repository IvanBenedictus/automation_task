import pandas as pd
from faker import Faker

# Create fake data: name, mail, address
fake = Faker()
profiles = [fake.profile() for i in range(50)]

# Store fake data in Pandas
df = pd.DataFrame(profiles)
df = df[["name", "mail", "address"]]

# Create fake data: phone number, comment
numbers = [fake.phone_number() for i in range(50)]
comment = "-"

# Store fake data in Pandas
df["Phone number"] = numbers
df["Comments"] = comment

# Change column names
df.rename(columns={"name": "Name", "mail": "Email", "address": "Address"}, inplace=True)

# Export data to csv file
df.to_csv("./output/fake_data.csv", index=False)