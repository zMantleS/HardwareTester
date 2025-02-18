prompt = int(input("Hello, choose:\n----------------------\n1: Memory Stress Test\n2: Disk Stress Test\n3: Network Stress Test\n4: CPU Stress Test\n5: MySQL Stress Test\n----------------------\n> "))
match prompt:
    case 1:
        print("Memory stress test")
    case 2:
        print("Disk stress test")
    case 3:
        print("Network stress test")
    case 4:
        print("CPU stress test")
    case 5:
        print("MySQL stress test")