customers=[
  (101,"Ravi",25000),
  (102,"Kiran",30000),
  (103,"Arun",35000),
  (104,"Priya",40000),
  (105,"John",45000)
]

print("Customer Processing Started")

for customer in customers:
  print(customer)

print("Customer Processing Completed")

def calculate_bonus(sal):
  return sal*0.1
sal=50000