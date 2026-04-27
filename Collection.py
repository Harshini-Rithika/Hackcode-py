N = int(input())
Student = namedtuple('Student', input().split())
marks = [int(Student(*input().split()).MARKS) for _ in range(N)]
print("{:.2f}".format(sum(marks) / N))
n = int(input())
Student = namedtuple('Student', input().split())
total_marks = sum(int(Student(*input().split()).MARKS) for _ in range(n))
print("{:.2f}".format(total_marks / n))