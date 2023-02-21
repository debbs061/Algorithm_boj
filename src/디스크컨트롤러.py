import heapq

def solution(jobs):

    jobs.sort(key=lambda x: x[0])  # sort jobs by start time
    total_len = len(jobs)
    remaining_jobs = len(jobs)
    pq = []  # priority queue to hold jobs by processing time
    total_time = 0
    current_time = 0
    while pq or remaining_jobs > 0:
        while jobs and jobs[0][0] <= current_time:
            heapq.heappush(pq, jobs.pop(0)[::-1])  # push job into the priority queue in reverse order
        if pq:
            processing_time, start_time = heapq.heappop(pq)
            total_time += current_time - start_time + processing_time
            current_time += processing_time
            remaining_jobs -= 1
        else:
            current_time = jobs[0][0]
    answer = total_time // total_len
    return answer
