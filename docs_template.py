import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate

doc = DocxTemplate("./source/docs_template.docx")
my_name = "Ivan Benedictus"
my_phone = "+62 851-5900-7279"
my_email = "ivan.benedictuss@gmail.com"
my_address = "Jalan Bukit 123, Tangerang Selatan"
today_date = datetime.today().strftime("%d %b, %Y")

my_context = {"my_name": my_name, "my_phone": my_phone, "my_email": my_email, "my_address": my_address,
              "today_date": today_date}


# Iterate for every hiring managers
df = pd.read_csv("./source/fake_data.csv")

for index, row in df.iterrows():
    
    context = {"hiring_manager_name": row["name"],
               "address": row["address"],
               "phone_number": row["phone_number"],
               "email": row["email"],
               "job_position": row["job"],
               "company_name": row["company"]}

    context.update(my_context)

    doc.render(context)
    doc.save(f"./output/generated_docs{index}.docx")