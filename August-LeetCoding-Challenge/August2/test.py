import main
import other.other as o

def read_test_case(file_name):
    test_case = open(file_name, 'r')
    actions = test_case.readline()
    numbers = test_case.readline()
    expected_output = test_case.readline()

    return actions.split(','), numbers.split(','), expected_output

def look_for_diff(expected, output):
    print('Expected:', len(expected))
    print('Got:', len(output))
    if len(expected) != len(output):
        print('different length of expected output and my output')

    i = 0
    while i < len(output):
        #print(i,'Expected:', (expected[i]).capitalize())
        #print(i,'Received:', str(output[i]).capitalize(), '\n')
        if expected[i].capitalize() != str(output[i]).capitalize():
            print('Discrepancy:')
            print(i,'Expected:', (expected[i]).capitalize())
            print(i,'Received:', str(output[i]).capitalize(), '\n')
        i += 1
        #input()
    #print(i,'Expected:', (expected[i]).capitalize())
    return

#testing below
obj = o.MyHashSet()
output = []
actions, numbers, expected_output = read_test_case('testcase_24.log')

contains_count = 0
add_count = 0
remove_count = 0
MyHashSet_count = 0

expected = expected_output.split(',')
for i in range(0, len(actions) - 1):
    actions[i] = actions[i].strip('"')
    numbers[i] = numbers[i].strip('[')
    numbers[i] = numbers[i].strip(']')

    if actions[i] == 'add':
        add_count += 1
        obj.add(int(numbers[i]))
        output.append('null')
    elif actions[i] == 'MyHashSet':
        MyHashSet_count += 1
        output.append('null')
    elif actions[i] == 'remove':
        remove_count += 1
        obj.remove(int(numbers[i]))
        output.append('null')
    elif actions[i] == 'contains':
        contains_count += 1
        _ = obj.contains(int(numbers[i]))
        output.append(_)
    else:
        print(actions[i])

print('add count:', add_count)
print('MyHashSet count:', MyHashSet_count)
print('remove count:', remove_count)
print('contains count:', contains_count)

look_for_diff(expected, output)