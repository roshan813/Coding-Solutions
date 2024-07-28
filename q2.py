import collections

class Solution:
    def __init__(self):
        self.graph = collections.defaultdict(list)
    
    def add_friend(self, person, friend):
        self.graph[person].append(friend)
        self.graph[friend].append(person)
    
    def find_friends(self, person):
        return self.graph[person]
    
    def find_common_friends(self, person1, person2):
        return list(set(self.graph[person1]) & set(self.graph[person2]))
    
    def find_nth_connection(self, person1, person2):
        if person1 == person2:
            return 0
        
        visited = {person: False for person in self.graph}
        distance = {person: float('inf') for person in self.graph}
        q= collections.deque([person1])
        
        visited[person1] = True
        distance[person1] = 0
        
        while q:
            current = q.popleft()
            for friend in self.graph[current]:
                if not visited[friend]:
                    visited[friend] = True
                    distance[friend] = distance[current] + 1
                    q.append(friend)
                    if friend == person2:
                        return distance[friend]
        
        return -1

def main():
    graph = Solution()
    graph.add_friend('Alice', 'Bob')
    graph.add_friend('Bob', 'Janice')
    graph.add_friend('Alice', 'Charlie')
    graph.add_friend('Charlie', 'Alex')
    graph.add_friend('Alex', 'Kevin')
    
    while True:
        print("\n1.Add friend")
        print("2. Find all friends of a person")
        print("3.Find common friends between two people")
        print("4.Find the nth connection between two people")
        print("5.Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            person1 = input("Enter the name of the first person: ")
            person2 = input("Enter the name of the second person: ")
            graph.add_friend(person1, person2)
            print(f"Added {person1} and {person2} as friends.")
        
        elif choice == '2':
            person = input("Enter the name of the person: ")
            friends = graph.find_friends(person)
            print(f"Friends of {person}: {friends}")
        
        elif choice == '3':
            person1 = input("Enter the name of the first person: ")
            person2 = input("Enter the name of the second person: ")
            common_friends = graph.find_common_friends(person1, person2)
            print(f"Common friends of {person1} and {person2}: {common_friends}")
        
        elif choice == '4':
            person1 = input("Enter the name of the first person: ")
            person2 = input("Enter the name of the second person: ")
            connection = graph.find_nth_connection(person1, person2)
            print(f"{person2} is {connection}th connection of {person1}")
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
