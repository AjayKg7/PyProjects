def solve (N, start, finish, Ticket_cost):
    # Write your code here
    if finish == N and start == 1:
        if sum(Ticket_cost[start-1:-1]) > Ticket_cost[-1]:
            return Ticket_cost[-1]
        return sum(Ticket_cost[start-1:-1])

    else:
        if finish > start:
            #forward
            min_cost1 = sum(Ticket_cost[start-1:finish-1])
            min_cost2 = 0
            #reverse
            if start == 1:
                min_cost2 = sum(Ticket_cost[finish-1:])
            else:
                min_cost2=sum(Ticket_cost[finish-1:]) + sum(Ticket_cost[:start-1])
            if min_cost2 < min_cost1 :
                return min_cost2
            return min_cost1
        else:
            return sum(Ticket_cost[finish-1:start-1])


N = int(input())
start = int(input())
finish = int(input())
Ticket_cost = list(map(int, input().split()))

out_ = solve(N, start, finish, Ticket_cost)
print (out_)