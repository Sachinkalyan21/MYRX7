def sort_hashmap_by_value(input_map):
    # Sort the hashmap by value
    sorted_map = dict(sorted(input_map.items(), key=lambda item: item[1]))
    return sorted_map

# Example usage
input_map = {101: "John Doe", 102: "Jane Smith", 103: "Peter Johnson"}
output_map = sort_hashmap_by_value(input_map)
print(output_map)
