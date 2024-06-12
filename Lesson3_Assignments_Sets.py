# Set Operations in Data Analysis

# Task 1 : Flight Route Comparison 

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def main():
    while True:
        input1 = input(''' 
Flight Comparison
                       
1- View Destinations
2- Destination both airlines fly to
3- Unique airline destinations
4- Destinations not shared
5- Quit
 ''')
        if input1 == "1":
            print("Our Routes")
            print(our_routes)
            print("Competitor Routes")
            print(competitor_routes)
        elif input1 == "2":
            both()
        elif input1 == "3":
            unique()
        elif input1 == "4":
            not_shared()
        elif input1 == "5":
            break
        else:
            print(" Please enter a valid input")
            continue
def both():
    intersect = our_routes.intersection(competitor_routes)
    our_routes.intersection(competitor_routes)
    print("Destinations both airlines fly to")
    print(intersect)

def unique():
    unique_destinations = our_routes.difference(competitor_routes)
    print("Unique destinations your airline")
    print(unique_destinations)

def not_shared():
    neither_share = our_routes.symmetric_difference(competitor_routes)
    print("Destinations neither airlines share")
    print(neither_share)

main()

# Set Operations in Data Analysis

# Task 1 : Duplicate Entries Cleanup

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

set_list = set(customer_ids)
print(f"Unique customer IDs",set_list)
