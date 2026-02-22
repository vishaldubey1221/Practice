# task 1 : Ek program likho jo number input le aur bataye ki woh positive, negative, ya zero hai.
# a = int(input("Enter the Number :"))
# if a >= 0:
#     print("The Number is positive")
# else:
#     print("Number is Neg")

#task 2 : 1 se 10 tak ka table print karo using for loop.
# for i in range(1,11):
#     print(f"\n---table of {i}-----")
#     for j in range(1,11):
#         print(f"{i}x{j} = {i*j}")


#task3 :  List numbers = [10, 25, 30, 45, 50]
# mein se sirf even numbers print karo. Hint: % operator
# use karo.
# List_numbers = [10, 25, 30, 45, 50]
# for num in List_numbers:
#     if num%2 != 0:
#         print(num)




# task 4 :  User se age input lo. Agar age 13-19 ke
# beech hai toh "Teenager", 20-59 toh "Adult", 60+ toh
# "Senior Citizen" print karo.

# i = int(input("Enter your age :"))
# if i>=13 and i<=19:
#     print("Teanager")
# elif i>=20 and i<=59:
#     print("Adult")
# else:
#     print("Senoir Citizen")



# for i in range(3):
#     for j in range(2):
#         print(i * j, end=" ")
#     print()


List_prices = [100, 250, 300, 450, 600]
# mein se 300 se zyada wale items ka total price calculate
# kar
total_sum = print(sum([price for price in List_prices if price>300]))
