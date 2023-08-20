destinations = ["sweden", "germany", "japan", "greece"]

print(f"list: {destinations}")
print(f"temporarily sorted list: {sorted(destinations)}")
print(f"list: {destinations}")
print(f"temporarily sorted list in reverse: {sorted(destinations, reverse=True)}")

destinations.reverse()
print(f"permanently reversed list: {destinations}")
destinations.reverse()
print(f"permanently reversed back list: {destinations}")

destinations.sort()
print(f"permanently sorted list: {destinations}")
destinations.sort(reverse=True)
print(f"permanently sorted reversed list: {destinations}")