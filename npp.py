def npp_formula(jobs, arrival_time, burst_time, priority):
    n = len(jobs)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    remaining_priority = list(priority)
    current_time = 0
    min_burst = float('inf')

    for i in range(n):
        min_priority = float('inf')
        next_job = None

        for i in range(n):
            if arrival_time[i] <= current_time and remaining_priority[i] <= min_priority:
                if burst_time[i] > min_burst and remaining_priority[i] == min_priority:
                    continue
                min_burst = burst_time[i]
                min_priority = remaining_priority[i]
                next_job = i
        
        if next_job is None:
            current_time += 1
            continue

        waiting_time[next_job] = current_time - arrival_time[next_job]

        current_time += burst_time[next_job]
        turnaround_time[next_job] = waiting_time[next_job] + burst_time[next_job]

        remaining_priority[next_job] = float('inf')

    return arrival_time, burst_time, priority, waiting_time, turnaround_time

def main():    
    print("================================================")
    print("Welcome to the Non Preemptive Priority Simulator")
    print("================================================")

    process = int(input(f"Enter number of process: "))
    n = process
    jobs = [chr(ord('A') + i) for i in range(n)]
    arrival_time = []
    burst_time = []
    priority = []

    for i in range(n):
        print("")
        arrival_time.append(int(input(f"Enter arrival time for the job {jobs[i]}: ")))
        burst_time.append(int(input(f"Enter burst time for the job {jobs[i]}: ")))
        priority.append(int(input(f"Enter priority for the job {jobs[i]}: ")))
    
    arrival_time, burst_time, priority, waiting_time, turnaround_time = npp_formula(jobs, arrival_time, burst_time, priority)

    print("\nR  E  S  U  L  T")
    print("------------------------------------------------")
    print("   Job\t|   AT\t|   BT\t|   P\t|  TAT\t|   WT")
    for i in range(n):
        print(f"    {jobs[i]}\t|   {arrival_time[i]}\t|   {burst_time[i]}\t|   {priority[i]}\t|   {turnaround_time[i]}\t|   {waiting_time[i]}")
    print("------------------------------------------------")


main()