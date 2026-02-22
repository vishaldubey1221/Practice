#task 1:
# sales_data = [100, -50, 200, 300, -20, 150]
# valid_sales = []
# for sale in sales_data:
#     if sale >0:
#         valid_sales.append(sale)
#         print(valid_sales)



#task 2:
# data_points = [10, 20, None, 30, None, 50, None]
# count = 0
# for i in data_points:
#     if i is None :
#        count = count+1
# print(count)

# total_count = print(len([i for i in data_points if i is None]))


#task 3 
# visitors = [800, 1200, 950, 1500, 700]
# for i in visitors:
#     if i > 1000:
#         print(f"visitors {i}:Alert!")
#     else:
#         print(f"visitors {i}:Normal")


#task 4 
#transactions = [200, 100, 0, 500, 0, 300]
# Total_transections = print(sum([a for a in transactions if a is not 0]))
# total_revenue =0
# for t in transactions:
#     if t is not 0:
#         total_revenue = total_revenue+t
# print(total_revenue)


# task 5 
# prices = [1200, 400, 750, 200, 1500]
# for price in prices:
#     if price>1000:
#         print(f"{price}:premium")
#     elif price>500 and 1000:
#         print(f"{price}:Standard")
#     else:
#         print(f"{price}:Budget")


#task 6 :
daily_sales = [150, 300, 120, 450, 200]
# max_sales = 0
# for d in daily_sales:
#     if d > max_sales:
#         max_sales = d
# print("Highest_sale :",max_sales)
# a = max(daily_sales)
# print(a)

#task 7:
# cart_amounts = [400, 600, 300, 800]

# for disc in cart_amounts:
#     if disc > 500:
#         disc_amt = (disc-(disc*0.1))
#         print(f"Discount 10% off :{disc_amt}")
#     else:
#         print(disc)

#task 7:
# logs = ["Success", "Success", "Warning", "Error", "Success"]
# for a in logs:
#     if a == "Error":
#         break
#     print("Processing Stoped",a)


# logs = ["Success", "Success", "Warning", "Error", "Success"]
# for log in logs:
#     if log == "Error":
#         print("Processing Stopped")
#         break
#     print(f"Log: {log}")

#task 9:
ratings = [4.0, 4.8, 3.9, 4.9, 4.5]
experience = [3, 5, 2, 1, 4]
elg_count = 0
for i in range(len(ratings)):
    if ratings[i]>=4.5 and experience[i]>2:
        elg_count += 1
print("Eligible for bonous ",elg_count)
        
# eligible_count = 0

# # Range function use karke index access kar rahe hain
# for i in range(len(ratings)):
#     if ratings[i] >= 4.5 and experience[i] > 2:
#         eligible_count += 1
# print("Employees eligible for bonus:", eligible_count)
 